"""Advanced problem 10 — Sound Intensity in Decibels (functional)

Subject: Physics. Style: functional.

Problem
-------
A sound-meter reads intensities (W/m²) of `1e-7, 1e-6, 1e-4, 1e-2, 1.0` in different rooms. Convert each to decibels using `dB = 10 log₁₀(I / I₀)` with `I₀ = 1e-12`. Then keep only those above 80 dB (the hearing-damage threshold).

Concepts taught
---------------
Composition of `map` and `filter`, lambda, list comprehension for output formatting.

Expected output
---------------
Dangerous levels (dB): ['100.0', '120.0']
"""


from math import log10

I0 = 1e-12
intensities = [1e-7, 1e-6, 1e-4, 1e-2, 1.0]

to_db = lambda I: 10 * log10(I / I0)
dangerous = list(filter(lambda dB: dB > 80, map(to_db, intensities)))

print("Dangerous levels (dB):", [f"{x:.1f}" for x in dangerous])
