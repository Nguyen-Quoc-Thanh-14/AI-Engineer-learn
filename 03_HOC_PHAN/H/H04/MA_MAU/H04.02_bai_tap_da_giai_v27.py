# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import logging, io
log_buffer=io.StringIO()
logger=logging.getLogger('security-demo');logger.handlers.clear();logger.propagate=False
h=logging.StreamHandler(log_buffer);logger.addHandler(h);logger.setLevel(logging.WARNING)
def login(user,password):
    if password!='correct-password':
        logger.warning('login failed for user=%s',user)
        return False
    return True
assert not login('a','secret123')
assert login('a','correct-password')
assert 'secret123' not in log_buffer.getvalue()
assert 'login failed' in log_buffer.getvalue()
print('PASS H04.02')
