import logging
from io import StringIO
from contextvars import ContextVar
request_id = ContextVar('request_id', default='-')
class RequestFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get()
        return True
out=StringIO();log=logging.getLogger('curriculum.F04.01');log.handlers.clear();log.propagate=False
h=logging.StreamHandler(out);h.addFilter(RequestFilter());h.setFormatter(logging.Formatter('%(request_id)s %(message)s'));log.addHandler(h);log.setLevel(logging.INFO)
token=request_id.set('req-42')
try: log.info('user request completed; sensitive value deliberately excluded')
finally: request_id.reset(token)
s=out.getvalue();assert 'req-42' in s and 'secret' not in s and 'password' not in s
