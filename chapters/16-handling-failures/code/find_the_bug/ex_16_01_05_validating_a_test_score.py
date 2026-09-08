"""Exercise 16.1.5 — Validating a test score

Chapter 16 (Handling Failures), section 16.1: Handling Bad User Input.

Problem
-------
This program should accept a score the user types only if it is a whole number, then print it.

Bug type: Logical
-----------------
The `except` block silently keeps the invalid text by assigning `score = raw`, so the program reports nonsense as a score instead of rejecting it. Validation should re-prompt or refuse bad input rather than swallow it.

The program below is the corrected version.
"""


while True:
    raw = input("Enter your test score: ")
    try:
        score = int(raw)
        break
    except ValueError:
        print("Please type a whole number.")
print("Your score is", score)
