"""Exercise 20.26.3 — Logging a single temperature

Chapter 20 (Common Pitfalls), section 20.26: Mutable default arguments.

Problem
-------
Each call should return a new log holding only the reading passed in.

Bug type: Logical
-----------------
The default `log=[]` is created once and reused across calls, so readings accumulate. Default to `None` and build a fresh list.

The program below is the corrected version.
"""


def log_reading(reading, log=None):
    if log is None:
        log = []
    log.append(reading)
    return log

print(log_reading(21.5))  # [21.5]
print(log_reading(19.0))  # [19.0]
