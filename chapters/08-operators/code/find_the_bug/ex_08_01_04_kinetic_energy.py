"""Exercise 8.1.4 — Kinetic energy

Chapter 8 (Operators), section 8.1: Arithmetic Operators.

Problem
-------
Kinetic energy is one-half times mass times speed squared. For a mass of 2 kg moving at 3 m/s this should print `9.0`.

Bug type: Logical
-----------------
The formula multiplies speed by 2 instead of squaring it, giving 6.0 rather than 9.0. Use the power operator `**` to square the speed.

The program below is the corrected version.
"""


mass = 2
speed = 3
energy = 0.5 * mass * speed ** 2
print(energy)   # 9.0
