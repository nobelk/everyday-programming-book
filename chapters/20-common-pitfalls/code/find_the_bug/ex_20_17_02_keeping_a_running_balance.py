"""Exercise 20.17.2 — Keeping a running balance

Chapter 20 (Common Pitfalls), section 20.17: Changing a global variable inside a function by accident.

Problem
-------
This program should subtract a withdrawal from the account balance.

Bug type: Runtime
-----------------
The function assigns to `balance`, so Python treats it as local and the read raises `UnboundLocalError`. Add `global balance`.

The program below is the corrected version.
"""


balance = 500

def withdraw(amount):
    global balance
    balance = balance - amount

withdraw(120)
print("Balance:", balance)
