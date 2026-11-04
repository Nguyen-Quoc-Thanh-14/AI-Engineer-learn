# coding: utf-8
# Bài PA03.02 — Tài liệu có thể thực thi độc lập
actions=[('rename','a','b')]
def execute(actions,dry_run=True):return ['would '+x[0] if dry_run else x[0] for x in actions]
assert execute(actions)==['would rename']
