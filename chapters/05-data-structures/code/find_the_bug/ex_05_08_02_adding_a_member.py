"""Exercise 5.8.2 — Adding a member

Chapter 5 (Data Structures), section 5.8: Sets.

Problem
-------
The program should add "Sydney" to the set of cities and print 4 members in total.

Bug type: Runtime
-----------------
Sets have no `append` method, so this raises an `AttributeError`. Use `add` to put an item in a set.

The program below is the corrected version.
"""


cities = {"New York", "London", "Tokyo"}
cities.add("Sydney")
print(len(cities))   # 4
