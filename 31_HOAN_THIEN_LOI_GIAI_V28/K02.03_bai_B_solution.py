from array import array
import sys
values=list(range(1000));compact=array('i',values)
assert list(compact)==values
assert sys.getsizeof(compact)<sys.getsizeof(values)
# Shallow getsizeof excludes referenced PyLong objects in list; note this explicitly in report.
