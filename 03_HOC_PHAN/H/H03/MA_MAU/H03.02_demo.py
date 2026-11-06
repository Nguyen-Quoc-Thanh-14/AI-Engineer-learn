# coding: utf-8
# Bài H03.02 — Tài liệu có thể thực thi độc lập
from unittest.mock import Mock
mailer = Mock()
def signup(email, send):
    send(email, 'welcome')
signup('x@example.com', mailer)
mailer.assert_called_once_with('x@example.com', 'welcome')
