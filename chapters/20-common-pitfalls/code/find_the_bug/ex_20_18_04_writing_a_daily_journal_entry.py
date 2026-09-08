"""Exercise 20.18.4 — Writing a daily journal entry

Chapter 20 (Common Pitfalls), section 20.18: Forgetting to close a file.

Problem
-------
The program should write one journal line to a file safely.

Bug type: Logical
-----------------
The file is left open. A `with` block guarantees the file is closed even if an error occurs.

The program below is the corrected version.
"""


entry = "Today I walked 10000 steps.\n"
with open("journal.txt", "w") as journal:
    journal.write(entry)
print("Entry written")
