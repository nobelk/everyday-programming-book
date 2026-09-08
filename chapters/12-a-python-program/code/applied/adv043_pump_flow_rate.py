"""Advanced problem 43 — Pump Flow Rate (imperative)

Subject: Engineering. Style: imperative.

Problem
-------
A water pump fills a 5,000 L tank. Given measured flow rates [120, 95, 140, 80] L/min during four time periods of [10, 15, 20, 25] min, compute when the tank fills up (or report it didn't).

Concepts taught
---------------
Nested loops with `break`, flag variable to exit multiple loops, `zip`.

Expected output
---------------
Tank full at minute 42 (filled 5005 L).
"""


flows    = [120, 95, 140, 80]
times    = [10, 15, 20, 25]
capacity = 5000

filled = 0
elapsed = 0
done = False
for f, t in zip(flows, times):
    for minute in range(1, t + 1):
        filled += f
        elapsed += 1
        if filled >= capacity:
            print(f"Tank full at minute {elapsed} (filled {filled} L).")
            done = True
            break
    if done:
        break

if not done:
    print(f"Tank only reached {filled} L of {capacity} L after "
          f"{elapsed} min.")
