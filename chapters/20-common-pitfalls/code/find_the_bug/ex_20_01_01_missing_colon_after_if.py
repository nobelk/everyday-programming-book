"""Exercise 20.1.1 — Missing colon after `if`

Chapter 20 (Common Pitfalls), section 20.1: Forgetting the : after if, for, while, or def.

Problem
-------
This program should print `"Fever"` when a temperature is at or above 38 degrees Celsius.

Bug type: Syntax
----------------
The `if` header is missing the trailing `:`, so Python cannot tell where the condition ends and the block begins. Adding the colon fixes the parse error.

The program below is the corrected version.
"""


temperature = 39
if temperature >= 38:
    print("Fever")
