"""Problem 52 — Compound interest year by year

Domain: Engineering / Mathematics. Chapter 10 (Control Flow), loops.

Problem
-------
₹1000 at 8% compounded annually for 5 years.

Expected output
---------------
Year 1: 1080.00
Year 2: 1166.40
Year 3: 1259.71
Year 4: 1360.49
Year 5: 1469.33
"""


amount = 1000
rate = 0.08
for year in range(1, 6):
    amount = amount * (1 + rate)
    print(f"Year {year}: {amount:.2f}")
