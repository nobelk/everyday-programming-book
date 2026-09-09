"""Exercise 17.2.1 — Splitting a bill

Chapter 17 (Handling Failures), section 17.2: Handling Different Kinds of Errors.

Problem
-------
This program divides a restaurant bill among friends and should report when there are zero friends.

Bug type: Runtime
-----------------
Dividing by zero raises `ZeroDivisionError`, but the code catches `ValueError`, so the real error escapes and the program crashes. Catch `ZeroDivisionError`.

The program below is the corrected version.
"""


bill = 60.0
friends = 0
try:
    share = bill / friends
    print("Each person pays", share)
except ZeroDivisionError:
    print("There must be at least one person.")
