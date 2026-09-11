"""Exercise 18.2.2 — Speed test

Chapter 18 (Testing), section 18.2: Testing with Pytest.

Problem
-------
This pytest function should verify that traveling 100 km in 2 hours gives a speed of 50 km/h.

Bug type: Logical
-----------------
Speed is distance divided by time, but the function multiplies them, returning 200 instead of 50. Changing `*` to `/` fixes the formula.

The program below is the corrected version.
"""


def speed(distance, time):
    return distance / time

def test_speed():
    assert speed(100, 2) == 50
