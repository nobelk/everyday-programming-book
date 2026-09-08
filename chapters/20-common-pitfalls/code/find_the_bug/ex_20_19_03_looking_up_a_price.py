"""Exercise 20.19.3 — Looking up a price

Chapter 20 (Common Pitfalls), section 20.19: Using a broad except: and hiding errors.

Problem
-------
This program should read a price from a dictionary and warn only when the item is missing.

Bug type: Logical
-----------------
The bare `except:` hides all errors. A missing dictionary key raises `KeyError`, so catch exactly that.

The program below is the corrected version.
"""


prices = {"apple": 0.5, "banana": 0.3}
item = "cherry"
try:
    print("Price:", prices[item])
except KeyError:
    print("That item is not on the price list")
