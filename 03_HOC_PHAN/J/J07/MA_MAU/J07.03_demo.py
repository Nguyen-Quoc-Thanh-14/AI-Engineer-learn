# coding: utf-8
# Bài J07.03 — Tài liệu có thể thực thi độc lập
import sysconfig
assert isinstance(sysconfig.get_config_var('SOABI'),(str,type(None)))
