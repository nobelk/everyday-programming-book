"""Problem 4 — Body-mass index (BMI)

Domain: Biology. Chapter 5 (Data Structures), variables.

Problem
-------
For a person 1.70 m tall weighing 65 kg, compute `BMI = mass / height²`.

Expected output
---------------
BMI: 22.49
"""


mass_kg = 65
height_m = 1.70
bmi = mass_kg / height_m ** 2
print(f"BMI: {bmi:.2f}")
