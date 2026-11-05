#!/usr/bin/env python3
"""Automated course structure and link auditing; NEVER a human review."""
import csv
import hashlib
import json
from pathlib import Path
import re
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"evidence"/"curriculum_quality"
FENCE=re.compile(r"(?ms)^[ \t]*" + chr(96)*3 + r".*?^[ \t]*" + chr(96)*3 + r"[ \t]*$")
LINK=re.compile(r"\[[^]\n]+\]\(([^)\n]+)\)")
BLOCKING_FLAGS={"INVALID_ID","TITLE_MISMATCH","NO_DEMO","NO_ANSWER","BROKEN_LOCAL_LINK"}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def broken_links(path, source):
    s=FENCE.sub("",source)
    # Ignore Markdown inline code, including link-shaped syntax inside type expressions.
    tick=chr(96)
    s=re.sub(re.escape(tick)+r"[^"+re.escape(tick)+r"\n]*"+re.escape(tick),"",s)
    out=[]
    for raw in LINK.findall(s):
        target=raw.strip().split()[0].strip("<>").split("#")[0].split("?")[0]
        if not target or target.startswith(("http://","https://","mailto:","data:")) or "://" in target:
            continue
        dest=(path.parent/target).resolve()
        if not dest.is_relative_to(ROOT.resolve()):
            out.append("OUTSIDE_ROOT:"+raw)
        elif not dest.exists():
            out.append(raw)
    return out

def run():
    lessons=sorted(ROOT.glob("03_HOC_PHAN/**/BAI_HOC/*.md"))
    demos=sorted(ROOT.glob("03_HOC_PHAN/**/MA_MAU/*_demo.py"))
    executable=sorted(ROOT.glob("31_HOAN_THIEN_LOI_GIAI_V28/*_bai_B_solution.py"))
    lc=[x.stem for x in lessons]
    dc=[x.name.removesuffix("_demo.py") for x in demos]
    ec=[x.name.removesuffix("_bai_B_solution.py") for x in executable]
    errors=[]
    if len(lessons)!=441 or len(set(lc))!=441:errors.append("441 unique lesson files required")
    if len(demos)!=441 or set(lc)!=set(dc):errors.append("exactly matching 441 demos required")
    if len(executable)!=95 or len(set(ec))!=95:errors.append("exactly 95 standalone B solution programs required")
    rows=[]
    for p in lessons:
        code=p.stem
        demo=p.parent.parent/"MA_MAU"/(code+"_demo.py")
        ans=p.parent.parent/"LOI_GIAI"/(code+"_loi_giai.md")
        s=p.read_text(encoding="utf8",errors="replace")
        a=ans.read_text(encoding="utf8",errors="replace") if ans.exists() else ""
        broken=broken_links(p,s)+(broken_links(ans,a) if ans.exists() else [])
        flags=[]
        if not re.fullmatch(r"[A-Z]{1,2}\d{2}\.\d{2}",code):flags.append("INVALID_ID")
        if not s.startswith("# "+code):flags.append("TITLE_MISMATCH")
        if not demo.exists():flags.append("NO_DEMO")
        if not ans.exists():flags.append("NO_ANSWER")
        if (chr(96)*3+"python") not in s and "_demo.py" not in s:flags.append("NO_CODE_OR_DEMO_REFERENCE")
        if not any(marker in s for marker in ("Bài B","Bài tập","Thực hành","Luyện tập")):flags.append("NO_EXERCISE_MARKER")
        if "http://" not in s and "https://" not in s:flags.append("NO_SOURCE_LINK")
        if "Lời giải thiết kế" in a or "Lời giải dạng thiết kế" in a:flags.append("DESIGN_ANSWER_NEEDS_HUMAN")
        if re.search(r"chưa (kiểm định trực tiếp|xác nhận trực tiếp).{0,30}3\.15\.2",s,re.I):
            flags.append("POSSIBLE_STALE_VERSION_CLAIM")
        if broken:flags.append("BROKEN_LOCAL_LINK")
        rows.append({"id":code,"lesson":p.relative_to(ROOT).as_posix(),
                     "lesson_sha256":sha(p),"demo_sha256":sha(demo) if demo.exists() else "",
                     "answer_sha256":sha(ans) if ans.exists() else "",
                     "part":p.parts[1],"word_count":len(s.split()),
                     "high_risk":bool(re.match(r"^(N|L|PM|PR|PL)\d",code)),
                     "has_executable_B":code in ec,
                     "review_status":"AWAITING_EXTERNAL_REVIEW",
                     "flags":";".join(flags),"broken_link_count":len(broken),
                     "broken_links_sample":";".join(broken[:4])})
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"lessons_441.csv").open("w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    flagcounts=Counter(flag for r in rows for flag in r["flags"].split(";") if flag)
    blockers=[{"lesson_id":r["id"],"flags":[f for f in r["flags"].split(";") if f in BLOCKING_FLAGS]}
              for r in rows if any(f in BLOCKING_FLAGS for f in r["flags"].split(";"))]
    if blockers:
        errors.append(f"{len(blockers)} lesson(s) with structural blocking defects")
    report={
        "inventory_integrity":"PASS" if not errors else "FAIL",
        "inventory_errors":errors,
        "blocking_lesson_count":len(blockers),
        "blocking_lessons_sample":blockers[:20],
        "audit_scope":"inventory and structural integrity; flagged lesson quality requires human review",
        "lesson_count":len(lessons),"demo_count":len(demos),"executable_B_count":len(executable),
        "answers_found":sum(bool(r["answer_sha256"]) for r in rows),
        "review_accepted_by_verified_experts":0,
        "risk_signal_counts":dict(flagcounts),
        "broken_links_total":sum(int(r["broken_link_count"]) for r in rows),
        "limits":"File presence, code fence and links are NOT proof of pedagogy, correctness, independence or safety."
    }
    (OUT/"summary.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
    print(json.dumps(report,ensure_ascii=False))
    return 0 if not errors else 2

if __name__=="__main__":
    raise SystemExit(run())
