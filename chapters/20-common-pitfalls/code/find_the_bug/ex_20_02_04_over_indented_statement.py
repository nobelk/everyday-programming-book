"""Exercise 20.2.4 — Over-indented statement

Chapter 20 (Common Pitfalls), section 20.2: Using the wrong indentation.

Problem
-------
This program should print whether water is boiling at the given temperature.

Bug type: Syntax
----------------
The second `print` is indented inconsistently relative to the `if` block, causing an `IndentationError`. Matching the block's indentation (here, dedenting it to the top level) fixes it.

The program below is the corrected version.
"""


temperature = 100
if temperature >= 100:
    print("Boiling")
print("Done checking")
