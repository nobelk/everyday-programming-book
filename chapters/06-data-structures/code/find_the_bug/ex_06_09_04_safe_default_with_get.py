"""Exercise 6.9.4 — Safe default with get

Chapter 6 (Data Structures), section 6.9: Dictionaries.

Problem
-------
Using `.get`, the program should print "science" when the key exists.

Bug type: Runtime
-----------------
`Subject` (capital S) is undefined, so printing it raises a `NameError`. Print the variable `subject`.

The program below is the corrected version.
"""


student = {"favorite_subject": "science"}
subject = student.get("favorite_subject", "unknown")
print(subject)   # science
