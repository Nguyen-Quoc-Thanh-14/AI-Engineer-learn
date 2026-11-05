from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as tmp:
    root=Path(tmp)
    (root/'.env.example').write_text('API_KEY=replace-me\n',encoding='utf-8')
    (root/'.gitignore').write_text('.env\n',encoding='utf-8')
    assert 'replace-me' in (root/'.env.example').read_text()
    assert '.env' in (root/'.gitignore').read_text()
    assert not (root/'.env').exists()
# Incident response: revoke exposed key, issue a new key, inspect logs, invalidate caches,
# remove secret from tracked history with expert-reviewed procedure and notify owners.
