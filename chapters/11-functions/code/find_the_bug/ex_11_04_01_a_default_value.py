"""Exercise 11.4.1 — A default value

Chapter 11 (Functions), section 11.4: Default Arguments.

Problem
-------
This program should print a greeting with the default name when called with no argument.

Bug type: Logical
-----------------
`greet` without parentheses does not call the function. Add `()` so it runs with the default name.

The program below is the corrected version.
"""


def greet(name="friend"):
    print("Hello,", name)

greet()
