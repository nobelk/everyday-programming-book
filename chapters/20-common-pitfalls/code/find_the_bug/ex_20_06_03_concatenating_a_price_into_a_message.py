"""Exercise 20.6.3 — Concatenating a price into a message

Chapter 20 (Common Pitfalls), section 20.6: Mixing strings and numbers without converting types.

Problem
-------
This program should announce the ticket price.

Bug type: Runtime
-----------------
`"...$" + price` adds a string and an int, raising `TypeError`. Wrap `price` in `str()`.

The program below is the corrected version.
"""


price = 15
message = "Ticket costs $" + str(price)
print(message)
