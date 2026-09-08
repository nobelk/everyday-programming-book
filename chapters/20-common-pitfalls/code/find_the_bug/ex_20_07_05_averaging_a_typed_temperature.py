"""Exercise 20.7.5 — Averaging a typed temperature

Chapter 20 (Common Pitfalls), section 20.7: Forgetting to convert input() to a number.

Problem
-------
This program should halve the temperature the user types.

Bug type: Runtime
-----------------
`temperature` is text, so `temperature / 2` raises `TypeError`. Convert the input to a number first (`float` allows decimals).

The program below is the corrected version.
"""


temperature = float(input("Temperature: "))
print(temperature / 2)
