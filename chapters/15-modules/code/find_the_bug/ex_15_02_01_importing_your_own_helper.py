"""Exercise 15.2.1 — Importing your own helper

Chapter 15 (Modules), section 15.2: Writing Your Own Module.

Problem
-------
This two-file program should convert 100 degrees Celsius to Fahrenheit (212.0).

Bug type: Runtime
-----------------
The import line asks for `c_to_k`, but `conversions.py` only defines `c_to_f`, so the import raises `ImportError`. Import the function that actually exists.

The program below is the corrected version.
"""


# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

# file: main.py
from conversions import c_to_f

print(c_to_f(100))   # 212.0
