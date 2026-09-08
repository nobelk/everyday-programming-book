"""Exercise 6.2.4 — Instance overriding shared default

Chapter 6 (Objects), section 6.2: Instance Data vs Class Data.

Problem
-------
Every thermostat shares a default target, but the kitchen is set warmer for itself only. The bedroom should keep the shared default.

Bug type: Logical
-----------------
`Thermostat.target_c = 22` reassigns the shared *class* attribute, so both rooms read 22 and the bedroom does not keep the default. Assigning to the instance, `kitchen.target_c = 22`, creates an instance attribute that shadows the class default for the kitchen only, leaving the bedroom at 20.

The program below is the corrected version.
"""


class Thermostat:
    target_c = 20

    def __init__(self, room):
        self.room = room

kitchen = Thermostat("kitchen")
bedroom = Thermostat("bedroom")
kitchen.target_c = 22   # set only this instance

print(kitchen.target_c)   # 22
print(bedroom.target_c)   # 20
