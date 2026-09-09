"""Problem 24 — Largest of three test scores

Domain: Mathematics. Chapter 10 (Control Flow), conditionals.

Problem
-------
Print the highest of three scores.

Expected output
---------------
Highest: 85
"""


a, b, c = 72, 85, 78
if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c
print(f"Highest: {largest}")
