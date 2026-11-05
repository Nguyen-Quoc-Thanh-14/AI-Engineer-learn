# Compiles a minimal CPython extension in a temporary sandbox against the local interpreter only.
import subprocess,sys,sysconfig,importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
SOURCE=r"""
#define PY_SSIZE_T_CLEAN
#include <Python.h>
static PyObject* add(PyObject* self, PyObject* args) {
    PyObject *a, *b;
    if (!PyArg_ParseTuple(args,"OO",&a,&b)) return NULL;
    if (!PyLong_CheckExact(a) || !PyLong_CheckExact(b)) {
        PyErr_SetString(PyExc_TypeError,"expected two exact Python integers");
        return NULL;
    }
    return PyNumber_Add(a,b);  /* New reference; no C long overflow. */
}
static PyMethodDef methods[]={{"add",add,METH_VARARGS,"Add two C long values"},{NULL,NULL,0,NULL}};
static struct PyModuleDef module={PyModuleDef_HEAD_INIT,"miniadd",NULL,-1,methods};
PyMODINIT_FUNC PyInit_miniadd(void){return PyModule_Create(&module);}
"""
with TemporaryDirectory() as td:
    root=Path(td);src=root/'miniadd.c';src.write_text(SOURCE)
    ext=root/('miniadd'+sysconfig.get_config_var('EXT_SUFFIX'))
    incl=sysconfig.get_path('include')
    build=subprocess.run(['gcc','-shared','-fPIC',f'-I{incl}',str(src),'-o',str(ext)],capture_output=True,text=True,timeout=15)
    assert build.returncode==0,build.stderr
    spec=importlib.util.spec_from_file_location('miniadd',ext)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    assert mod.add(2,3)==5 and mod.add(-3,2)==-1
    assert mod.add(10**100,10**100)==2*10**100
    try: mod.add('invalid',2)
    except TypeError:pass
    else:raise AssertionError('wrong type accepted')
# Compiled against current 3.13 headers; cannot claim Python 3.15 or abi3/abi3t compatibility.
