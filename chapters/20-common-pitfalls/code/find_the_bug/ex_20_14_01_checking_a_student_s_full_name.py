"""Exercise 20.14.1 — Checking a student's full name

Chapter 20 (Common Pitfalls), section 20.14: Using is instead of == for value comparison.

Problem
-------
This program should announce a match when the typed name equals the enrolled name.

Bug type: Logical
-----------------
The name built with `join` is a brand-new string object, so `is` (which tests identity) returns `False` even though the text matches. Compare values with `==`.

The program below is the corrected version.
"""


enrolled_name = "Ada Lovelace"
typed_name = " ".join(["Ada", "Lovelace"])
if typed_name == enrolled_name:
    print("Name matches our records")
else:
    print("Name does not match")
