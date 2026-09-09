"""Advanced problem 6 — Thin-Lens Image Distance (functional)

Subject: Physics. Style: functional.

Problem
-------
A magnifying glass has focal length `f = 10 cm`. For object distances `d_o = 5, 8, 12, 20, 30 cm`, compute the image distance from the thin-lens equation `1/f = 1/d_o + 1/d_i`. Filter and report only those that produce a *real* image (positive `d_i`).

Concepts taught
---------------
Composition of `map` and `filter`, lambda predicate, lazy iterator pipeline.

Expected output
---------------
d_o=12 cm → d_i= 60.00 cm (real image)
d_o=20 cm → d_i= 20.00 cm (real image)
d_o=30 cm → d_i= 15.00 cm (real image)
"""


focal = 10.0
object_distances = [5, 8, 12, 20, 30]

image_distance = lambda d_o: 1.0 / (1.0 / focal - 1.0 / d_o)
results = map(lambda d_o: (d_o, image_distance(d_o)), object_distances)
real_images = filter(lambda pair: pair[1] > 0, results)

for d_o, d_i in real_images:
    print(f"d_o={d_o:>2} cm → d_i={d_i:6.2f} cm (real image)")
