#!/usr/bin/env python3
"""All-source triage for Issue #9; flags are candidates, NOT proof of semantic defects."""
import ast
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from collections import Counter
from difflib import SequenceMatcher

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"evidence"/"issue9_content_qa"
TASK=re.compile(r"\*\*Bài\s+B\s*[-–—]\s*Ứng dụng:\*\*\s*(.+)",re.I)
ANSWER_TASK=re.compile(r"\*\*Đề\s+bài:\*\*\s*(.+)",re.I)
FENCE=re.compile("(?ms)^"+chr(96)*3+r"python[ \t]*\n(.*?)^"+chr(96)*3)
STALE=re.compile(r"chưa (?:kiểm định trực tiếp|xác nhận trực tiếp).{0,30}3\.15\.2",re.I)
FIELDS=("lesson_id","part","lesson_path","lesson_sha256","answer_path","answer_sha256",
        "demo_path","demo_sha256","B_program_path","B_program_sha256",
        "B_prompt","answer_prompt","prompt_similarity","candidate_flags")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def clean(s):
    s=unicodedata.normalize("NFKC",s).casefold()
    return " ".join(re.sub("["+chr(96)+"*_]","",s).split()).strip(" .;")

def capture(p,s):
    m=p.search(s)
    return m.group(1).strip() if m else ""

def parse(s):
    try:return ast.parse(s)
    except SyntaxError:return None

def audit(root=ROOT,expected_lessons=441,expected_programs=95):
    lessons=sorted((root/"03_HOC_PHAN").glob("**/BAI_HOC/*.md"))
    programs=sorted((root/"31_HOAN_THIEN_LOI_GIAI_V28").glob("*_bai_B_solution.py"))
    errors=[]
    if len(lessons)!=expected_lessons:errors.append(f"LESSON_COUNT:{len(lessons)}")
    if len(programs)!=expected_programs:errors.append(f"B_PROGRAM_COUNT:{len(programs)}")
    names=[p.stem for p in lessons]
    if len(set(names))!=len(names):errors.append("DUPLICATE_LESSON_IDS")
    by_id={p.name.removesuffix("_bai_B_solution.py"):p for p in programs}
    if len(by_id)!=len(programs):errors.append("DUPLICATE_B_IDS")
    if set(by_id)-set(names):errors.append("ORPHAN_B_IDS")
    rows=[]
    for lesson in lessons:
        key=lesson.stem
        part=lesson.relative_to(root/"03_HOC_PHAN").parts[0]
        chapter=lesson.parent.parent
        answer=chapter/"LOI_GIAI"/(key+"_loi_giai.md")
        demo=chapter/"MA_MAU"/(key+"_demo.py")
        b=by_id.get(key)
        source=lesson.read_text(encoding="utf8")
        solution=answer.read_text(encoding="utf8") if answer.is_file() else ""
        flags=[]
        for label,p in (("ANSWER",answer),("DEMO",demo)):
            if not p.is_file():
                flags.append("MISSING_"+label)
                errors.append("MISSING_"+label+":"+key)
        if any(t in solution for t in ("Lời giải thiết kế","Lời giải dạng thiết kế")):
            flags.append("DESIGN_ANSWER_REVIEW")
        if STALE.search(source):flags.append("POSSIBLE_STALE_VERSION_CLAIM")
        prompt=capture(TASK,source)
        in_answer=capture(ANSWER_TASK,solution)
        if b and not prompt:flags.append("B_PROMPT_NOT_FOUND_REVIEW")
        if b and not in_answer:flags.append("ANSWER_B_PROMPT_NOT_FOUND_REVIEW")
        ratio=(SequenceMatcher(None,clean(prompt),clean(in_answer)).ratio()
               if prompt and in_answer else 0.0)
        if b and prompt and in_answer and ratio<0.85:
            flags.append("B_VS_ANSWER_PROMPT_CANDIDATE")
        snippet=FENCE.search(solution)
        if b:
            script=parse(b.read_text(encoding="utf8"))
            if script is None:
                flags.append("B_SCRIPT_SYNTAX_ERROR")
                errors.append("B_SCRIPT_SYNTAX_ERROR:"+key)
            elif not any(isinstance(node,ast.Assert) for node in ast.walk(script)):
                flags.append("B_SCRIPT_NO_AST_ASSERT_REVIEW")
            if not snippet:flags.append("ANSWER_NO_EMBEDDED_CODE_REVIEW")
            elif parse(snippet.group(1)) is None:flags.append("ANSWER_SNIPPET_SYNTAX_REVIEW")
            elif script and ast.dump(parse(snippet.group(1)))!=ast.dump(script):
                flags.append("ANSWER_SNIPPET_DIFFERS_FROM_B_SCRIPT_REVIEW")
        rows.append({
            "lesson_id":key,"part":part,
            "lesson_path":lesson.relative_to(root).as_posix(),
            "lesson_sha256":sha(lesson),
            "answer_path":answer.relative_to(root).as_posix() if answer.is_file() else "",
            "answer_sha256":sha(answer) if answer.is_file() else "",
            "demo_path":demo.relative_to(root).as_posix() if demo.is_file() else "",
            "demo_sha256":sha(demo) if demo.is_file() else "",
            "B_program_path":b.relative_to(root).as_posix() if b else "",
            "B_program_sha256":sha(b) if b else "",
            "B_prompt":prompt[:600],"answer_prompt":in_answer[:600],
            "prompt_similarity":f"{ratio:.3f}" if prompt and in_answer else "",
            "candidate_flags":";".join(flags)
        })
    return rows,errors

def main():
    rows,errors=audit()
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"lesson_triage_441.csv").open("w",newline="",encoding="utf8") as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS)
        writer.writeheader();writer.writerows(rows)
    flags=Counter(f for row in rows for f in row["candidate_flags"].split(";") if f)
    report={
        "status":"INVENTORY_PASS_TRIAGE_PENDING" if not errors else "INVENTORY_FAILED",
        "lesson_count":len(rows),
        "standalone_B_count":sum(bool(x["B_program_path"]) for x in rows),
        "parts":dict(sorted(Counter(x["part"] for x in rows).items())),
        "candidate_flag_counts":dict(sorted(flags.items())),
        "lessons_with_any_flag":sum(bool(row["candidate_flags"]) for row in rows),
        "errors":errors[:60],
        "expert_review":"NOT_PERFORMED",
        "limits":"Heuristic flags, prompt similarity, and AST differences need manual confirmation. Exit 0 does not prove lesson/answer semantic alignment."
    }
    (OUT/"summary.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps(report,ensure_ascii=False))
    return 0 if not errors else 2

if __name__=="__main__":
    raise SystemExit(main())
