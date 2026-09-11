"""Exercise 10.3.1 — Entry rules

Chapter 10 (Control Flow), section 10.3: Logical Operators.

Problem
-------
Entry is allowed only when a person is at least 18 *and* has an ID. With age 20 and no ID, this should print `Entry denied`.

Bug type: Logical
-----------------
`or` allows entry when *either* condition holds, but both age and ID are required. Using `and` enforces both.

The program below is the corrected version.
"""


age = 20
has_id = False

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
