"""Exercise 10.8.5 — Skip a specific student

Chapter 10 (Control Flow), section 10.8: continue.

Problem
-------
This program should print every name except "Leo".

Bug type: Logical
-----------------
The condition skips everyone *except* Leo, so only Leo is printed—the opposite of what we want. Skip when the name *is* Leo by using `==`.

The program below is the corrected version.
"""


names = ["Ana", "Leo", "Sam"]

for name in names:
    if name == "Leo":
        continue
    print(name)
