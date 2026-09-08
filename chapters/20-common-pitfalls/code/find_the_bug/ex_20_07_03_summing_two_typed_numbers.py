"""Exercise 20.7.3 — Summing two typed numbers

Chapter 20 (Common Pitfalls), section 20.7: Forgetting to convert input() to a number.

Problem
-------
This program should add two typed prices and print the total.

Bug type: Runtime
-----------------
`second` is left as text, so `first + second` adds an int and a string, raising `TypeError`. Convert `second` with `int()` as well.

The program below is the corrected version.
"""


first = int(input("First price: "))
second = int(input("Second price: "))
print(first + second)
