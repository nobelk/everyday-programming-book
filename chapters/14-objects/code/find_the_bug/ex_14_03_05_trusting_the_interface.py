"""Exercise 14.3.5 — Trusting the interface

Chapter 14 (Objects), section 14.3: Duck Typing.

Problem
-------
Any sensor that provides a `read()` method can be sampled.

Bug type: Logical
-----------------
`sensor.read` returns the bound method instead of the reading, so the printout is a method reference, not a number. Calling `sensor.read()` returns the value from whichever sensor was passed.

The program below is the corrected version.
"""


class TempSensor:
    def read(self):
        return 21.5

class HumiditySensor:
    def read(self):
        return 48.0

def sample(sensor):
    return sensor.read()

print(sample(TempSensor()))       # 21.5
print(sample(HumiditySensor()))   # 48.0
