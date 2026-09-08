"""Advanced problem 5 — Wave Frequency from Period (imperative)

Subject: Physics. Style: imperative.

Problem
-------
Your physics lab measured the time between successive ocean wave crests at a beach: 4.2 s, 5.0 s, 4.8 s, 4.5 s. For each, print the frequency (Hz) and label whether the wave is *low frequency* (< 0.25 Hz) or *high frequency*.

Concepts taught
---------------
Helper function returning a string, `if/else`, mapping a list with a `for` loop.

Expected output
---------------
T=4.2s → f=0.238 Hz (low frequency)
T=5.0s → f=0.200 Hz (low frequency)
T=4.8s → f=0.208 Hz (low frequency)
T=4.5s → f=0.222 Hz (low frequency)
"""


periods = [4.2, 5.0, 4.8, 4.5]

def classify(freq: float) -> str:
    if freq < 0.25:
        return "low frequency"
    else:
        return "high frequency"

for T in periods:
    f = 1.0 / T
    print(f"T={T}s → f={f:.3f} Hz ({classify(f)})")
