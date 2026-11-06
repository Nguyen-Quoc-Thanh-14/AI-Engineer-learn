from pathlib import Path
from tempfile import TemporaryDirectory
text='Tiếng Việt: Đà Nẵng 🌱'
with TemporaryDirectory() as tmp:
    p=Path(tmp)/'content.txt'; p.write_text(text,encoding='utf-8')
    assert p.read_bytes()==text.encode('utf-8')
    assert p.read_text(encoding='utf-8')==text
# Always specify encoding explicitly for portable file interchange.
