# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import tomllib
payload=b'''[project]
name = "my-demo"
version = "0.1.0"
[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.9"]
'''
obj=tomllib.loads(payload.decode())
assert obj['project']['name']=='my-demo'
assert 'pytest>=8' in obj['project']['optional-dependencies']['dev']
assert len(obj['project']['optional-dependencies']['dev'])==2
print('PASS F02.03')
