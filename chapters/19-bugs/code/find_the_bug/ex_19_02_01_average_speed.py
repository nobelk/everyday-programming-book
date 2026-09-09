"""Exercise 19.2.1 — Average speed

Chapter 19 (Bugs), section 19.2: Runtime Bugs.

Problem
-------
This program should print average speed as distance divided by time.

Bug type: Runtime
-----------------
Calling the function with `hours = 0` divides by zero at run time, raising `ZeroDivisionError`. Guarding against a zero time (or passing a real duration) avoids the crash.

The program below is the corrected version.
"""


def average_speed(distance, hours):
    if hours == 0:
        return "Time cannot be zero"
    return distance / hours

print(average_speed(120, 2))   # 60.0
