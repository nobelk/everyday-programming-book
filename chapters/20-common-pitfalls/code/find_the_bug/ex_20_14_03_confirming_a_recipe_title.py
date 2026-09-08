"""Exercise 20.14.3 — Confirming a recipe title

Chapter 20 (Common Pitfalls), section 20.14: Using is instead of == for value comparison.

Problem
-------
A recipe title is built from its words and should match the saved title.

Bug type: Logical
-----------------
The title built by concatenation is a separate string object, so `is` returns `False` even when the text is identical. Use `==` to compare the values.

The program below is the corrected version.
"""


saved_title = "Banana Bread"
first = "Banana"
second = "Bread"
built_title = first + " " + second
if built_title == saved_title:
    print("Recipe title matches")
else:
    print("Recipe title differs")
