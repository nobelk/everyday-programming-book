"""Exercise 16.2.4 — Looking up a grade

Chapter 16 (Handling Failures), section 16.2: Handling Different Kinds of Errors.

Problem
-------
This program looks up a student's grade in a dictionary and reports a clear message if the name is missing.

Bug type: Runtime
-----------------
Looking up a missing dictionary key raises `KeyError`, but the code catches `ValueError`, so the lookup failure is not handled and the program crashes. Catch `KeyError`.

The program below is the corrected version.
"""


grades = {"Ann": 91, "Bo": 84}
name = "Cleo"
try:
    print(name, "scored", grades[name])
except KeyError:
    print("No grade recorded for", name)
