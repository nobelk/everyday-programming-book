"""Problem 56 — Temperature gradient down a mine

Domain: Geology. Chapter 10 (Control Flow), loops.

Problem
-------
Surface is 20 °C; temperature rises 25 °C per km of depth. Print temperature every 500 m to 3 km.

Expected output
---------------
500 m → 32.5 C
1000 m → 45.0 C
1500 m → 57.5 C
2000 m → 70.0 C
2500 m → 82.5 C
3000 m → 95.0 C
"""


surface_c = 20
for depth_m in range(500, 3001, 500):
    temp_c = surface_c + 25 * (depth_m / 1000)
    print(f"{depth_m} m → {temp_c} C")
