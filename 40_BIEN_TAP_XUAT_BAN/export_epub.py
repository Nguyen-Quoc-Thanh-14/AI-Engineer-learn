#!/usr/bin/env python3
"""Convert preview manuscripts into EPUB3 with installed Pandoc."""
from pathlib import Path
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
OUTPUT=HERE/"_build"

def main():
    exe=shutil.which("pandoc")
    if not exe:
        raise RuntimeError("Pandoc required for EPUB3, no silent skip")
    source=sorted(OUTPUT.glob("TAP_*.md"))
    if len(source)!=10:
        raise RuntimeError("Need 10 Markdown manuscripts, found " + str(len(source)))
    for doc in source:
        dest=doc.with_suffix(".epub")
        cmd=[exe, "-f","gfm","-t","epub3","--toc","--css",str(OUTPUT/"print.css"),
             "--metadata","lang=vi",str(doc),"-o",str(dest)]
        subprocess.run(cmd,check=True,timeout=180)
        if dest.stat().st_size < 1200:
            raise RuntimeError("EPUB too small: "+str(dest))
        print("EPUB_OK",dest.name,dest.stat().st_size,flush=True)
    print("EPUB_PREVIEW_READY",len(source))

if __name__=="__main__":
    sys.exit(main())
