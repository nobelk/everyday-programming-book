"""Exercise 9.9.5 — Stub class

Chapter 9 (Control Flow), section 9.9: pass.

Problem
-------
This program defines a placeholder class and should print `Ready`.

Bug type: Runtime
-----------------
`pas` is a typo for the keyword `pass`; Python reads it as a reference to an undefined name, so executing the class body raises a `NameError`. Correct the spelling to `pass`.

The program below is the corrected version.
"""


class Sensor:
    pass

print("Ready")
