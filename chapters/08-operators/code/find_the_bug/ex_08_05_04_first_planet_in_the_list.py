"""Exercise 8.5.4 — First planet in the list

Chapter 8 (Operators), section 8.5: Other Operators.

Problem
-------
This program should print the first planet, `"Mercury"`.

Bug type: Logical
-----------------
List indexing starts at 0, so `planets[1]` is the second planet, "Venus". Use index `0` to get the first.

The program below is the corrected version.
"""


planets = ["Mercury", "Venus", "Earth"]
first_planet = planets[0]
print(first_planet)   # Mercury
