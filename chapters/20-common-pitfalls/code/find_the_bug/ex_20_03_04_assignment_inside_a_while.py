"""Exercise 20.3.4 — Assignment inside a `while`

Chapter 20 (Common Pitfalls), section 20.3: Confusing assignment with equality.

Problem
-------
This program should keep doubling a sample count until it reaches at least 50.

Bug type: Syntax
----------------
A `while` condition cannot use `=`; it needs a comparison. The intended loop continues while the count is below 50, so use `<`.

The program below is the corrected version.
"""


count = 5
while count < 50:
    count = count * 2
    print(count)
