"""Exercise 6.9.1 — Looking up a name

Chapter 6 (Data Structures), section 6.9: Dictionaries.

Problem
-------
A student record stores a name. The program should print "Maya".

Bug type: Runtime
-----------------
Keys are case-sensitive; `"Name"` is not in the dict, so this raises a `KeyError`. Use the actual key `"name"`.

The program below is the corrected version.
"""


student = {"name": "Maya", "grade": 10}
print(student["name"])   # Maya
