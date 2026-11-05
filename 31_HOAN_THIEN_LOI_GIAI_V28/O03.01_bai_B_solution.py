import doctest

def square(x):
    """Square a numeric value.

    >>> square(3)
    9
    >>> square(-2)
    4
    """
    return x*x
assert doctest.testmod().failed==0
README="# Sample package\nInstall: `python -m pip install -e .`\nTest: `python -m doctest -v module.py`\nLimitations: no string inputs.\n"
assert 'Limitations' in README
