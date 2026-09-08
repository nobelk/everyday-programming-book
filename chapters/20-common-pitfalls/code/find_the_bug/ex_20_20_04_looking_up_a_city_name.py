"""Exercise 20.20.4 — Looking up a city name

Chapter 20 (Common Pitfalls), section 20.20: Comparing text without thinking about case.

Problem
-------
The program should find "Paris" in the list even if typed in lowercase.

Bug type: Logical
-----------------
The list stores `"Paris"`, so a lowercase `"paris"` is not found. Compare in a consistent case, for example by lowercasing each city.

The program below is the corrected version.
"""


cities = ["Paris", "London", "Tokyo"]
search = "paris"
if search in [city.lower() for city in cities]:
    print("City found")
else:
    print("City not found")
