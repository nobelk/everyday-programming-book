"""Exercise 18.2.5 — Looking up a planet

Chapter 18 (Bugs), section 18.2: Runtime Bugs.

Problem
-------
This program should print the number of moons for Mars.

Bug type: Runtime
-----------------
The key `"mars"` is lowercase, but the dictionary key is `"Mars"`; dictionary lookups are case sensitive, so this raises `KeyError`. Matching the stored key returns the value.

The program below is the corrected version.
"""


moons = {"Earth": 1, "Mars": 2, "Venus": 0}
print(moons["Mars"])   # 2
