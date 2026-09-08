"""Problem 58 — Heart-rate readings during exercise

Domain: Biology. Chapter 9 (Control Flow), loops.

Problem
-------
Given a list of minute-by-minute bpm readings, print the highest.

Expected output
---------------
Peak heart rate: 152 bpm
"""


readings_bpm = [72, 88, 102, 118, 131, 144, 152, 149, 140, 128]
max_bpm = readings_bpm[0]
for bpm in readings_bpm:
    if bpm > max_bpm:
        max_bpm = bpm
print(f"Peak heart rate: {max_bpm} bpm")
