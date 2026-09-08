"""Advanced problem 35 — Heart Rate Training Zones (imperative)

Subject: Biology. Style: imperative.

Problem
-------
Given a person's age, print their five heart-rate training zones (50-60%, 60-70%, …, 90-100% of max HR), where `max_HR = 220 - age`.

Concepts taught
---------------
`while` loop with two updating counters (`lower`, `zone`), formatted output.

Expected output
---------------
Max HR: 204 bpm

Zone 1: 102-122 bpm (50-60%)
Zone 2: 122-142 bpm (60-70%)
Zone 3: 142-163 bpm (70-80%)
Zone 4: 163-183 bpm (80-89%)
Zone 5: 183-203 bpm (89-99%)
"""


age = 16
max_hr = 220 - age

print(f"Max HR: {max_hr} bpm\n")
zone = 1
lower = 0.5
while zone <= 5:
    upper = lower + 0.1
    lo_bpm = int(max_hr * lower)
    hi_bpm = int(max_hr * upper)
    print(f"Zone {zone}: {lo_bpm}-{hi_bpm} bpm "
          f"({int(lower * 100)}-{int(upper * 100)}%)")
    lower = upper
    zone += 1
