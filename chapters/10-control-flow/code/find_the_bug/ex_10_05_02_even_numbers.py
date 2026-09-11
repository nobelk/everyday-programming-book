"""Exercise 10.5.2 — Even numbers

Chapter 10 (Control Flow), section 10.5: range.

Problem
-------
This program should print the even numbers from 2 up to 10 using a step.

Bug type: Logical
-----------------
A step of 1 prints every number, not just the evens. The step should be 2.

The program below is the corrected version.
"""


for number in range(2, 11, 2):
    print(number)
