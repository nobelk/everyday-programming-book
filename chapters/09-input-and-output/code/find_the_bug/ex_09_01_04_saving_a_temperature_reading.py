"""Exercise 9.1.4 — Saving a temperature reading

Chapter 9 (Input and Output), section 9.1: Reading Input and Printing Output.

Problem
-------
This program writes one weather reading to a file and then prints it back.

Bug type: Runtime
-----------------
The second `open` uses mode `"w"` again, which opens the file for writing (and erases it); calling `f.read()` on a write-mode file raises `io.UnsupportedOperation`. Open it in read mode `"r"` to read the contents back.

The program below is the corrected version.
"""


with open("reading.txt", "w", encoding="utf-8") as f:
    f.write("Tokyo,36.5\n")

with open("reading.txt", "r", encoding="utf-8") as f:
    contents = f.read()

print(contents)
