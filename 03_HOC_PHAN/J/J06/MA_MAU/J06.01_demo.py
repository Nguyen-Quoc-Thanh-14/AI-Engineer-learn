# coding: utf-8
# Bài J06.01 — Tài liệu có thể thực thi độc lập
import dis
code=compile('a=2+3', '<demo>', 'exec')
ops=[ins.opname for ins in dis.get_instructions(code)]
assert ops and ('RETURN_VALUE' in ops or 'RETURN_CONST' in ops)
