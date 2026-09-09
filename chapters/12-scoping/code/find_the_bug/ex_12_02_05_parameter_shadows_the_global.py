"""Exercise 12.2.5 — parameter shadows the global

Chapter 12 (Scoping), section 12.2: A Local Variable Can Hide a Global Variable.

Problem
-------
The global `gravity` is 9.8. The function takes its own `gravity` as a parameter so a caller can test the Moon's 1.6. The program should print the weight on the Moon.

Bug type: Logical
-----------------
The parameter `gravity` shadows the global, which is exactly what lets a caller test the Moon, but the call passes 9.8 (Earth) instead of 1.6. Pass the Moon's value as the argument.

The program below is the corrected version.
"""


gravity = 9.8

def weight(mass, gravity):
    return mass * gravity

print("Moon weight:", weight(10, 1.6))
