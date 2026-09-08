"""Advanced problem 49 — Electrical Power Consumption (imperative)

Subject: Engineering. Style: imperative.

Problem
-------
Several appliances run different daily hours. Compute monthly (30-day) energy consumption in kWh and total cost at $0.12 / kWh.

Concepts taught
---------------
Tuple unpacking in `for`, two parallel accumulators, table formatting.

Expected output
---------------
    Fridge:  108.00 kWh  $ 12.96
        AC:  270.00 kWh  $ 32.40
        TV:   12.00 kWh  $  1.44
    Laptop:   15.60 kWh  $  1.87
 LED bulbs:    6.00 kWh  $  0.72
------------------------------------
     TOTAL:  411.60 kWh  $ 49.39
"""


appliances = [
    ("Fridge",       150, 24),
    ("AC",          1500,  6),
    ("TV",           100,  4),
    ("Laptop",        65,  8),
    ("LED bulbs",     40,  5),
]
rate = 0.12
days = 30

total_kwh = 0.0
total_cost = 0.0
for name, watts, hours in appliances:
    kwh = watts * hours * days / 1000.0
    cost = kwh * rate
    total_kwh += kwh
    total_cost += cost
    print(f"{name:>10}: {kwh:7.2f} kWh  ${cost:6.2f}")

print("-" * 36)
print(f"{'TOTAL':>10}: {total_kwh:7.2f} kWh  ${total_cost:6.2f}")
