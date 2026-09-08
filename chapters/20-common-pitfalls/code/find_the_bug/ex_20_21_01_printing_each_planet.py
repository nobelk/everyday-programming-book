"""Exercise 20.21.1 — Printing each planet

Chapter 20 (Common Pitfalls), section 20.21: Using range(len(...)) when iterating over items directly is simpler.

Problem
-------
This program should print every planet name on its own line.

Bug type: Runtime
-----------------
The loop indexes with `i` but prints `planet`, which was never defined, raising `NameError`. Iterate over the items directly.

The program below is the corrected version.
"""


planets = ["Mercury", "Venus", "Earth", "Mars"]
for planet in planets:
    print(planet)
