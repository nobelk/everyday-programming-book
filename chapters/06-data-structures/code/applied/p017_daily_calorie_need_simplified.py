"""Problem 17 — Daily calorie need (simplified)

Domain: Biology. Chapter 6 (Data Structures), variables.

Problem
-------
A rough basal-rate estimate: `BMR ≈ 10·mass + 6.25·height − 5·age + 5` (male, kg-cm-years).

Expected output
---------------
BMR: 1648.75 kcal/day
"""


mass_kg = 70
height_cm = 175
age_years = 30
bmr_kcal = 10 * mass_kg + 6.25 * height_cm - 5 * age_years + 5
print(f"BMR: {bmr_kcal} kcal/day")
