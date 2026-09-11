"""Exercise 11.1.4 — Indenting the body

Chapter 11 (Functions), section 11.1: Your First Function.

Problem
-------
This program defines a function with two body lines and calls it once.

Bug type: Syntax
----------------
The two body lines must share the same indentation. The second `print` is indented two spaces instead of four, so Python raises an `IndentationError`.

The program below is the corrected version.
"""


def study_plan():
    print("Read the chapter.")
    print("Solve five problems.")

study_plan()
