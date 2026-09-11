"""Exercise 11.4.5 — The default is optional

Chapter 11 (Functions), section 11.4: Default Arguments.

Problem
-------
This program should print 10 by relying on the default increment.

Bug type: Runtime
-----------------
The first parameter `value` has no default, so calling `increase()` with no arguments raises a `TypeError`. Pass a value, or give `value` a default.

The program below is the corrected version.
"""


def increase(value=0, by=10):
    return value + by

print(increase())  # 10
