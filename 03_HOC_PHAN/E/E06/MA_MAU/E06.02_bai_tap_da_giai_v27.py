# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
class UserService:
    def __init__(self, repository): self.repo=repository
    def display(self, user_id):
        try: return self.repo.get(user_id)['name']
        except (KeyError, TypeError, TimeoutError): return None
class FakeRepo:
    def __init__(self, behavior): self.behavior=behavior
    def get(self, user_id):
        if isinstance(self.behavior,Exception): raise self.behavior
        return self.behavior
assert UserService(FakeRepo({'name':'A'})).display(1)=='A'
assert UserService(FakeRepo(KeyError('x'))).display(1) is None
assert UserService(FakeRepo(TimeoutError())).display(1) is None
print('PASS E06.02')
