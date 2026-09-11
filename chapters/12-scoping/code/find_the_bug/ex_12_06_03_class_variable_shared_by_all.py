"""Exercise 12.6.3 — class variable shared by all

Chapter 12 (Scoping), section 12.6: Scope with Objects and Classes.

Problem
-------
This program gives every `Planet` the same unit and should print "km" for two planets.

Bug type: Runtime
-----------------
The class variable is named `unit`, but the last line reads `mars.units`, which does not exist, so Python raises `AttributeError`. Use the correct attribute name.

The program below is the corrected version.
"""


class Planet:
    unit = "km"

    def __init__(self, name):
        self.name = name

earth = Planet("Earth")
mars = Planet("Mars")
print(earth.unit)
print(mars.unit)
