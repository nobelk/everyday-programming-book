"""Exercise 20.19.4 — Parsing a temperature

Chapter 20 (Common Pitfalls), section 20.19: Using a broad except: and hiding errors.

Problem
-------
The program should convert typed text to a float and warn only on bad number text.

Bug type: Logical
-----------------
A bare `except:` masks unrelated problems. `float()` raises `ValueError` on non-numeric text, so catch `ValueError`.

The program below is the corrected version.
"""


reading = "hot"
try:
    celsius = float(reading)
    print("Fahrenheit:", celsius * 9 / 5 + 32)
except ValueError:
    print("That is not a valid temperature")
