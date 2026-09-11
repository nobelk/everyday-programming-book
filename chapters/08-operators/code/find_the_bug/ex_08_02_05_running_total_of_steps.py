"""Exercise 8.2.5 — Running total of steps

Chapter 8 (Operators), section 8.2: Assignment Operator.

Problem
-------
This program should add today's 4{,}000 steps to yesterday's 6{,}000 and print the running total, which is `10000`.

Bug type: Logical
-----------------
The line computes `total_steps + today_steps` but throws the result away because it never assigns it back. Use `+=` so the running total is updated.

The program below is the corrected version.
"""


total_steps = 6000
today_steps = 4000
total_steps += today_steps
print(total_steps)   # 10000
