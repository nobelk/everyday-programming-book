"""Exercise 17.3.1 — Sum of an empty list

Chapter 17 (Testing), section 17.3: Helpful Tips.

Problem
-------
This pytest function tests the edge case of summing an empty list, which should give 0.

Bug type: Logical
-----------------
The function correctly returns 0 for an empty list, but the test asserts 1, so the edge-case check fails. The fix corrects the expected value to 0.

The program below is the corrected version.
"""


def total(numbers):
    running = 0
    for n in numbers:
        running += n
    return running

def test_total_empty():
    assert total([]) == 0
