"""Exercise 20.24.2 — Final price after discount

Chapter 20 (Common Pitfalls), section 20.24: Writing long code without testing small pieces.

Problem
-------
The program should subtract a 20 percent discount from a $50 item and print 40.0.

Bug type: Logical
-----------------
A percentage must be divided by 100 first; `price * 20` computes a huge discount. Divide the percent by 100 (or test the discount step alone to catch this).

The program below is the corrected version.
"""


def final_price(price, percent_off):
    discount = price * percent_off / 100
    return price - discount

print("Final price:", final_price(50, 20))  # Final price: 40.0
