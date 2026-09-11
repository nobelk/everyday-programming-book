"""Exercise 18.2.5 — Doubling a recipe

Chapter 18 (Testing), section 18.2: Testing with Pytest.

Problem
-------
This pytest function should verify that doubling 3 cups of flour gives 6 cups.

Bug type: Syntax
----------------
The assert uses a single `=` (assignment) instead of `==` (comparison), which is a syntax error. Using `==` fixes the comparison.

The program below is the corrected version.
"""


def double_recipe(cups):
    return cups * 2

def test_double_recipe():
    assert double_recipe(3) == 6
