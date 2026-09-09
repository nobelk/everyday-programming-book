"""Problem 15 — Simple interest on savings

Domain: Mathematics. Chapter 6 (Data Structures), variables.

Problem
-------
Compute simple interest on ₹5000 at 6% per year for 3 years using `I = P × r × t`.

Expected output
---------------
Interest earned: 900.0
"""


principal = 5000
rate = 0.06
time_years = 3
interest = principal * rate * time_years
print(f"Interest earned: {interest}")
