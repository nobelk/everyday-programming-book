"""Exercise 12.6.5 — updating an instance attribute

Chapter 12 (Scoping), section 12.6: Scope with Objects and Classes.

Problem
-------
This program saves money into an account and should print the balance, 70, after one deposit.

Bug type: Logical
-----------------
`deposit` assigns to a local `balance`, which vanishes when the method returns; the object's `self.balance` is never updated, so it stays 50. Assign to `self.balance`.

The program below is the corrected version.
"""


class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

savings = Account(50)
savings.deposit(20)
print("Balance:", savings.balance)
