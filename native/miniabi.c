/* Minimal CPython 3.15 abi3t module. No mutable global Python state. */
#define Py_TARGET_ABI3T 0x30f0000
#include <Python.h>

#if Py_TARGET_ABI3T != 0x30f0000
#error "This example requires abi3t targeting CPython 3.15"
#endif

static PyObject* multiply_two(PyObject *self, PyObject *arg) {
    PyObject *two = PyLong_FromLong(2);
    if (two == NULL) return NULL;
    PyObject *result = PyNumber_Multiply(arg, two);
    Py_DECREF(two);
    return result;
}

static PyMethodDef methods[] = {
    {"twice", (PyCFunction)multiply_two, METH_O, "Multiply by two"},
    {NULL, NULL, 0, NULL}
};

PyABIInfo_VAR(abi_info);

static PySlot module_slots[] = {
    PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
    PySlot_STATIC_DATA(Py_mod_name, "miniabi"),
    PySlot_STATIC_DATA(Py_mod_doc, "abi3t minimal module"),
    PySlot_STATIC_DATA(Py_mod_methods, methods),
    PySlot_DATA(Py_mod_gil, Py_MOD_GIL_NOT_USED),
    PySlot_END
};

PyMODEXPORT_FUNC
PyModExport_miniabi(void) {
    return module_slots;
}
