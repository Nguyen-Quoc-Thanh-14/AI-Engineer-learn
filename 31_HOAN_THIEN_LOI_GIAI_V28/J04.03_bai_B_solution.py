trace=[]
class Descriptor:
    def __set_name__(self,owner,name):trace.append(('set_name',name))
class Base:
    def __init_subclass__(cls,**kwargs):
        trace.append(('init_subclass',cls.__name__))
        super().__init_subclass__(**kwargs)
class Metaclass(type):
    def __new__(mcls,name,bases,namespace):
        trace.append(('meta_new',name))
        return super().__new__(mcls,name,bases,namespace)
class Child(Base,metaclass=Metaclass):
    field=Descriptor()
assert trace==[('meta_new','Child'),('set_name','field'),('init_subclass','Child')]
assert Child.__mro__==(Child,Base,object)
