"""Exercise 11.5.2 — Order independence

Chapter 11 (Functions), section 11.5: Keyword Arguments.

Problem
-------
Keyword arguments let you reorder; this should print the speed as distance over time, 20.0.

Bug type: Logical
-----------------
The keyword values are swapped: `time=100` and `distance=5` give 0.05, not 20.0. Match each keyword to the intended value.

The program below is the corrected version.
"""


def speed(distance, time):
    return distance / time

print(speed(distance=100, time=5))  # 20.0
