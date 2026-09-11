"""Exercise 10.1.1 — Grading with elif

Chapter 10 (Control Flow), section 10.1: if, elif, else.

Problem
-------
This program should print the letter grade for a score. A score of 82 should print `Grade: B`.

Bug type: Syntax
----------------
The `else` line is missing its colon, so Python cannot parse the block. Adding the colon fixes it.

The program below is the corrected version.
"""


score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Needs improvement")
