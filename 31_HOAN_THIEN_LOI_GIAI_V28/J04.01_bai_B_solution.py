class Temp:
    @property
    def celsius(self):return self._c
    def __init__(self,c):self._c=c
x=Temp(20)
assert object.__getattribute__(x,'celsius')==20
assert type.__getattribute__(Temp,'celsius') is Temp.__dict__['celsius']
# Class attribute access returns the descriptor object; instance access calls its __get__.
