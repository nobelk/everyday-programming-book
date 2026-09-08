"""Advanced problem 31 — BMI Calculator with Categories (imperative)

Subject: Biology. Style: imperative.

Problem
-------
Compute the Body Mass Index for a list of (height_m, weight_kg) tuples and print the WHO category for each.

Concepts taught
---------------
Multi-branch `if/elif/else`, tuple unpacking in a `for` loop.

Expected output
---------------
  Alex: BMI=22.86 → normal
 Jamie: BMI=35.16 → obese
   Sam: BMI=18.52 → normal
 Riley: BMI=20.20 → normal
"""


people = [("Alex", 1.75, 70), ("Jamie", 1.60, 90),
          ("Sam", 1.80, 60), ("Riley", 1.65, 55)]

for name, h, w in people:
    bmi = w / (h * h)
    if bmi < 18.5:
        cat = "underweight"
    elif bmi < 25:
        cat = "normal"
    elif bmi < 30:
        cat = "overweight"
    else:
        cat = "obese"
    print(f"{name:>6}: BMI={bmi:5.2f} → {cat}")
