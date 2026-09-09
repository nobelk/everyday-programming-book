"""Advanced problem 1 — Free-Fall Drop Time (imperative)

Subject: Physics. Style: imperative.

Problem
-------
You drop a stone from a bridge and hear it hit the water 2.5 seconds later. Ignoring air resistance, how high is the bridge above the water? Compute the height for any user-supplied fall time using `h = ½ g t²`.

Concepts taught
---------------
Variables, function definition with default arguments, conditional input validation, `for` loop over a list, formatted output.

Expected output
---------------
After 1.0s the stone has fallen 4.91 m
After 2.0s the stone has fallen 19.62 m
After 2.5s the stone has fallen 30.66 m
After 3.0s the stone has fallen 44.15 m
"""


def fall_height(time_seconds: float, gravity: float = 9.81) -> float:
    if time_seconds < 0:
        raise ValueError("Time cannot be negative.")
    height = 0.5 * gravity * time_seconds ** 2
    return height

for t in [1.0, 2.0, 2.5, 3.0]:
    print(f"After {t}s the stone has fallen {fall_height(t):.2f} m")
