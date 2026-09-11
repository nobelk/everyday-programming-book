"""Exercise 15.2.5 — Kelvin conversion formula

Chapter 15 (Modules), section 15.2: Writing Your Own Module.

Problem
-------
This two-file program should convert 0 degrees Celsius to Kelvin (273.15).

Bug type: Logical
-----------------
The Celsius-to-Kelvin formula adds 273.15, but the function subtracts it, giving -273.15 instead of 273.15. Change the operator to `+`.

The program below is the corrected version.
"""


# file: conversions.py
def c_to_k(celsius):
    return celsius + 273.15

# file: main.py
from conversions import c_to_k

print(c_to_k(0))   # 273.15
