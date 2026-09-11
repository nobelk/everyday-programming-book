"""Exercise 10.1.5 — Ticket price by age

Chapter 10 (Control Flow), section 10.1: if, elif, else.

Problem
-------
This program should set a discounted price for children under 12 and a full price otherwise. A 10-year-old should pay 5.

Bug type: Logical
-----------------
The `print` is indented inside the `else` branch, so it only runs for the full price; the child's price is never shown. Moving `print` out to run after the `if`/`else` fixes it.

The program below is the corrected version.
"""


age = 10

if age < 12:
    price = 5
else:
    price = 12

print("Ticket price:", price)
