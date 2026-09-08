"""Exercise 6.3.2 — Same behavior, different types

Chapter 6 (Objects), section 6.3: Duck Typing.

Problem
-------
Any object that can `speak()` can be greeted, regardless of its class.

Bug type: Runtime
-----------------
`greet` calls `animal.speka()`, but both classes provide `speak`, not `speka`, so every call raises an `AttributeError`. Correcting the method name to `animal.speak()` lets duck typing work for any object that can `speak`.

The program below is the corrected version.
"""


class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

def greet(animal):
    print("The animal says:", animal.speak())

greet(Cat())
greet(Cow())   # The animal says: Moo
