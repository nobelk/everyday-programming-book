"""Exercise 18.2.4 — Counting even numbers

Chapter 18 (Testing), section 18.2: Testing with Pytest.

Problem
-------
This pytest function should confirm that there are 3 even numbers in the list `[1, 2, 3, 4, 6]`.

Bug type: Logical
-----------------
pytest only discovers functions whose names start with `test_`; `check_count_evens` will never be collected or run. Renaming it to `test_count_evens` lets pytest find it.

The program below is the corrected version.
"""


def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])

def test_count_evens():
    assert count_evens([1, 2, 3, 4, 6]) == 3
