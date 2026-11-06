/* PR02.01/PR02.02: REAL extension source with Python 3.15 abi3t.
   Stateless per-call operations; no static mutable shared Python objects. */
#define Py_TARGET_ABI3T 0x30f0000
#include <Python.h>

PyABIInfo_VAR(abi_info);

static PyObject *cube_checked(PyObject *self, PyObject *arg) {
    if (!PyLong_Check(arg)) {
        PyErr_SetString(PyExc_TypeError, "cube_checked expects a Python int");
        return NULL;
    }
    PyObject *square = PyNumber_Multiply(arg, arg);
    if (square == NULL) return NULL;
    PyObject *cube = PyNumber_Multiply(square, arg);
    Py_DECREF(square);
    return cube;
}

static PyMethodDef functions[] = {
    {"cube_checked", (PyCFunction)cube_checked, METH_O, "Cube Python ints without C integer overflow"},
    {NULL, NULL, 0, NULL}
};

static PySlot module_slots[] = {
    PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
    PySlot_STATIC_DATA(Py_mod_name, "course_math"),
    PySlot_STATIC_DATA(Py_mod_doc, "Python 3.15 abi3t educational checked-math extension"),
    PySlot_STATIC_DATA(Py_mod_methods, functions),
    PySlot_DATA(Py_mod_gil, Py_MOD_GIL_NOT_USED),
    PySlot_END
};

PyMODEXPORT_FUNC
PyModExport_course_math(void) {
    return module_slots;
}
