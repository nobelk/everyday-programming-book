"""Exercise 20.18.2 — Logging a temperature reading

Chapter 20 (Common Pitfalls), section 20.18: Forgetting to close a file.

Problem
-------
The program should append one temperature reading to a log file safely.

Bug type: Logical
-----------------
The file handle is never closed. Wrap the write in a `with` block so the file is closed safely.

The program below is the corrected version.
"""


with open("temps.txt", "a") as log:
    log.write("21.5\n")
