"""Exercise 11.11.5 — Checking for None

Chapter 11 (Functions), section 11.11: Mutable Default Argument Trap.

Problem
-------
The guard should run when no list is passed; both calls should print a one-item list.

Bug type: Runtime
-----------------
The default is `None`, but the guard checks `== []`, which is never true for `None`, so `days.append` raises an `AttributeError` on the first call. Check `is None`.

The program below is the corrected version.
"""


def append_day(day, days=None):
    if days is None:
        days = []
    days.append(day)
    return days

print(append_day("Mon"))  # ['Mon']
print(append_day("Tue"))  # ['Tue']
