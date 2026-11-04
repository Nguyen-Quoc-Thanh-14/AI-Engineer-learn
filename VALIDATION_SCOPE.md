# Experimental GitHub validation (not curriculum certification)

Contains FOUR original course examples copied unchanged from version 3.1 and a small test suite.
On each push to the audit branch, GitHub Actions attempts:
- Ubuntu and Windows: CPython 3.15.2, original examples, exact expected stdout.
- Ubuntu free-threaded: CPython 3.15.2t, GIL off, lock-protected thread test.
- Ubuntu CPU: NumPy, pandas, scikit-learn, PyTorch and PyArrow smoke integration.

Not included: the remaining 437 demo scripts, 95 B solution scripts, GPU CUDA, native abi3t, full curriculum certification.
Even all green checks here must NOT be called certification for the 441-lesson curriculum.
Main branch remains untouched; run evidence must be inspected separately.
