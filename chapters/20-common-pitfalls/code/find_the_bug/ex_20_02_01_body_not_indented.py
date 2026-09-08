"""Exercise 20.2.1 — Body not indented

Chapter 20 (Common Pitfalls), section 20.2: Using the wrong indentation.

Problem
-------
This program should greet a registered member.

Bug type: Syntax
----------------
The `print` after the `if` must be indented to form the block. Indenting it by four spaces fixes the `IndentationError`.

The program below is the corrected version.
"""


member = "Alex"
if member == "Alex":
    print("Welcome back")
