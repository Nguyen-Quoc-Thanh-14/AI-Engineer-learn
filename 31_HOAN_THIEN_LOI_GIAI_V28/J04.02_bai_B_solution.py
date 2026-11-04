class RequireName:
    def __init_subclass__(cls,**kwargs):
        super().__init_subclass__(**kwargs)
        if not isinstance(cls.__dict__.get('name'),str) or not cls.name:
            raise TypeError('subclass must define nonempty class attribute name')
class OK(RequireName): name='report'
assert OK.name=='report'
try:
    class Broken(RequireName): pass
except TypeError: pass
else: raise AssertionError('invalid subclass accepted')
