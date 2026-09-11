"""Exercise 6.9.3 — Missing key

Chapter 6 (Data Structures), section 6.9: Dictionaries.

Problem
-------
The program should safely look up a missing subject and print "not found" instead of crashing.

Bug type: Runtime
-----------------
Indexing a missing key with `[]` raises a `KeyError`. Use `.get` with a default so it returns "not found" instead.

The program below is the corrected version.
"""


student = {"name": "Maya", "grade": 10}
subject = student.get("favorite_subject", "not found")
print(subject)   # not found
