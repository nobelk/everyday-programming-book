"""Advanced problem 38 — Predator-Prey (Lotka-Volterra) Step (functional)

Subject: Biology. Style: functional.

Problem
-------
Run 10 discrete time-steps of the Lotka-Volterra equations starting with 40 prey and 9 predators, with parameters `α=0.1, β=0.02, δ=0.01, γ=0.1, dt=1`. Use a recursive (immutable) approach.

Concepts taught
---------------
Recursion building a list, immutable state (each call gets a new tuple), pure function with no global state.

Expected output
---------------
t= 0: prey= 40.00, predators= 9.00
t= 1: prey= 36.80, predators=11.70
t= 2: prey= 31.87, predators=14.84
t= 3: prey= 25.60, predators=18.08
t= 4: prey= 18.90, predators=20.90
t= 5: prey= 12.89, predators=22.76
t= 6: prey=  8.31, predators=23.42
t= 7: prey=  5.25, predators=23.02
t= 8: prey=  3.36, predators=21.93
t= 9: prey=  2.22, predators=20.47
t=10: prey=  1.53, predators=18.88
"""


def step(state, n):
    if n == 0:
        return [state]
    prey, pred = state
    new_prey = prey + (0.1 * prey - 0.02 * prey * pred)
    new_pred = pred + (0.01 * prey * pred - 0.1 * pred)
    return [state] + step((new_prey, new_pred), n - 1)

history = step((40.0, 9.0), 10)
for i, (p, q) in enumerate(history):
    print(f"t={i:>2}: prey={p:6.2f}, predators={q:5.2f}")
