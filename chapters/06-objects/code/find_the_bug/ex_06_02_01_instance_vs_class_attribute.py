"""Exercise 6.2.1 — Instance vs class attribute

Chapter 6 (Objects), section 6.2: Instance Data vs Class Data.

Problem
-------
Every planet shares the same gravity unit, but each has its own mass. This program should print each planet's name and the shared unit.

Bug type: Runtime
-----------------
The class attribute is named `gravity_unit`, but the last line reads `earth.unit`, which does not exist. Using `earth.gravity_unit` fixes the `AttributeError`.

The program below is the corrected version.
"""


class Planet:
    gravity_unit = "m/s^2"

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

earth = Planet("Earth", 5.97e24)
mars = Planet("Mars", 6.42e23)

print(earth.name, earth.gravity_unit)   # Earth m/s^2
print(mars.name, mars.gravity_unit)     # Mars m/s^2
print(earth.gravity_unit)               # m/s^2
