"""Exercise 11.2.4 — Using the parameter

Chapter 11 (Functions), section 11.2: Parameters.

Problem
-------
This program should double the number that is passed in and print 10.

Bug type: Runtime
-----------------
The call uses `number`, a name that exists only inside the function, so Python raises a `NameError`. Pass an actual value such as 5.

The program below is the corrected version.
"""


def double(number):
    return number * 2

print(double(5))
