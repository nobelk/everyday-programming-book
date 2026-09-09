"""Exercise 10.5.1 — Counting to five

Chapter 10 (Control Flow), section 10.5: range.

Problem
-------
Using `range`, this program should print the numbers 1 through 5.

Bug type: Logical
-----------------
`range` stops before its end value, so `range(1, 5)` yields 1–4. To reach 5, use `range(1, 6)`.

The program below is the corrected version.
"""


for number in range(1, 6):
    print(number)
