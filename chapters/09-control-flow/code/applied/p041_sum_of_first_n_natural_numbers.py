"""Problem 41 — Sum of first N natural numbers

Domain: Mathematics. Chapter 9 (Control Flow), loops.

Problem
-------
Add up 1 + 2 + … + 100.

Expected output
---------------
Sum: 5050
"""


total = 0
for i in range(1, 101):
    total = total + i
print(f"Sum: {total}")
