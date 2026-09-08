"""Exercise 17.3.5 — Approximate division

Chapter 17 (Testing), section 17.3: Helpful Tips.

Problem
-------
This pytest function uses `pytest.approx` to check that dividing 1 by 3 is about 0.3333.

Bug type: Logical
-----------------
Setting `abs=0` gives `pytest.approx` zero tolerance, so 0.3333… never matches 0.3333 and the test fails. Using a small tolerance (or the default) lets the approximate comparison succeed.

The program below is the corrected version.
"""


import pytest

def divide(a, b):
    return a / b

def test_divide():
    assert divide(1, 3) == pytest.approx(0.3333, abs=1e-4)
