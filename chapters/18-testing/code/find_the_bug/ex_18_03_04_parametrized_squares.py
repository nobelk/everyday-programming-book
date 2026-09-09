"""Exercise 18.3.4 — Parametrized squares

Chapter 18 (Testing), section 18.3: Helpful Tips.

Problem
-------
This parametrized pytest checks that squaring 0, 2, and 5 gives 0, 4, and 25.

Bug type: Logical
-----------------
The third parameter case expects 20, but 5² = 25, so that case fails. Correcting the expected value to 25 makes all parametrized cases pass.

The program below is the corrected version.
"""


import pytest

def square(n):
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (2, 4),
    (5, 25),
])
def test_square(n, expected):
    assert square(n) == expected
