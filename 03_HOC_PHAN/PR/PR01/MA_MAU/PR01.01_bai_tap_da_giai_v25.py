"""PR01.01 corrected: Structure c_double, sizeof and native alignment."""
import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x",ctypes.c_int),("y",ctypes.c_double)]

def layout():
    return {"size":ctypes.sizeof(Point),
            "alignment":ctypes.alignment(Point),
            "x_offset":Point.x.offset,
            "y_offset":Point.y.offset,
            "c_int_size":ctypes.sizeof(ctypes.c_int),
            "c_double_size":ctypes.sizeof(ctypes.c_double),
            "c_double_alignment":ctypes.alignment(ctypes.c_double)}
def check():
    p=Point(7,1.25)
    assert p.x==7 and p.y==1.25
    d=layout()
    assert d["x_offset"]==0
    assert d["y_offset"]>=d["c_int_size"]
    assert d["y_offset"]%d["c_double_alignment"]==0
    assert d["size"]>=d["y_offset"]+d["c_double_size"]
    assert d["size"]%d["alignment"]==0
    assert d["alignment"]>=d["c_double_alignment"]
if __name__=="__main__":
    check()
    print("PASS PR01.01",layout())
