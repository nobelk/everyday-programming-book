"""Exercise 20.19.5 — Reading a list position

Chapter 20 (Common Pitfalls), section 20.19: Using a broad except: and hiding errors.

Problem
-------
This program should print the third score and warn only when the position is out of range.

Bug type: Logical
-----------------
The broad `except:` hides real bugs. An out-of-range index raises `IndexError`, so catch exactly that.

The program below is the corrected version.
"""


scores = [88, 92]
try:
    print("Third score:", scores[2])
except IndexError:
    print("There is no score at that position")
