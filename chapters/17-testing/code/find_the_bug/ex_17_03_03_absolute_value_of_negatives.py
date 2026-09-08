"""Exercise 17.3.3 — Absolute value of negatives

Chapter 17 (Testing), section 17.3: Helpful Tips.

Problem
-------
This pytest function tests the edge case of a negative input, expecting `abs_value(-7)` to be 7.

Bug type: Logical
-----------------
For a negative input the function returns the number unchanged instead of negating it, so `abs_value(-7)` gives -7. Returning `-number` in the negative branch fixes the edge case.

The program below is the corrected version.
"""


def abs_value(number):
    if number < 0:
        return -number
    return number

def test_abs_value_negative():
    assert abs_value(-7) == 7
