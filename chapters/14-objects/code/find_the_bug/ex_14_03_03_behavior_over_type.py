"""Exercise 14.3.3 — Behavior over type

Chapter 14 (Objects), section 14.3: Duck Typing.

Problem
-------
A function should work with anything that has a `length` attribute.

Bug type: Runtime
-----------------
Both objects expose a `length` attribute, but `meters_of` reads `thing.size`, which neither class has. Reading `thing.length` fixes the `AttributeError`, and any object with a `length` works.

The program below is the corrected version.
"""


class Field:
    def __init__(self, length):
        self.length = length

class Pool:
    def __init__(self, length):
        self.length = length

def meters_of(thing):
    return thing.length

print(meters_of(Field(100)))   # 100
print(meters_of(Pool(25)))     # 25
