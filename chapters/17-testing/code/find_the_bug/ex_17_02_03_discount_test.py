"""Exercise 17.2.3 — Discount test

Chapter 17 (Testing), section 17.2: Testing with Pytest.

Problem
-------
This pytest function should check that a 20% discount on a $50 item leaves a $40 price.

Bug type: Logical
-----------------
A pytest test should check with `assert` and not `return` a value; the trailing `return True` makes the test look like it passes regardless. Removing it leaves the assertion as the real check.

The program below is the corrected version.
"""


def discounted_price(price, percent_off):
    return price - price * percent_off / 100

def test_discounted_price():
    assert discounted_price(50, 20) == 40
