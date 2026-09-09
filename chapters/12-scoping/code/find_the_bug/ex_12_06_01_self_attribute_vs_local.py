"""Exercise 12.6.1 — self attribute vs local

Chapter 12 (Scoping), section 12.6: Scope with Objects and Classes.

Problem
-------
This program creates a thermometer and should print its stored temperature, 22.

Bug type: Runtime
-----------------
In `__init__`, `temperature = temperature` just reassigns the local parameter; it never stores anything on the object, so `read()` raises an `AttributeError` for the missing `self.temperature`. Assign to `self.temperature`.

The program below is the corrected version.
"""


class Thermometer:
    def __init__(self, temperature):
        self.temperature = temperature

    def read(self):
        return self.temperature

device = Thermometer(22)
print("Temp:", device.read())
