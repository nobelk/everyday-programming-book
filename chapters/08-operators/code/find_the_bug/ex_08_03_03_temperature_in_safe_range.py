"""Exercise 8.3.3 — Temperature in safe range

Chapter 8 (Operators), section 8.3: Comparison Operators.

Problem
-------
Water is liquid between 0 and 100 degrees Celsius. For 25 degrees this program should print `True`.

Bug type: Logical
-----------------
The chained comparison `0 < temp_c > 100` checks that the temperature is above both 0 and 100, which is wrong. It should be `0 < temp_c < 100` to test the range between them.

The program below is the corrected version.
"""


temp_c = 25
in_range = 0 < temp_c < 100
print(in_range)   # True
