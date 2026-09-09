"""Exercise 10.3.3 — Comfortable room

Chapter 10 (Control Flow), section 10.3: Logical Operators.

Problem
-------
A room is comfortable when the temperature is between 20 and 25 degrees inclusive. At 30 degrees (too warm) this should print `Adjust the thermostat`.

Bug type: Logical
-----------------
With `or`, almost every temperature satisfies at least one side, so even 30 degrees prints ``Comfortable''. The range requires *both* bounds, so use `and`.

The program below is the corrected version.
"""


temp_c = 30

if temp_c >= 20 and temp_c <= 25:
    print("Comfortable")
else:
    print("Adjust the thermostat")
# expected: Adjust the thermostat
