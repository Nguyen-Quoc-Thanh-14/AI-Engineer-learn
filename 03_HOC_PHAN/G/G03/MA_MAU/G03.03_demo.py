# coding: utf-8
# Bài G03.03 — Tài liệu có thể thực thi độc lập
import json
unsafe_network_payload = '{"status": "ok"}'
assert json.loads(unsafe_network_payload)['status'] == 'ok'
