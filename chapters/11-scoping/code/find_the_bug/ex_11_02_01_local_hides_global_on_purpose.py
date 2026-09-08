"""Exercise 11.2.1 — local hides global, on purpose

Chapter 11 (Scoping), section 11.2: A Local Variable Can Hide a Global Variable.

Problem
-------
The global `discount` is 0.10. Inside `checkout()` a local `discount` of 0.25 should be used for one sale, but the global should stay 0.10. The program should print the local rate then the global rate.

Bug type: Logical
-----------------
The intended output uses 0.10 for the sale, but inside the function the local `discount` is set to 0.25, which shadows the global. To make both lines print 0.10, the local should not override it; assign the sale rate to match the intended 0.10.

The program below is the corrected version.
"""


discount = 0.10

def checkout():
    discount = 0.10
    print("Sale rate:", discount)

checkout()
print("Normal rate:", discount)
