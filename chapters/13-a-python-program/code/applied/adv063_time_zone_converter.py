"""Advanced problem 63 — Time-Zone Converter (imperative)

Subject: Geography. Style: imperative.

Problem
-------
Given an event at 14:00 local time in New York (UTC-5), print the local time in several other cities accounting for the offset.

Concepts taught
---------------
Modulo for wrap-around, fractional offset handling, `int` truncation.

Expected output
---------------
Event at 14:00 New York time
   London: 19:00
   Berlin: 20:00
    Cairo: 21:00
   Mumbai: 00:30
    Tokyo: 04:00
   Sydney: 05:00
"""


event_hour_NY = 14
NY_offset = -5

zones = [("London", 0), ("Berlin", 1), ("Cairo", 2),
         ("Mumbai", 5.5), ("Tokyo", 9), ("Sydney", 10)]

print(f"Event at {event_hour_NY:02d}:00 New York time")
for city, offset in zones:
    diff = offset - NY_offset
    local_time = (event_hour_NY + diff) % 24
    hour = int(local_time)
    minute = int((local_time - hour) * 60)
    print(f"  {city:>7}: {hour:02d}:{minute:02d}")
