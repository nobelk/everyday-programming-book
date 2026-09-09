"""Problem 42 — Position of a falling stone each second

Domain: Physics. Chapter 10 (Control Flow), loops.

Problem
-------
Print the distance fallen after each second for 5 seconds using `d = 0.5 g t²`.

Expected output
---------------
t = 1 s, fallen 4.9 m
t = 2 s, fallen 19.6 m
t = 3 s, fallen 44.1 m
t = 4 s, fallen 78.4 m
t = 5 s, fallen 122.5 m
"""


g = 9.8
for t in range(1, 6):
    distance_m = 0.5 * g * t * t
    print(f"t = {t} s, fallen {distance_m} m")
