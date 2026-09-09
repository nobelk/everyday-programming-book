"""Exercise 6.9.5 — Adding an entry

Chapter 6 (Data Structures), section 6.9: Dictionaries.

Problem
-------
The program should add a phone number to the contact and print it.

Bug type: Runtime
-----------------
`==` compares values; it does not store anything, so the key "phone" is never added and the next line raises a `KeyError`. Use a single `=` to assign the new entry.

The program below is the corrected version.
"""


contact = {"name": "Leo"}
contact["phone"] = "555-0100"
print(contact["phone"])   # 555-0100
