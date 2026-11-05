import logging,re
from io import StringIO
class Redact(logging.Filter):
    def filter(self,record):
        text=record.getMessage();record.msg=re.sub(r'(?i)(api_key|token)=\S+',r'\1=[REDACTED]',text)
        record.args=();return True
buf=StringIO();handler=logging.StreamHandler(buf);handler.addFilter(Redact())
logger=logging.getLogger('lesson.N02.01');logger.handlers.clear();logger.addHandler(handler);logger.propagate=False;logger.setLevel(logging.INFO)
logger.info('operation token=real-secret-value api_key=another-secret')
out=buf.getvalue();assert '[REDACTED]' in out and 'real-secret-value' not in out and 'another-secret' not in out
# Redaction is defense in depth; do not put tokens in log messages in the first place.
