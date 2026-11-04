# Native abi3t CI: evidence boundaries

Compile a **new illustrative native extension** using Py_TARGET_ABI3T=0x30f0000 with the CPython 3.15.2 regular header; import exactly the **same compiled .abi3t.so** on both regular and free-threaded CPython 3.15.2, checking that the GIL remains disabled in the latter and testing large integers and invalid argument behavior.

This is **not** a certification of arbitrary course native extensions. It does not evaluate any CUDA GPU, commercial binary extension, 3rd party wheel, or Windows native ABI. It complements the 441-demo/full-course test gate, which has not yet been run from the full source tree on GitHub.

Official migration guide: https://docs.python.org/3/howto/abi3t-migration.html
