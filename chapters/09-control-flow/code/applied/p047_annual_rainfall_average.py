"""Problem 47 — Annual rainfall average

Domain: Geography. Chapter 9 (Control Flow), loops.

Problem
-------
Average 12 monthly rainfall readings.

Expected output
---------------
Average rainfall: 113.33333333333333 mm/month
"""


monthly_mm = [12, 18, 40, 80, 120, 250, 300, 280, 170, 60, 20, 10]
total = 0
for mm in monthly_mm:
    total = total + mm
average = total / len(monthly_mm)
print(f"Average rainfall: {average} mm/month")
