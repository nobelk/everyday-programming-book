"""Exercise 10.4.3 — Overriding the default

Chapter 10 (Functions), section 10.4: Default Arguments.

Problem
-------
This program should print 200 by overriding the default step count.

Bug type: Logical
-----------------
The call meant to keep the default 100 steps but passed 200 as the override, giving `2 * 200 = 400`. To get 200 for two days, pass 100 as the per-day count (or omit it to use the default).

The program below is the corrected version.
"""


def total_steps(days, per_day=100):
    return days * per_day

print(total_steps(2, 100))  # 200
