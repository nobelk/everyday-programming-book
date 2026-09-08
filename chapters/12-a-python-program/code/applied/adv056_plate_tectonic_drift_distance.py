"""Advanced problem 56 — Plate Tectonic Drift Distance (functional)

Subject: Geology. Style: functional.

Problem
-------
Several tectonic plates drift at different rates (mm/year). Compute the distance each will have moved after 1, 10, 100, 1,000, and 10,000 years.

Concepts taught
---------------
Nested list comprehension producing structured data, underscores in numeric literals for readability.

Expected output
---------------

Pacific:
  after     1 yr →         70 mm (   0.1 m)
  after    10 yr →        700 mm (   0.7 m)
  after   100 yr →      7,000 mm (   7.0 m)
  after  1000 yr →     70,000 mm (  70.0 m)
  after 10000 yr →    700,000 mm ( 700.0 m)

North American:
  after     1 yr →         25 mm (   0.0 m)
  after    10 yr →        250 mm (   0.2 m)
  after   100 yr →      2,500 mm (   2.5 m)
  after  1000 yr →     25,000 mm (  25.0 m)
  after 10000 yr →    250,000 mm ( 250.0 m)

African:
  after     1 yr →         25 mm (   0.0 m)
  after    10 yr →        250 mm (   0.2 m)
  after   100 yr →      2,500 mm (   2.5 m)
  after  1000 yr →     25,000 mm (  25.0 m)
  after 10000 yr →    250,000 mm ( 250.0 m)

Indian:
  after     1 yr →         50 mm (   0.1 m)
  after    10 yr →        500 mm (   0.5 m)
  after   100 yr →      5,000 mm (   5.0 m)
  after  1000 yr →     50,000 mm (  50.0 m)
  after 10000 yr →    500,000 mm ( 500.0 m)
"""


plates = [("Pacific", 70), ("North American", 25),
          ("African", 25), ("Indian", 50)]
years = [1, 10, 100, 1_000, 10_000]

distances = [(name, [(yr, rate * yr) for yr in years])
             for name, rate in plates]

for name, rows in distances:
    print(f"\n{name}:")
    for yr, mm in rows:
        print(f"  after {yr:>5} yr → {mm:>10,} mm ({mm / 1000:>6.1f} m)")
