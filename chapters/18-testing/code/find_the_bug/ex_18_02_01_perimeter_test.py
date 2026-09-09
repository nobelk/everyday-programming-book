"""Exercise 18.2.1 — Perimeter test

Chapter 18 (Testing), section 18.2: Testing with Pytest.

Problem
-------
This pytest function checks that the perimeter of a square with side 5 is 20.

Bug type: Logical
-----------------
The function correctly returns 4 × 5 = 20, but the test asserts 25, so it fails. The fix corrects the expected value to 20.

The program below is the corrected version.
"""


def square_perimeter(side):
    return 4 * side

def test_square_perimeter():
    assert square_perimeter(5) == 20
