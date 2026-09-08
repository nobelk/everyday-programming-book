"""Problem 74 — Wave speed

Domain: Physics. Chapter 10 (Functions), functions.

Problem
-------
`v = f × λ`.

Expected output
---------------
343.2
"""


def wave_speed(frequency_hz, wavelength_m):
    return frequency_hz * wavelength_m

print(wave_speed(440, 0.78))
