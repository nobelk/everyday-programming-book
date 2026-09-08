"""Exercise 20.19.1 — Converting a typed age

Chapter 20 (Common Pitfalls), section 20.19: Using a broad except: and hiding errors.

Problem
-------
This program should turn typed text into a number and warn only when the text is not a number.

Bug type: Logical
-----------------
The bare `except:` hides every error, including programming mistakes. Catch only `ValueError`, which is the error `int()` raises on bad text.

The program below is the corrected version.
"""


text = "12y"
try:
    age = int(text)
    print("Next year you will be", age + 1)
except ValueError:
    print("Please type a whole number")
