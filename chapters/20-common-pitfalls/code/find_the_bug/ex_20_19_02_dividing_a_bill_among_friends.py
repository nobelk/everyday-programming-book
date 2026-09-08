"""Exercise 20.19.2 — Dividing a bill among friends

Chapter 20 (Common Pitfalls), section 20.19: Using a broad except: and hiding errors.

Problem
-------
The program should split a bill and report only when the number of people is zero.

Bug type: Logical
-----------------
A broad `except:` would swallow unrelated bugs. Catch the specific `ZeroDivisionError` that division by zero raises.

The program below is the corrected version.
"""


bill = 90
people = 0
try:
    share = bill / people
    print("Each pays", share)
except ZeroDivisionError:
    print("There must be at least one person")
