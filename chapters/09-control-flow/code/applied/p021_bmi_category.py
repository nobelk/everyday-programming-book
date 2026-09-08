"""Problem 21 — BMI category

Domain: Biology. Chapter 9 (Control Flow), conditionals.

Problem
-------
Classify a BMI as Underweight (<18.5), Normal (<25), Overweight (<30), or Obese (≥30).

Expected output
---------------
BMI 27.3 is Overweight
"""


bmi = 27.3
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI {bmi} is {category}")
