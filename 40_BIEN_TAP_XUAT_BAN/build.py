#!/usr/bin/env python3
"""Assemble the frozen course sources into five reproducible editorial previews.

All source lessons and solutions are copied, not semantically rewritten. Numbered
section prefixes are normalized for print; original files are never modified.
Publication QA does not confer academic, CUDA, native or free-threaded certification.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import os
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
import tempfile
from urllib.parse import quote, unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONFIG = HERE / "book.json"
EXPECTED_PARTS = {
    "A":16, "B":28, "C":22, "D":19, "E":19,
    "F":16, "G":16, "H":19, "I":22, "J":22,
    "K":16, "L":19, "M":22, "N":16, "O":19,
    "PA":13, "PD":16, "PE":12, "PL":16, "PM":16,
    "PN":13, "PR":12, "PS":13, "PT":13, "PV":13, "PW":13,
}
CODE_FENCE = re.compile(r"^\s{0,3}(" + chr(96) + r"{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})\s+(.+)$")
LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
INLINE_CODE = re.compile(r"(\x60+)(.*?)\1")
TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
CHAPTER_META = re.compile(r"\*\*Chương:\*\*\s*([^·\n]+)")

def sha_bytes(contents: bytes) -> str:
    return hashlib.sha256(contents).hexdigest()

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def source_sha():
    env = os.environ.get("GITHUB_SHA", "").strip()
    if re.fullmatch(r"[a-fA-F0-9]{40}", env):
        return env.lower()
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL, timeout=5
        ).strip()
        if re.fullmatch(r"[a-f0-9]{40}", sha):
            return sha
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
    raise RuntimeError("Explicit commit evidence is required: set GITHUB_SHA")

def lesson_files():
    return sorted(ROOT.glob("03_HOC_PHAN/*/*/BAI_HOC/*.md"),
                  key=lambda p: p.as_posix())

def verify_source_inventory():
    lessons = lesson_files()
    parts = {}
    chapters = set()
    for path in lessons:
        part, chapter = path.parts[-4:-2]
        parts[part] = parts.get(part, 0) + 1
        chapters.add((part, chapter))
        if not re.fullmatch(r"[A-Z]{1,2}\d{2}\.\d{2}", path.stem):
            raise RuntimeError("Invalid source lesson ID: " + str(path))
        if not path.stem.startswith(chapter + "."):
            raise RuntimeError("Lesson/chapter mismatch: " + str(path))
        answer = path.parent.parent / "LOI_GIAI" / (path.stem + "_loi_giai.md")
        if not answer.is_file():
            raise RuntimeError("Missing independent answer: " + str(answer))
    if parts != EXPECTED_PARTS or len(lessons) != 441 or len(chapters) != 137:
        raise RuntimeError(
            "Source inventory differs from editorial snapshot: "
            + repr({"lessons":len(lessons),"chapters":len(chapters),"parts":parts})
        )
    return lessons, parts, chapters

def chapter_title(text: str, code: str) -> str:
    m = CHAPTER_META.search(text)
    name = (m.group(1).strip().rstrip("* .") if m else "")
    return name if name.startswith(code) else code + " — " + name if name else code

def lesson_title(source: str, ident: str) -> str:
    m = TITLE.search(source)
    if not m or not m.group(1).startswith(ident):
        raise RuntimeError("First lesson title does not match source ID: " + ident)
    return m.group(1)

def rewrite_links(line: str, origin: Path, sha: str, warnings: list):
    # Source code signatures in inline code are not Markdown hyperlinks.
    protected = [(m.start(),m.end()) for m in INLINE_CODE.finditer(line)]
    def link(match):
        if any(start <= match.start() < end for start,end in protected):
            return match.group(0)
        label, raw = match.group(1), match.group(2)
        value = raw.strip()
        if value.startswith(("#","https://","http://","mailto:","data:","/")):
            return match.group(0)
        # A raw target with spaces or Markdown title is not reliably parsed.
        if " " in value or "<" in value or ">" in value:
            warnings.append({"kind":"LINK_COMPLEX_TARGET","source":str(origin.relative_to(ROOT)),"value":value})
            return match.group(0)
        parsed = urlsplit(value)
        if parsed.scheme:
            return match.group(0)
        normal = posixpath.normpath(posixpath.join(
            origin.parent.relative_to(ROOT).as_posix(), unquote(parsed.path)))
        file_path = ROOT / normal
        if not file_path.is_file():
            warnings.append({"kind":"LINK_TARGET_NOT_FOUND","source":str(origin.relative_to(ROOT)),"value":value})
            return match.group(0)
        new = "https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/blob/" + sha + "/" + quote(normal, safe="/._-")
        if parsed.fragment:
            new += "#" + quote(parsed.fragment, safe="-_")
        return "[" + label + "](" + new + ")"
    return LINK.sub(link, line)

def adapt_source(source: str, origin: Path, sha: str, warnings: list):
    """Keep lesson prose and code intact; normalize only display heading levels."""
    result = []
    fence = ""
    numbering = 0
    for line in source.splitlines():
        match = CODE_FENCE.match(line)
        if match:
            token = match.group(1)
            if not fence:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = ""
            result.append(line)
            continue
        if not fence:
            match = HEADING.match(line)
            if match:
                level = len(match.group(1))
                heading = match.group(2)
                if level == 2 and re.match(r"^\d+\.\s+", heading):
                    heading = re.sub(r"^\d+\.\s+", "", heading)
                    numbering += 1
                line = "#" * min(6, level + 2) + " " + heading
            line = rewrite_links(line, origin, sha, warnings)
        result.append(line)
    if fence:
        warnings.append({"kind":"UNCLOSED_CODE_FENCE","source":str(origin.relative_to(ROOT))})
    return "\n".join(result).rstrip() + "\n", numbering

def markdown_to_html(text: str, title: str, css: str):
    try:
        import markdown
    except ImportError as exc:
        raise RuntimeError("Install markdown==3.9 for HTML export") from exc
    body = markdown.markdown(
        text, extensions=["fenced_code","tables","toc","sane_lists","attr_list"],
        output_format="html5")
    return (
        '<!doctype html><html lang="vi"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>" + html.escape(title) + "</title><style>"
        + css + "</style></head><body><main>" + body + "</main></body></html>\n"
    )

def build(root: Path = ROOT, output: Path | None = None, sha: str | None = None):
    global ROOT
    original_root = ROOT
    ROOT = root.resolve()
    try:
        source_commit = sha or source_sha()
        if not re.fullmatch(r"[a-f0-9]{40}", source_commit):
            raise ValueError("Source commit must be a full lowercase SHA")
        conf = read_json(CONFIG)
        volumes = conf["volumes"]
        if {p for v in volumes for p in v["parts"]} != set(EXPECTED_PARTS):
            raise RuntimeError("Volume partition does not cover every source part")
        lessons, parts, chapters = verify_source_inventory()
        output = (output or HERE / "_build").resolve()
        if output == ROOT or ROOT in output.parents and not (HERE == output or HERE in output.parents):
            raise ValueError("Build output must be inside publication folder or an external temp directory")
        css = (HERE / "print.css").read_text(encoding="utf-8")
        preface = (HERE / "LOI_NOI_DAU.md").read_text(encoding="utf-8").splitlines()
        if not preface or not preface[0].startswith("# "):
            raise RuntimeError("Invalid editorial preface")
        preface_body = "\n".join(preface[1:]).strip()
        warnings = []
        source_map = []
        files_meta = {}
        def record(path, value):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8", newline="\n")
            files_meta[path.name] = sha_bytes(path.read_bytes())
        with tempfile.TemporaryDirectory(prefix="publication_", dir=output.parent) as tmp:
            draft = Path(tmp)
            for volume in volumes:
                ident = volume["id"]
                chosen = [x for x in lessons if x.parts[-4] in volume["parts"]]
                for kind in ("HOC_VIEN","LOI_GIAI"):
                    is_solution = kind == "LOI_GIAI"
                    heading = conf["title"] + " — " + volume["title"]
                    book = [
                        "# " + heading,
                        "",
                        "**Tập:** " + ident + " · **Phiên bản biên tập:** " + conf["edition"],
                        "",
                        "**Loại:** " + ("Sách lời giải và tham khảo" if is_solution else "Sách học viên"),
                        "",
                        "BẢN XEM TRƯỚC — CHƯA PHÁT HÀNH CHÍNH THỨC.",
                        "",
                        "Nguồn gốc cố định: commit " + source_commit,
                        "",
                        "Các ghi chú phiên bản trong từng bài là dấu vết lịch sử, không phải chứng nhận chất lượng hiện hành.",
                        "Lời giải chỉ dùng để đối chiếu sau khi người học hoàn tất bài.",
                        "",
                        "## Lời nói đầu",
                        "",
                        preface_body,
                        "",
                        "## Mục lục",
                        "",
                    ]
                    chapters_selected = {}
                    for lesson in chosen:
                        code = lesson.parts[-3]
                        chapters_selected.setdefault(code, []).append(lesson)
                    for code, members in chapters_selected.items():
                        sample = members[0].read_text(encoding="utf-8")
                        book.append("- [" + chapter_title(sample, code) + "](#chuong-" + code + ")")
                        for lesson in members:
                            book.append("  - [" + lesson_title(lesson.read_text(encoding="utf-8"), lesson.stem) +
                                        "](#bai-" + lesson.stem.replace(".","-") + ")")
                    book.extend(["", "---", ""])
                    number_removed = 0
                    for code, members in chapters_selected.items():
                        book.append('<a id="chuong-' + code + '"></a>')
                        book.append("## " + chapter_title(members[0].read_text(encoding="utf-8"), code))
                        book.append("")
                        for lesson in members:
                            answer = lesson.parent.parent / "LOI_GIAI" / (lesson.stem + "_loi_giai.md")
                            chosen_path = answer if is_solution else lesson
                            content = chosen_path.read_text(encoding="utf-8")
                            if not is_solution:
                                source_map.append({
                                    "volume":ident, "part":lesson.parts[-4],
                                    "chapter":code,"lesson_id":lesson.stem,
                                    "title":lesson_title(content,lesson.stem),
                                    "lesson_path":lesson.relative_to(ROOT).as_posix(),
                                    "lesson_sha256":sha_bytes(lesson.read_bytes()),
                                    "answer_path":answer.relative_to(ROOT).as_posix(),
                                    "answer_sha256":sha_bytes(answer.read_bytes())
                                })
                            normal, replaced = adapt_source(content, chosen_path, source_commit, warnings)
                            number_removed += replaced
                            book.append('<a id="bai-' + lesson.stem.replace(".","-") + '"></a>')
                            book.append(normal)
                            book.append("")
                            book.append("---")
                            book.append("")
                    name = ident + "_" + kind
                    md = "\n".join(book).rstrip() + "\n"
                    record(draft/(name+".md"),md)
                    record(draft/(name+".html"),markdown_to_html(md,heading,css))
                    warnings.append({
                        "kind":"HEADING_NUMBER_PREFIX_NORMALIZED",
                        "volume":ident,"book":kind,"count":number_removed})
            if len(source_map) != 441 or len({r["lesson_id"] for r in source_map}) != 441:
                raise RuntimeError("Source map did not cover exactly 441 unique lessons")
            with (draft/"source_map.csv").open("w",encoding="utf-8",newline="") as fp:
                writer=csv.DictWriter(fp,fieldnames=list(source_map[0]))
                writer.writeheader()
                writer.writerows(source_map)
            manifest = {
                "edition":conf["edition"],"title":conf["title"],"source_commit":source_commit,
                "status":"EDITORIAL_PREVIEW_NOT_RELEASED",
                "source_lessons":len(lessons),"source_chapters":len(chapters),
                "lesson_parts":parts,
                "volumes":[{"id":v["id"],"name":v["title"],
                            "parts":v["parts"],
                            "lesson_count":sum(parts[p] for p in v["parts"])}
                           for v in volumes],
                "generated_sha256":files_meta,
                "source_map_sha256":sha_bytes((draft/"source_map.csv").read_bytes()),
                "rights_clearance":"REQUIRES_OWNER_APPROVAL",
                "expert_review":"ORAL_FEEDBACK_REPORTED_BY_OWNER; IDENTITY_AND_SCOPE_UNVERIFIED",
                "gpu_hardware_evidence":"NOT_CLAIMED",
                "full_native_freethreaded_evidence":"NOT_CLAIMED",
            }
            (draft/"manifest.json").write_text(
                json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
                encoding="utf-8")
            (draft/"editorial_warnings.json").write_text(
                json.dumps(warnings,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
            shutil.copy2(HERE/"print.css",draft/"print.css")
            if output.exists():
                shutil.rmtree(output)
            draft.rename(output)
        return manifest, warnings
    finally:
        ROOT = original_root

def main():
    parser = argparse.ArgumentParser(description="Generate five volumes plus answer keys")
    parser.add_argument("--sha",help="full Git SHA for reproducible source links")
    parser.add_argument("--output",type=Path,default=HERE/"_build")
    args=parser.parse_args()
    manifest,warnings=build(output=args.output,sha=args.sha)
    for warning in warnings:
        if warning["kind"] in ("LINK_TARGET_NOT_FOUND", "LINK_COMPLEX_TARGET", "UNCLOSED_CODE_FENCE"):
            print("EDITORIAL_WARNING " + json.dumps(warning,ensure_ascii=False),flush=True)
    print(json.dumps({
        "status":manifest["status"],"source_commit":manifest["source_commit"],
        "lessons":manifest["source_lessons"],"chapters":manifest["source_chapters"],
        "volumes":len(manifest["volumes"]),
        "broken_relative_links":sum(w["kind"]=="LINK_TARGET_NOT_FOUND" for w in warnings),
        "uncertain_relative_links":sum(w["kind"]=="LINK_COMPLEX_TARGET" for w in warnings),
        "heading_number_prefixes_normalized":sum(w["count"] for w in warnings
             if w["kind"]=="HEADING_NUMBER_PREFIX_NORMALIZED"),
    },ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
