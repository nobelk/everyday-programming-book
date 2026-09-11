"""Exercise 12.4.3 — global keyword spelling

Chapter 12 (Scoping), section 12.4: Using global.

Problem
-------
This program should use the `global` keyword so the function changes the module-level `temperature` to 25, and print 25.

Bug type: Syntax
----------------
The keyword is `global` (lowercase); `Global` is not a keyword, so the line fails to parse. Use the lowercase keyword.

The program below is the corrected version.
"""


temperature = 0

def set_room():
    global temperature
    temperature = 25

set_room()
print("Temperature:", temperature)
