"""Exercise 12.4.4 — accumulate into a global

Chapter 12 (Scoping), section 12.4: Using global.

Problem
-------
This program should use `global` to add each deposit into the module-level `savings`, ending at 60.

Bug type: Runtime
-----------------
The final `print` reads `saving`, but the global is `savings`, so Python raises `NameError`. Use the correct name.

The program below is the corrected version.
"""


savings = 0
deposits = [10, 20, 30]

def collect():
    global savings
    for amount in deposits:
        savings = savings + amount

collect()
print("Savings:", savings)
