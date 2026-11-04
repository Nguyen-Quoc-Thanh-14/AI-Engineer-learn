# coding: utf-8
# Bài PR02.01 — Tài liệu có thể thực thi độc lập
import sysconfig
suffix=sysconfig.get_config_var('EXT_SUFFIX')
assert isinstance(suffix,(str,type(None)))
