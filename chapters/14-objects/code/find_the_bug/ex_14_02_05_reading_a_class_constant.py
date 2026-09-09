"""Exercise 14.2.5 — Reading a class constant

Chapter 14 (Objects), section 14.2: Instance Data vs Class Data.

Problem
-------
The class stores a fixed sales-tax rate shared by all carts; each cart has its own subtotal. The total should add the tax.

Bug type: Logical
-----------------
Sales tax is added by *multiplying* the subtotal by the rate, not dividing by it. The corrected line uses `self.subtotal + self.subtotal * self.tax_rate`, giving `54.0`.

The program below is the corrected version.
"""


class Cart:
    tax_rate = 0.08

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def total(self):
        return self.subtotal + self.subtotal * self.tax_rate

groceries = Cart(50.0)
print(groceries.total())   # 54.0
