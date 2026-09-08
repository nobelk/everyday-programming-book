"""Exercise 5.3.3 — Both lights on

Chapter 5 (Data Structures), section 5.3: bool.

Problem
-------
A room is "ready" only if both lights are on. The program should print `False` here, since one light is off.

Bug type: Logical
-----------------
"Both" requires `and`; `or` is True when either light is on. Use `and` so the result is False here.

The program below is the corrected version.
"""


light1_on = True
light2_on = False

ready = light1_on and light2_on
print(ready)   # False
