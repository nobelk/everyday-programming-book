"""Exercise 6.3.4 — Duck typing a method call

Chapter 6 (Objects), section 6.3: Duck Typing.

Problem
-------
Different timers each provide `tick()`, so one loop can advance them all.

Bug type: Logical
-----------------
`device.tick` only looks up the method; it never calls it, so `watch.seconds` stays 0. Adding parentheses — `device.tick()` — actually advances each device.

The program below is the corrected version.
"""


class Stopwatch:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds = self.seconds + 1

class Metronome:
    def __init__(self):
        self.beats = 0

    def tick(self):
        self.beats = self.beats + 1

def advance(devices):
    for device in devices:
        device.tick()

watch = Stopwatch()
advance([watch])
print(watch.seconds)   # 1
