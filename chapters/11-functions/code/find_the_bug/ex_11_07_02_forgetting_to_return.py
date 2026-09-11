"""Exercise 11.7.2 — Forgetting to return

Chapter 11 (Functions), section 11.7: Implicit None Return.

Problem
-------
This program should print the doubled value 14, using the function's return value.

Bug type: Logical
-----------------
The function computes `answer` but never returns it, so it returns `None` and prints `None`. Add a `return`.

The program below is the corrected version.
"""


def double(number):
    answer = number * 2
    return answer

print(double(7))  # 14
