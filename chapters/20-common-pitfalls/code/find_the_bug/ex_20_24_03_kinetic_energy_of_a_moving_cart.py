"""Exercise 20.24.3 — Kinetic energy of a moving cart

Chapter 20 (Common Pitfalls), section 20.24: Writing long code without testing small pieces.

Problem
-------
This program should compute kinetic energy (one-half m v squared) for m=2, v=3 and print 9.0.

Bug type: Logical
-----------------
The speed must be squared (`speed ** 2`), but the code multiplies by 2 instead. Testing the squaring step alone would reveal this.

The program below is the corrected version.
"""


def kinetic_energy(mass, speed):
    return 0.5 * mass * speed ** 2

print("Kinetic energy:", kinetic_energy(2, 3))  # Kinetic energy: 9.0
