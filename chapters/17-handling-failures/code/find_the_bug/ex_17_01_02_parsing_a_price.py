"""Exercise 17.1.2 — Parsing a price

Chapter 17 (Handling Failures), section 17.1: Handling Bad User Input.

Problem
-------
This program should read a price like `"4.99"` and print double it, recovering from bad input.

Bug type: Runtime
-----------------
The exception name is misspelled `VlaueError`, which Python treats as an unknown name; when `float` raises the real `ValueError` it is not caught and the program crashes (and the wrong name itself raises `NameError`). Spell it `ValueError`.

The program below is the corrected version.
"""


try:
    price = float(input("Enter a price in dollars: "))
    print("Two of those cost", 2 * price)
except ValueError:
    print("That was not a valid price.")
