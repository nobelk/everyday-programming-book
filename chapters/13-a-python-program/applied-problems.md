# Chapter 13 — A Python Program: Applied Problems

Each problem here is a whole small program rather than a single expression: it combines **variables**, **functions**, **loops**, and **conditionals** — the material of chapters 5 through 11 — which is why the set sits with the chapter on assembling a complete Python program.

Half of the problems (the even-numbered ones in each subject) are solved in a **pure functional** style — `map`, `filter`, `functools.reduce`, comprehensions, recursion, lambdas, and immutable values — following the [Python Functional HOWTO](https://docs.python.org/3/howto/functional.html). The odd-numbered ones are **imperative**. Comparing the two styles on neighbouring problems is the point.

Every entry has four parts: the problem, the solution, what the solution prints, and the Python concepts it exemplifies. The programs are also available as runnable files under [`code/applied/`](code/applied).

This set is numbered 1–70 on its own; it is separate from the 100 applied problems filed under chapters 5, 9, and 10.

**70 problems across 7 subjects.**

## Physics

### Advanced problem 1 — Free-Fall Drop Time (imperative)

You drop a stone from a bridge and hear it hit the water 2.5 seconds later. Ignoring air resistance, how high is the bridge above the water? Compute the height for any user-supplied fall time using `h = ½ g t²`.

```python
def fall_height(time_seconds: float, gravity: float = 9.81) -> float:
    if time_seconds < 0:
        raise ValueError("Time cannot be negative.")
    height = 0.5 * gravity * time_seconds ** 2
    return height

for t in [1.0, 2.0, 2.5, 3.0]:
    print(f"After {t}s the stone has fallen {fall_height(t):.2f} m")
```

**Output:**
```
After 1.0s the stone has fallen 4.91 m
After 2.0s the stone has fallen 19.62 m
After 2.5s the stone has fallen 30.66 m
After 3.0s the stone has fallen 44.15 m
```

**Concepts taught.** Variables, function definition with default arguments, conditional input validation, `for` loop over a list, formatted output.

<sub>[Runnable file](code/applied/adv001_free_fall_drop_time.py)</sub>

### Advanced problem 2 — Projectile Range Table (functional)

A water-rocket launches at 25 m/s. Compute the horizontal range for launch angles 10°, 20°, … 80°. Range is `R = v² sin(2θ) / g`.

```python
from math import sin, radians

velocity = 25.0
gravity = 9.81

ranges = list(map(
    lambda angle_deg: (angle_deg,
                       velocity ** 2 * sin(radians(2 * angle_deg)) / gravity),
    range(10, 81, 10),
))

for angle, r in ranges:
    print(f"{angle:>3}° → {r:6.2f} m")
```

**Output:**
```
 10° →  21.79 m
 20° →  40.95 m
 30° →  55.17 m
 40° →  62.74 m
 50° →  62.74 m
 60° →  55.17 m
 70° →  40.95 m
 80° →  21.79 m
```

**Concepts taught.** Pure functions (no side effects in the math), `lambda`, `map` over a numeric range, tuple packing, list comprehension alternative expressed via `map`.

<sub>[Runnable file](code/applied/adv002_projectile_range_table.py)</sub>

### Advanced problem 3 — Ohm's Law Battery Tester (imperative)

A flashlight has a 4.5 V battery and a bulb whose resistance you measured at several brightness settings: 6 Ω, 9 Ω, 12 Ω, 18 Ω. Print the current through the bulb at each setting, and warn if the current exceeds 0.5 A (the bulb's safe limit).

```python
voltage = 4.5
resistances = [6, 9, 12, 18]
safe_limit = 0.5

for r in resistances:
    current = voltage / r
    status = "OK"
    if current > safe_limit:
        status = "DANGER — bulb may burn out"
    print(f"R={r}Ω  I={current:.3f}A  {status}")
```

**Output:**
```
R=6Ω  I=0.750A  DANGER — bulb may burn out
R=9Ω  I=0.500A  OK
R=12Ω  I=0.375A  OK
R=18Ω  I=0.250A  OK
```

**Concepts taught.** Variables, looping over a list, `if` conditional with descriptive flag variable, formatted output.

<sub>[Runnable file](code/applied/adv003_ohm_s_law_battery_tester.py)</sub>

### Advanced problem 4 — Newton's Law of Cooling (functional)

A cup of tea at 90 °C is left in a 22 °C room. Newton's law says the temperature after time `t` (minutes) is `T(t) = T_room + (T_initial - T_room) · e^(-k·t)` with `k = 0.05`. Produce the temperature for the first 30 minutes (every 5 minutes).

```python
from math import exp

room, initial, k = 22.0, 90.0, 0.05

temperature = lambda t: room + (initial - room) * exp(-k * t)
times = range(0, 31, 5)
readings = [(t, temperature(t)) for t in times]

for t, T in readings:
    print(f"t={t:2d} min  T={T:5.2f} °C")
```

**Output:**
```
t= 0 min  T=90.00 °C
t= 5 min  T=74.96 °C
t=10 min  T=63.24 °C
t=15 min  T=54.12 °C
t=20 min  T=47.02 °C
t=25 min  T=41.48 °C
t=30 min  T=37.17 °C
```

**Concepts taught.** Lambda capturing constants by closure, list comprehension, immutable inputs (no variable reassignment), pure function.

<sub>[Runnable file](code/applied/adv004_newton_s_law_of_cooling.py)</sub>

### Advanced problem 5 — Wave Frequency from Period (imperative)

Your physics lab measured the time between successive ocean wave crests at a beach: 4.2 s, 5.0 s, 4.8 s, 4.5 s. For each, print the frequency (Hz) and label whether the wave is *low frequency* (< 0.25 Hz) or *high frequency*.

```python
periods = [4.2, 5.0, 4.8, 4.5]

def classify(freq: float) -> str:
    if freq < 0.25:
        return "low frequency"
    else:
        return "high frequency"

for T in periods:
    f = 1.0 / T
    print(f"T={T}s → f={f:.3f} Hz ({classify(f)})")
```

**Output:**
```
T=4.2s → f=0.238 Hz (low frequency)
T=5.0s → f=0.200 Hz (low frequency)
T=4.8s → f=0.208 Hz (low frequency)
T=4.5s → f=0.222 Hz (low frequency)
```

**Concepts taught.** Helper function returning a string, `if/else`, mapping a list with a `for` loop.

<sub>[Runnable file](code/applied/adv005_wave_frequency_from_period.py)</sub>

### Advanced problem 6 — Thin-Lens Image Distance (functional)

A magnifying glass has focal length `f = 10 cm`. For object distances `d_o = 5, 8, 12, 20, 30 cm`, compute the image distance from the thin-lens equation `1/f = 1/d_o + 1/d_i`. Filter and report only those that produce a *real* image (positive `d_i`).

```python
focal = 10.0
object_distances = [5, 8, 12, 20, 30]

image_distance = lambda d_o: 1.0 / (1.0 / focal - 1.0 / d_o)
results = map(lambda d_o: (d_o, image_distance(d_o)), object_distances)
real_images = filter(lambda pair: pair[1] > 0, results)

for d_o, d_i in real_images:
    print(f"d_o={d_o:>2} cm → d_i={d_i:6.2f} cm (real image)")
```

**Output:**
```
d_o=12 cm → d_i= 60.00 cm (real image)
d_o=20 cm → d_i= 20.00 cm (real image)
d_o=30 cm → d_i= 15.00 cm (real image)
```

**Concepts taught.** Composition of `map` and `filter`, lambda predicate, lazy iterator pipeline.

<sub>[Runnable file](code/applied/adv006_thin_lens_image_distance.py)</sub>

### Advanced problem 7 — Pendulum Period (imperative)

A grandfather-clock pendulum has lengths from 0.5 m to 2.0 m in 0.25 m steps. Print the period `T = 2π √(L/g)` and identify which length gives a period closest to 2 seconds (the classic "seconds pendulum").

```python
from math import pi, sqrt

g = 9.81
best_length = None
best_diff = float("inf")

length = 0.5
while length <= 2.0001:
    T = 2 * pi * sqrt(length / g)
    print(f"L={length:.2f} m → T={T:.3f} s")
    diff = abs(T - 2.0)
    if diff < best_diff:
        best_diff = diff
        best_length = length
    length += 0.25

print(f"\nClosest to 2s: L={best_length:.2f} m")
```

**Output:**
```
L=0.50 m → T=1.419 s
L=0.75 m → T=1.737 s
L=1.00 m → T=2.006 s
L=1.25 m → T=2.243 s
L=1.50 m → T=2.457 s
L=1.75 m → T=2.654 s
L=2.00 m → T=2.837 s

Closest to 2s: L=1.00 m
```

**Concepts taught.** `while` loop with floating-point step, accumulator pattern (track best so far), `abs`, sentinel value (`float('inf')`).

<sub>[Runnable file](code/applied/adv007_pendulum_period.py)</sub>

### Advanced problem 8 — Energy Conservation Down a Slide (functional)

A child slides down a 3 m tall slide. Assuming no friction, compute the speed at heights 3, 2.5, 2, 1.5, 1, 0.5, 0 m using `v = √(2 g (h_top - h))`.

```python
from math import sqrt
from functools import reduce

g = 9.81
h_top = 3.0
heights = [3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]

speed_at = lambda h: sqrt(2 * g * (h_top - h))
table = list(map(lambda h: (h, speed_at(h)), heights))

max_speed = reduce(lambda acc, row: max(acc, row[1]), table, 0.0)

for h, v in table:
    print(f"h={h:.1f} m → v={v:.2f} m/s")
print(f"Max speed reached: {max_speed:.2f} m/s")
```

**Output:**
```
h=3.0 m → v=0.00 m/s
h=2.5 m → v=3.13 m/s
h=2.0 m → v=4.43 m/s
h=1.5 m → v=5.42 m/s
h=1.0 m → v=6.26 m/s
h=0.5 m → v=7.00 m/s
h=0.0 m → v=7.67 m/s
Max speed reached: 7.67 m/s
```

**Concepts taught.** `reduce` for an aggregate (max), pure transformation via `map`, immutable data (`heights` never mutated).

<sub>[Runnable file](code/applied/adv008_energy_conservation_down_a_slide.py)</sub>

### Advanced problem 9 — Coulomb's Law Between Two Charges (imperative)

Two small charged balls are placed at distances 0.05 m, 0.10 m, 0.20 m, and 0.50 m apart. Each carries 2 µC. Print the electrostatic force between them and label whether the force is *strong* (> 1 N) or *weak*.

```python
k = 8.99e9
q1 = 2e-6
q2 = 2e-6
distances = [0.05, 0.10, 0.20, 0.50]

for d in distances:
    F = k * q1 * q2 / d ** 2
    if F > 1.0:
        label = "strong"
    else:
        label = "weak"
    print(f"d={d:.2f} m → F={F:.4f} N ({label})")
```

**Output:**
```
d=0.05 m → F=14.3840 N (strong)
d=0.10 m → F=3.5960 N (strong)
d=0.20 m → F=0.8990 N (weak)
d=0.50 m → F=0.1438 N (weak)
```

**Concepts taught.** Scientific notation literals, looping with conditional labelling.

<sub>[Runnable file](code/applied/adv009_coulomb_s_law_between_two_charges.py)</sub>

### Advanced problem 10 — Sound Intensity in Decibels (functional)

A sound-meter reads intensities (W/m²) of `1e-7, 1e-6, 1e-4, 1e-2, 1.0` in different rooms. Convert each to decibels using `dB = 10 log₁₀(I / I₀)` with `I₀ = 1e-12`. Then keep only those above 80 dB (the hearing-damage threshold).

```python
from math import log10

I0 = 1e-12
intensities = [1e-7, 1e-6, 1e-4, 1e-2, 1.0]

to_db = lambda I: 10 * log10(I / I0)
dangerous = list(filter(lambda dB: dB > 80, map(to_db, intensities)))

print("Dangerous levels (dB):", [f"{x:.1f}" for x in dangerous])
```

**Output:**
```
Dangerous levels (dB): ['100.0', '120.0']
```

**Concepts taught.** Composition of `map` and `filter`, lambda, list comprehension for output formatting.

<sub>[Runnable file](code/applied/adv010_sound_intensity_in_decibels.py)</sub>

## Chemistry

### Advanced problem 11 — Molecular Weight Calculator (imperative)

Compute the molar mass of water (H₂O), carbon dioxide (CO₂), and glucose (C₆H₁₂O₆) given the atomic masses H=1.008, C=12.011, O=15.999.

```python
atomic_mass = {"H": 1.008, "C": 12.011, "O": 15.999}

def molar_mass(formula: dict) -> float:
    total = 0.0
    for element, count in formula.items():
        total += atomic_mass[element] * count
    return total

molecules = {
    "H2O":      {"H": 2, "O": 1},
    "CO2":      {"C": 1, "O": 2},
    "C6H12O6":  {"C": 6, "H": 12, "O": 6},
}

for name, formula in molecules.items():
    print(f"{name:10s} → {molar_mass(formula):.3f} g/mol")
```

**Output:**
```
H2O        → 18.015 g/mol
CO2        → 44.009 g/mol
C6H12O6    → 180.156 g/mol
```

**Concepts taught.** Dictionaries, nested iteration, accumulator pattern.

<sub>[Runnable file](code/applied/adv011_molecular_weight_calculator.py)</sub>

### Advanced problem 12 — pH of a Solution (functional)

Given hydrogen-ion concentrations `[H⁺]` of common substances (stomach acid, lemon juice, milk, blood, soap, bleach), compute their pH and classify each as acidic, neutral, or basic.

```python
from math import log10

samples = [
    ("stomach acid", 1e-1),
    ("lemon juice",  1e-2),
    ("milk",         1e-7),
    ("blood",        4e-8),
    ("soap",         1e-10),
    ("bleach",       1e-13),
]

ph = lambda h_plus: -log10(h_plus)
classify = lambda p: "acidic" if p < 7 else ("basic" if p > 7 else "neutral")

results = [(name, ph(c), classify(ph(c))) for name, c in samples]

for name, p, label in results:
    print(f"{name:15s} pH={p:5.2f}  {label}")
```

**Output:**
```
stomach acid    pH= 1.00  acidic
lemon juice     pH= 2.00  acidic
milk            pH= 7.00  neutral
blood           pH= 7.40  basic
soap            pH=10.00  basic
bleach          pH=13.00  basic
```

**Concepts taught.** Lambdas, nested ternary in a lambda, list comprehension that destructures tuples.

<sub>[Runnable file](code/applied/adv012_ph_of_a_solution.py)</sub>

### Advanced problem 13 — Ideal Gas Law Solver (imperative)

Three gas cylinders sit in a chemistry lab. Given their pressure (atm), volume (L), and temperature (K), compute the moles of gas in each using `PV = nRT` (R = 0.0821 L·atm/(mol·K)). Warn if the cylinder contains more than 5 mol (over-filled).

```python
R = 0.0821
cylinders = [
    {"name": "A", "P": 2.0, "V": 10.0, "T": 300},
    {"name": "B", "P": 5.0, "V": 25.0, "T": 273},
    {"name": "C", "P": 1.0, "V": 50.0, "T": 350},
]

for c in cylinders:
    n = (c["P"] * c["V"]) / (R * c["T"])
    print(f"Cylinder {c['name']}: n={n:.3f} mol", end="")
    if n > 5:
        print("  ⚠ OVER-FILLED")
    else:
        print()
```

**Output:**
```
Cylinder A: n=0.812 mol
Cylinder B: n=5.577 mol  ⚠ OVER-FILLED
Cylinder C: n=1.740 mol
```

**Concepts taught.** List of dictionaries, formula evaluation, `if/else` with side-effect prints.

<sub>[Runnable file](code/applied/adv013_ideal_gas_law_solver.py)</sub>

### Advanced problem 14 — Reaction Stoichiometry (functional)

For the reaction `2 H₂ + O₂ → 2 H₂O`, given moles of H₂ available (`[1, 2, 4, 5, 10]`) and unlimited O₂, compute moles of water produced (it's 1 mole H₂O per 1 mole H₂).

```python
hydrogen_moles = [1, 2, 4, 5, 10]
water_produced = list(map(lambda h2: h2, hydrogen_moles))
oxygen_used    = list(map(lambda h2: h2 / 2.0, hydrogen_moles))

for h2, h2o, o2 in zip(hydrogen_moles, water_produced, oxygen_used):
    print(f"H2={h2} mol → H2O={h2o} mol, O2 used={o2} mol")
```

**Output:**
```
H2=1 mol → H2O=1 mol, O2 used=0.5 mol
H2=2 mol → H2O=2 mol, O2 used=1.0 mol
H2=4 mol → H2O=4 mol, O2 used=2.0 mol
H2=5 mol → H2O=5 mol, O2 used=2.5 mol
H2=10 mol → H2O=10 mol, O2 used=5.0 mol
```

**Concepts taught.** `map` over a list, `zip` to combine parallel sequences, identity lambda showing 1:1 mapping.

<sub>[Runnable file](code/applied/adv014_reaction_stoichiometry.py)</sub>

### Advanced problem 15 — Radioactive Half-Life Decay (imperative)

Carbon-14 has a half-life of 5730 years. Given an artifact that starts with 100 g of C-14, print the remaining mass every 5730 years for 6 half-lives, and stop early if less than 1 g remains.

```python
half_life = 5730
mass = 100.0
year = 0
half_lives_passed = 0

while half_lives_passed < 6:
    print(f"Year {year:>6}: {mass:6.2f} g")
    if mass < 1.0:
        print("Below 1 g — stopping early.")
        break
    mass = mass / 2.0
    year += half_life
    half_lives_passed += 1
```

**Output:**
```
Year      0: 100.00 g
Year   5730:  50.00 g
Year  11460:  25.00 g
Year  17190:  12.50 g
Year  22920:   6.25 g
Year  28650:   3.12 g
```

**Concepts taught.** `while` loop with multiple counters, `break`, conditional early exit.

<sub>[Runnable file](code/applied/adv015_radioactive_half_life_decay.py)</sub>

### Advanced problem 16 — Dilution (M₁V₁ = M₂V₂) (functional)

A lab has 2.0 M HCl stock. They want 100 mL each at 0.1, 0.5, and 1.0 M. Compute the volume of stock needed for each target and the water to add.

```python
stock_molarity = 2.0
target_volume = 100.0
target_molarities = [0.1, 0.5, 1.0]

stock_needed = lambda M2: (M2 * target_volume) / stock_molarity
plan = [(M2, stock_needed(M2), target_volume - stock_needed(M2))
        for M2 in target_molarities]

for M2, stock, water in plan:
    print(f"{M2} M: take {stock:5.2f} mL stock + {water:5.2f} mL water")
```

**Output:**
```
0.1 M: take  5.00 mL stock + 95.00 mL water
0.5 M: take 25.00 mL stock + 75.00 mL water
1.0 M: take 50.00 mL stock + 50.00 mL water
```

**Concepts taught.** Lambda with closure over constants, comprehension that yields a 3-tuple per element.

<sub>[Runnable file](code/applied/adv016_dilution_m_v_m_v.py)</sub>

### Advanced problem 17 — Periodic Table Lookup (imperative)

Build a mini periodic-table lookup. Given a list of element symbols, print the name and atomic number — and report any symbols that are unknown.

```python
table = {
    "H":  ("Hydrogen", 1),
    "He": ("Helium",   2),
    "Li": ("Lithium",  3),
    "C":  ("Carbon",   6),
    "N":  ("Nitrogen", 7),
    "O":  ("Oxygen",   8),
    "Fe": ("Iron",     26),
    "Au": ("Gold",     79),
}

queries = ["H", "Au", "Xx", "Fe", "C", "Mg"]

for sym in queries:
    if sym in table:
        name, num = table[sym]
        print(f"{sym}: {name} (Z={num})")
    else:
        print(f"{sym}: UNKNOWN")
```

**Output:**
```
H: Hydrogen (Z=1)
Au: Gold (Z=79)
Xx: UNKNOWN
Fe: Iron (Z=26)
C: Carbon (Z=6)
Mg: UNKNOWN
```

**Concepts taught.** Dict-of-tuples, membership test (`in`), tuple unpacking, branching.

<sub>[Runnable file](code/applied/adv017_periodic_table_lookup.py)</sub>

### Advanced problem 18 — Empirical Formula from Percent Composition (functional)

A compound is 40.0% C, 6.7% H, 53.3% O by mass. Find its empirical formula by dividing each percent by the element's atomic mass and then by the smallest result.

```python
from functools import reduce

percents = {"C": 40.0, "H": 6.7, "O": 53.3}
masses   = {"C": 12.011, "H": 1.008, "O": 15.999}

moles = {el: percents[el] / masses[el] for el in percents}
smallest = reduce(lambda acc, v: min(acc, v), moles.values(), float("inf"))
ratios = {el: round(moles[el] / smallest) for el in moles}

formula = "".join(f"{el}{n if n > 1 else ''}" for el, n in ratios.items())
print("Empirical formula:", formula)
```

**Output:**
```
Empirical formula: CH2O
```

**Concepts taught.** Dict comprehension, `reduce` to find a min, `str.join` with a generator expression.

<sub>[Runnable file](code/applied/adv018_empirical_formula_from_percent_composition.py)</sub>

### Advanced problem 19 — Acid-Base Titration End-Point (imperative)

You add 0.10 M NaOH dropwise (0.5 mL per drop) to 25 mL of 0.10 M HCl. Find how many drops are needed to reach the equivalence point (equal moles).

```python
acid_volume = 25.0       # mL
acid_M = 0.10
base_M = 0.10
drop_size = 0.5          # mL per drop

acid_moles = acid_volume * acid_M / 1000.0
drops = 0
base_volume = 0.0
base_moles = 0.0

while base_moles < acid_moles:
    base_volume += drop_size
    base_moles = base_volume * base_M / 1000.0
    drops += 1

print(f"Equivalence reached after {drops} drops "
      f"({base_volume} mL of base added)")
```

**Output:**
```
Equivalence reached after 50 drops (25.0 mL of base added)
```

**Concepts taught.** `while` loop with stopping condition derived from calculation, mutating accumulators.

<sub>[Runnable file](code/applied/adv019_acid_base_titration_end_point.py)</sub>

### Advanced problem 20 — Gas Density at STP (functional)

Compute the density (g/L) at STP for several gases using `ρ = M / 22.4` (M = molar mass, 22.4 L/mol at STP).

```python
gases = [("H2", 2.016), ("He", 4.003), ("N2", 28.014),
         ("O2", 31.998), ("CO2", 44.01)]

density = lambda molar_mass: molar_mass / 22.4
densities = list(map(lambda g: (g[0], density(g[1])), gases))
heavier_than_air = list(filter(lambda d: d[1] > density(28.97), densities))

for name, d in densities:
    print(f"{name:>4}: {d:.3f} g/L")
print("\nHeavier than air:", [n for n, _ in heavier_than_air])
```

**Output:**
```
  H2: 0.090 g/L
  He: 0.179 g/L
  N2: 1.251 g/L
  O2: 1.428 g/L
 CO2: 1.965 g/L

Heavier than air: ['O2', 'CO2']
```

**Concepts taught.** `map`/`filter` chaining, predicate using a free variable from outer scope (air's molar mass).

<sub>[Runnable file](code/applied/adv020_gas_density_at_stp.py)</sub>

## Mathematics

### Advanced problem 21 — Quadratic Equation Solver (imperative)

Solve `ax² + bx + c = 0` for any user-supplied coefficients, correctly handling all three discriminant cases.

```python
from math import sqrt

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("Not a quadratic (a = 0).")
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        r1 = (-b + sqrt(discriminant)) / (2 * a)
        r2 = (-b - sqrt(discriminant)) / (2 * a)
        return ("two real roots", r1, r2)
    elif discriminant == 0:
        return ("one real root", -b / (2 * a))
    else:
        real = -b / (2 * a)
        imag = sqrt(-discriminant) / (2 * a)
        return ("two complex roots", complex(real, imag), complex(real, -imag))

for coeffs in [(1, -3, 2), (1, 2, 1), (1, 0, 1)]:
    print(coeffs, "→", solve_quadratic(*coeffs))
```

**Output:**
```
(1, -3, 2) → ('two real roots', 2.0, 1.0)
(1, 2, 1) → ('one real root', -1.0)
(1, 0, 1) → ('two complex roots', 1j, -1j)
```

**Concepts taught.** Function returning a tuple, `if/elif/else`, argument unpacking with `*`, raising exceptions.

<sub>[Runnable file](code/applied/adv021_quadratic_equation_solver.py)</sub>

### Advanced problem 22 — Prime Number Check (functional)

Determine whether each of the numbers `[2, 7, 15, 23, 91, 97]` is prime.

```python
from math import isqrt

is_prime = lambda n: n > 1 and all(n % d != 0
                                   for d in range(2, isqrt(n) + 1))

numbers = [2, 7, 15, 23, 91, 97]
labelled = list(map(lambda n: (n, is_prime(n)), numbers))

for n, p in labelled:
    print(f"{n:>3}: {'prime' if p else 'composite'}")
```

**Output:**
```
  2: prime
  7: prime
 15: composite
 23: prime
 91: composite
 97: prime
```

**Concepts taught.** Lambda, generator expression in `all`, short-circuit boolean evaluation, `map`.

<sub>[Runnable file](code/applied/adv022_prime_number_check.py)</sub>

### Advanced problem 23 — Fibonacci Sequence (functional)

Generate the first 15 Fibonacci numbers — without mutation — using recursion plus memoization.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

sequence = [fib(i) for i in range(15)]
print(sequence)
```

**Output:**
```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

**Concepts taught.** Recursion, base case, decorator-style memoization (`lru_cache`), pure function, list comprehension.

<sub>[Runnable file](code/applied/adv023_fibonacci_sequence.py)</sub>

### Advanced problem 24 — GCD and LCM (imperative)

Find the greatest common divisor and least common multiple of two numbers using Euclid's algorithm.

```python
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

for a, b in [(12, 18), (100, 75), (17, 31)]:
    print(f"gcd({a},{b}) = {gcd(a, b)}, lcm({a},{b}) = {lcm(a, b)}")
```

**Output:**
```
gcd(12,18) = 6, lcm(12,18) = 36
gcd(100,75) = 25, lcm(100,75) = 300
gcd(17,31) = 1, lcm(17,31) = 527
```

**Concepts taught.** `while` loop, multiple assignment (tuple swap), function composition.

<sub>[Runnable file](code/applied/adv024_gcd_and_lcm.py)</sub>

### Advanced problem 25 — Statistics: Mean, Median, Mode (functional)

Given test scores `[85, 92, 78, 92, 88, 76, 92, 81, 88, 90]`, compute the mean, median, and mode in a pure-functional style.

```python
from functools import reduce
from collections import Counter

scores = [85, 92, 78, 92, 88, 76, 92, 81, 88, 90]

mean = reduce(lambda acc, x: acc + x, scores, 0) / len(scores)
sorted_scores = sorted(scores)
n = len(sorted_scores)
median = (sorted_scores[n // 2] if n % 2 == 1
          else (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2)
mode = Counter(scores).most_common(1)[0][0]

print(f"Mean   = {mean}")
print(f"Median = {median}")
print(f"Mode   = {mode}")
```

**Output:**
```
Mean   = 86.2
Median = 88.0
Mode   = 92
```

**Concepts taught.** `reduce`, ternary expression, `sorted` (returns a new list — doesn't mutate), `Counter` as a functional helper.

<sub>[Runnable file](code/applied/adv025_statistics_mean_median_mode.py)</sub>

### Advanced problem 26 — Pythagorean Triples (imperative)

Find all Pythagorean triples `(a, b, c)` with `c ≤ 30`.

```python
triples = []
for a in range(1, 31):
    for b in range(a, 31):
        c_squared = a * a + b * b
        c = int(c_squared ** 0.5)
        if c * c == c_squared and c <= 30:
            triples.append((a, b, c))

print(f"Found {len(triples)} triples:")
for t in triples:
    print(t)
```

**Output:**
```
Found 11 triples:
(3, 4, 5)
(5, 12, 13)
(6, 8, 10)
(7, 24, 25)
(8, 15, 17)
(9, 12, 15)
(10, 24, 26)
(12, 16, 20)
(15, 20, 25)
(18, 24, 30)
(20, 21, 29)
```

**Concepts taught.** Nested `for` loops, list mutation (`append`), integer-vs-float check trick.

<sub>[Runnable file](code/applied/adv026_pythagorean_triples.py)</sub>

### Advanced problem 27 — Factorial (functional)

Compute the factorial of `n` (up to 10) without loops or mutation.

```python
from functools import reduce

factorial = lambda n: reduce(lambda acc, x: acc * x, range(1, n + 1), 1)

for n in range(11):
    print(f"{n}! = {factorial(n)}")
```

**Output:**
```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
```

**Concepts taught.** `reduce` to accumulate a product, lambda, identity element (`1`) as the initial accumulator.

<sub>[Runnable file](code/applied/adv027_factorial.py)</sub>

### Advanced problem 28 — Compound Interest Growth Table (imperative)

A bank pays 6% interest per year, compounded annually. Print the balance for the first 10 years on an initial deposit of $1,000.

```python
principal = 1000.0
rate = 0.06
years = 10

balance = principal
print(f"Year  0: ${balance:>10.2f}")
for year in range(1, years + 1):
    balance = balance * (1 + rate)
    print(f"Year {year:>2}: ${balance:>10.2f}")
```

**Output:**
```
Year  0: $   1000.00
Year  1: $   1060.00
Year  2: $   1123.60
Year  3: $   1191.02
Year  4: $   1262.48
Year  5: $   1338.23
Year  6: $   1418.52
Year  7: $   1503.63
Year  8: $   1593.85
Year  9: $   1689.48
Year 10: $   1790.85
```

**Concepts taught.** Mutating accumulator over a `for` loop, formatted numeric output with width specifiers.

<sub>[Runnable file](code/applied/adv028_compound_interest_growth_table.py)</sub>

### Advanced problem 29 — Polynomial Evaluation (Horner's Method) (functional)

Evaluate `P(x) = 2x³ - 4x² + 3x - 5` at `x = -2, -1, 0, 1, 2` using Horner's method, expressed via `reduce`.

```python
from functools import reduce

coeffs = [2, -4, 3, -5]      # highest power first
horner = lambda x: reduce(lambda acc, c: acc * x + c, coeffs, 0)

for x in [-2, -1, 0, 1, 2]:
    print(f"P({x:>2}) = {horner(x)}")
```

**Output:**
```
P(-2) = -43
P(-1) = -14
P( 0) = -5
P( 1) = -4
P( 2) = 1
```

**Concepts taught.** Horner's method as a fold, `reduce` with non-trivial combining function, lambda capturing `x`.

<sub>[Runnable file](code/applied/adv029_polynomial_evaluation_horner_s_method.py)</sub>

### Advanced problem 30 — 2×2 Matrix Multiplication (imperative)

Multiply two 2×2 matrices.

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        total = 0
        for k in range(2):
            total += A[i][k] * B[k][j]
        C[i][j] = total

for row in C:
    print(row)
```

**Output:**
```
[19, 22]
[43, 50]
```

**Concepts taught.** Triple-nested loops, list-of-lists indexing, accumulator pattern inside the innermost loop.

<sub>[Runnable file](code/applied/adv030_2_2_matrix_multiplication.py)</sub>

## Biology

### Advanced problem 31 — BMI Calculator with Categories (imperative)

Compute the Body Mass Index for a list of (height_m, weight_kg) tuples and print the WHO category for each.

```python
people = [("Alex", 1.75, 70), ("Jamie", 1.60, 90),
          ("Sam", 1.80, 60), ("Riley", 1.65, 55)]

for name, h, w in people:
    bmi = w / (h * h)
    if bmi < 18.5:
        cat = "underweight"
    elif bmi < 25:
        cat = "normal"
    elif bmi < 30:
        cat = "overweight"
    else:
        cat = "obese"
    print(f"{name:>6}: BMI={bmi:5.2f} → {cat}")
```

**Output:**
```
  Alex: BMI=22.86 → normal
 Jamie: BMI=35.16 → obese
   Sam: BMI=18.52 → normal
 Riley: BMI=20.20 → normal
```

**Concepts taught.** Multi-branch `if/elif/else`, tuple unpacking in a `for` loop.

<sub>[Runnable file](code/applied/adv031_bmi_calculator_with_categories.py)</sub>

### Advanced problem 32 — Exponential Population Growth (functional)

A bacterial colony doubles every 30 minutes. Starting with 50 cells, predict the population after 0, 30, 60, …, 300 minutes.

```python
initial = 50
doubling_min = 30

population = lambda t: initial * 2 ** (t / doubling_min)
times = range(0, 301, 30)
table = [(t, population(t)) for t in times]

for t, p in table:
    print(f"t={t:>3} min → {int(p):>10,} cells")
```

**Output:**
```
t=  0 min →         50 cells
t= 30 min →        100 cells
t= 60 min →        200 cells
t= 90 min →        400 cells
t=120 min →        800 cells
t=150 min →      1,600 cells
t=180 min →      3,200 cells
t=210 min →      6,400 cells
t=240 min →     12,800 cells
t=270 min →     25,600 cells
t=300 min →     51,200 cells
```

**Concepts taught.** Lambda, list comprehension, formatting with thousands separators (`:,`).

<sub>[Runnable file](code/applied/adv032_exponential_population_growth.py)</sub>

### Advanced problem 33 — Punnett Square (imperative)

Build a Punnett square for a cross between two heterozygous parents (Aa × Aa) and report the genotype ratio.

```python
parent1 = ["A", "a"]
parent2 = ["A", "a"]

children = []
for g1 in parent1:
    for g2 in parent2:
        # Always put dominant allele first for canonical form
        pair = "".join(sorted([g1, g2], reverse=True))
        children.append(pair)

counts = {}
for c in children:
    counts[c] = counts.get(c, 0) + 1

print("Children:", children)
print("Ratio:   ", counts)
```

**Output:**
```
Children: ['AA', 'aA', 'aA', 'aa']
Ratio:    {'AA': 1, 'aA': 2, 'aa': 1}
```

**Concepts taught.** Nested loops, sorting for normalization, dict-counter idiom with `dict.get`.

<sub>[Runnable file](code/applied/adv033_punnett_square.py)</sub>

### Advanced problem 34 — DNA Base-Pair Counter (functional)

Given a DNA strand string, count each base (A, T, G, C) and compute the GC-content percentage.

```python
from functools import reduce

strand = "AGCTTAGCGCGTAACGTTAGCC"

count = lambda base: reduce(lambda acc, b: acc + (1 if b == base else 0),
                            strand, 0)
counts = {b: count(b) for b in "ATGC"}
gc_percent = (counts["G"] + counts["C"]) / len(strand) * 100

print("Counts:    ", counts)
print(f"GC content: {gc_percent:.2f}%")
```

**Output:**
```
Counts:     {'A': 5, 'T': 5, 'G': 6, 'C': 6}
GC content: 54.55%
```

**Concepts taught.** `reduce` over a string, dict comprehension, lambda with conditional expression.

<sub>[Runnable file](code/applied/adv034_dna_base_pair_counter.py)</sub>

### Advanced problem 35 — Heart Rate Training Zones (imperative)

Given a person's age, print their five heart-rate training zones (50-60%, 60-70%, …, 90-100% of max HR), where `max_HR = 220 - age`.

```python
age = 16
max_hr = 220 - age

print(f"Max HR: {max_hr} bpm\n")
zone = 1
lower = 0.5
while zone <= 5:
    upper = lower + 0.1
    lo_bpm = int(max_hr * lower)
    hi_bpm = int(max_hr * upper)
    print(f"Zone {zone}: {lo_bpm}-{hi_bpm} bpm "
          f"({int(lower * 100)}-{int(upper * 100)}%)")
    lower = upper
    zone += 1
```

**Output:**
```
Max HR: 204 bpm

Zone 1: 102-122 bpm (50-60%)
Zone 2: 122-142 bpm (60-70%)
Zone 3: 142-163 bpm (70-80%)
Zone 4: 163-183 bpm (80-89%)
Zone 5: 183-203 bpm (89-99%)
```

**Concepts taught.** `while` loop with two updating counters (`lower`, `zone`), formatted output.

<sub>[Runnable file](code/applied/adv035_heart_rate_training_zones.py)</sub>

### Advanced problem 36 — Photosynthesis Light Response (functional)

A leaf's photosynthesis rate (µmol CO₂/m²/s) follows `P = P_max · I / (I + K)` where `P_max = 25`, `K = 200`. Compute the rate at light intensities `[50, 100, 200, 400, 800, 1600]` µmol/m²/s.

```python
P_max, K = 25, 200
intensities = [50, 100, 200, 400, 800, 1600]

rate = lambda I: P_max * I / (I + K)
results = [(I, rate(I)) for I in intensities]
saturating = list(filter(lambda x: x[1] > 0.9 * P_max, results))

for I, P in results:
    print(f"I={I:>4} → P={P:5.2f}")
print("Light-saturated points:", [I for I, _ in saturating])
```

**Output:**
```
I=  50 → P= 5.00
I= 100 → P= 8.33
I= 200 → P=12.50
I= 400 → P=16.67
I= 800 → P=20.00
I=1600 → P=22.22
Light-saturated points: []
```

**Concepts taught.** Lambda, comprehension, `filter` with predicate that references an outer constant.

<sub>[Runnable file](code/applied/adv036_photosynthesis_light_response.py)</sub>

### Advanced problem 37 — Blood-Type Compatibility (imperative)

Print whether each pair of (donor, recipient) blood types is compatible.

```python
compatibility = {
    "O-":  ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
    "O+":  ["O+", "A+", "B+", "AB+"],
    "A-":  ["A-", "A+", "AB-", "AB+"],
    "A+":  ["A+", "AB+"],
    "B-":  ["B-", "B+", "AB-", "AB+"],
    "B+":  ["B+", "AB+"],
    "AB-": ["AB-", "AB+"],
    "AB+": ["AB+"],
}

pairs = [("O-", "A+"), ("AB+", "O-"), ("B+", "AB+"), ("A-", "B-")]

for donor, recipient in pairs:
    if recipient in compatibility[donor]:
        print(f"{donor} → {recipient}: compatible")
    else:
        print(f"{donor} → {recipient}: NOT compatible")
```

**Output:**
```
O- → A+: compatible
AB+ → O-: NOT compatible
B+ → AB+: compatible
A- → B-: NOT compatible
```

**Concepts taught.** Dict-of-lists, membership check, conditional output.

<sub>[Runnable file](code/applied/adv037_blood_type_compatibility.py)</sub>

### Advanced problem 38 — Predator-Prey (Lotka-Volterra) Step (functional)

Run 10 discrete time-steps of the Lotka-Volterra equations starting with 40 prey and 9 predators, with parameters `α=0.1, β=0.02, δ=0.01, γ=0.1, dt=1`. Use a recursive (immutable) approach.

```python
def step(state, n):
    if n == 0:
        return [state]
    prey, pred = state
    new_prey = prey + (0.1 * prey - 0.02 * prey * pred)
    new_pred = pred + (0.01 * prey * pred - 0.1 * pred)
    return [state] + step((new_prey, new_pred), n - 1)

history = step((40.0, 9.0), 10)
for i, (p, q) in enumerate(history):
    print(f"t={i:>2}: prey={p:6.2f}, predators={q:5.2f}")
```

**Output:**
```
t= 0: prey= 40.00, predators= 9.00
t= 1: prey= 36.80, predators=11.70
t= 2: prey= 31.87, predators=14.84
t= 3: prey= 25.60, predators=18.08
t= 4: prey= 18.90, predators=20.90
t= 5: prey= 12.89, predators=22.76
t= 6: prey=  8.31, predators=23.42
t= 7: prey=  5.25, predators=23.02
t= 8: prey=  3.36, predators=21.93
t= 9: prey=  2.22, predators=20.47
t=10: prey=  1.53, predators=18.88
```

**Concepts taught.** Recursion building a list, immutable state (each call gets a new tuple), pure function with no global state.

<sub>[Runnable file](code/applied/adv038_predator_prey_lotka_volterra_step.py)</sub>

### Advanced problem 39 — Genetic Disease Probability (Two Carriers) (imperative)

If both parents are carriers (`Aa`) of a recessive trait, compute the probability that 0, 1, 2, or 3 of their three children show the trait (`aa`, probability 1/4 per child).

```python
from math import comb

p_affected = 0.25
n_kids = 3

print(f"Both parents are carriers (Aa). With {n_kids} children:")
for k in range(n_kids + 1):
    prob = comb(n_kids, k) * (p_affected ** k) * ((1 - p_affected) ** (n_kids - k))
    print(f"  P(exactly {k} affected) = {prob:.4f}")
```

**Output:**
```
Both parents are carriers (Aa). With 3 children:
  P(exactly 0 affected) = 0.4219
  P(exactly 1 affected) = 0.4219
  P(exactly 2 affected) = 0.1406
  P(exactly 3 affected) = 0.0156
```

**Concepts taught.** Binomial distribution, `math.comb`, looping with formatted output.

<sub>[Runnable file](code/applied/adv039_genetic_disease_probability_two_carriers.py)</sub>

### Advanced problem 40 — Calorie Burn Calculator (functional)

Given a person of 65 kg doing several activities (walking 3.5 MET, cycling 8 MET, running 9.8 MET, swimming 6 MET) for 30 minutes each, compute total calories burned. Formula: `kcal = MET × weight_kg × hours`.

```python
from functools import reduce

weight_kg = 65
duration_hr = 0.5
activities = [("walking", 3.5), ("cycling", 8.0),
              ("running", 9.8), ("swimming", 6.0)]

burn = lambda met: met * weight_kg * duration_hr
per_activity = list(map(lambda a: (a[0], burn(a[1])), activities))
total = reduce(lambda acc, x: acc + x[1], per_activity, 0.0)

for name, kcal in per_activity:
    print(f"{name:>9}: {kcal:6.1f} kcal")
print(f"{'TOTAL':>9}: {total:6.1f} kcal")
```

**Output:**
```
  walking:  113.8 kcal
  cycling:  260.0 kcal
  running:  318.5 kcal
 swimming:  195.0 kcal
    TOTAL:  887.2 kcal
```

**Concepts taught.** `map` + `reduce` pipeline, lambda capturing constants by closure.

<sub>[Runnable file](code/applied/adv040_calorie_burn_calculator.py)</sub>

## Engineering

### Advanced problem 41 — Cantilever Beam Tip Deflection (imperative)

A cantilever beam of length L, with point load P at the free end, deflects by `δ = P L³ / (3 E I)`. For a steel beam (E = 200 GPa, I = 1.0×10⁻⁶ m⁴) and L = 2 m, print deflection for loads from 1 to 10 kN.

```python
E = 200e9        # Pa
I = 1.0e-6       # m^4
L = 2.0          # m

print("Load (kN) | Deflection (mm)")
print("-" * 30)
for P_kN in range(1, 11):
    P = P_kN * 1000.0
    delta = P * L ** 3 / (3 * E * I)
    print(f"{P_kN:>9} | {delta * 1000:>14.4f}")
```

**Output:**
```
Load (kN) | Deflection (mm)
------------------------------
        1 |        13.3333
        2 |        26.6667
        3 |        40.0000
        4 |        53.3333
        5 |        66.6667
        6 |        80.0000
        7 |        93.3333
        8 |       106.6667
        9 |       120.0000
       10 |       133.3333
```

**Concepts taught.** Loop with unit conversion, table-style formatting.

<sub>[Runnable file](code/applied/adv041_cantilever_beam_tip_deflection.py)</sub>

### Advanced problem 42 — Resistors in Series and Parallel (functional)

Given resistor values `[10, 22, 47, 100]` Ω, compute the total resistance if they are wired in series, and again if wired in parallel.

```python
from functools import reduce

resistors = [10, 22, 47, 100]

series = reduce(lambda acc, r: acc + r, resistors, 0)
parallel = 1 / reduce(lambda acc, r: acc + 1.0 / r, resistors, 0.0)

print(f"Series:   {series} Ω")
print(f"Parallel: {parallel:.3f} Ω")
```

**Output:**
```
Series:   179 Ω
Parallel: 5.658 Ω
```

**Concepts taught.** Two different folds over the same list (sum vs. reciprocal-sum), lambda.

<sub>[Runnable file](code/applied/adv042_resistors_in_series_and_parallel.py)</sub>

### Advanced problem 43 — Pump Flow Rate (imperative)

A water pump fills a 5,000 L tank. Given measured flow rates [120, 95, 140, 80] L/min during four time periods of [10, 15, 20, 25] min, compute when the tank fills up (or report it didn't).

```python
flows    = [120, 95, 140, 80]
times    = [10, 15, 20, 25]
capacity = 5000

filled = 0
elapsed = 0
done = False
for f, t in zip(flows, times):
    for minute in range(1, t + 1):
        filled += f
        elapsed += 1
        if filled >= capacity:
            print(f"Tank full at minute {elapsed} (filled {filled} L).")
            done = True
            break
    if done:
        break

if not done:
    print(f"Tank only reached {filled} L of {capacity} L after "
          f"{elapsed} min.")
```

**Output:**
```
Tank full at minute 42 (filled 5005 L).
```

**Concepts taught.** Nested loops with `break`, flag variable to exit multiple loops, `zip`.

<sub>[Runnable file](code/applied/adv043_pump_flow_rate.py)</sub>

### Advanced problem 44 — Stress and Strain (functional)

A steel rod (cross-section 1×10⁻⁴ m², E = 200 GPa) is subjected to forces 5, 10, 20, 50, 100 kN. Compute stress (Pa) and strain (dimensionless) for each.

```python
A = 1e-4         # m^2
E = 200e9        # Pa
forces_kN = [5, 10, 20, 50, 100]

stress = lambda F: F * 1000 / A
strain = lambda F: stress(F) / E
table = list(map(lambda F: (F, stress(F), strain(F)), forces_kN))

for F, s, e in table:
    print(f"F={F:>3} kN  σ={s:.2e} Pa  ε={e:.4e}")
```

**Output:**
```
F=  5 kN  σ=5.00e+07 Pa  ε=2.5000e-04
F= 10 kN  σ=1.00e+08 Pa  ε=5.0000e-04
F= 20 kN  σ=2.00e+08 Pa  ε=1.0000e-03
F= 50 kN  σ=5.00e+08 Pa  ε=2.5000e-03
F=100 kN  σ=1.00e+09 Pa  ε=5.0000e-03
```

**Concepts taught.** Composing two pure functions, lambda calling another lambda, scientific-notation formatting.

<sub>[Runnable file](code/applied/adv044_stress_and_strain.py)</sub>

### Advanced problem 45 — Gear Ratio Calculator (imperative)

A bicycle has front sprockets [50, 39, 30] teeth and rear sprockets [11, 13, 17, 21, 26, 32]. For each combination, print the gear ratio and label the gear *high* (≥ 3.0), *medium* (1.5–3.0), or *low*.

```python
front = [50, 39, 30]
rear  = [11, 13, 17, 21, 26, 32]

for f in front:
    for r in rear:
        ratio = f / r
        if ratio >= 3.0:
            label = "HIGH"
        elif ratio >= 1.5:
            label = "med "
        else:
            label = "low "
        print(f"{f}T / {r}T = {ratio:5.2f}  [{label}]")
    print()
```

**Output:**
```
50T / 11T =  4.55  [HIGH]
50T / 13T =  3.85  [HIGH]
50T / 17T =  2.94  [med ]
50T / 21T =  2.38  [med ]
50T / 26T =  1.92  [med ]
50T / 32T =  1.56  [med ]

39T / 11T =  3.55  [HIGH]
39T / 13T =  3.00  [HIGH]
39T / 17T =  2.29  [med ]
39T / 21T =  1.86  [med ]
39T / 26T =  1.50  [med ]
39T / 32T =  1.22  [low ]

30T / 11T =  2.73  [med ]
30T / 13T =  2.31  [med ]
30T / 17T =  1.76  [med ]
30T / 21T =  1.43  [low ]
30T / 26T =  1.15  [low ]
30T / 32T =  0.94  [low ]
```

**Concepts taught.** Nested loops with `if/elif/else`, formatted output with literal padding for alignment.

<sub>[Runnable file](code/applied/adv045_gear_ratio_calculator.py)</sub>

### Advanced problem 46 — Heat Conduction (Fourier's Law) (functional)

Compute heat flow `Q = k · A · ΔT / L` through walls of several materials: brick (k=0.7), wood (0.13), glass (1.0), insulation (0.04). Wall area 10 m², thickness 0.1 m, ΔT = 25 °C.

```python
A, L, dT = 10, 0.1, 25
materials = [("brick", 0.7), ("wood", 0.13),
             ("glass", 1.0), ("insulation", 0.04)]

heat_flow = lambda k: k * A * dT / L
results = list(map(lambda m: (m[0], heat_flow(m[1])), materials))

for name, Q in sorted(results, key=lambda x: x[1]):
    print(f"{name:>11}: Q = {Q:7.2f} W")
```

**Output:**
```
 insulation: Q =  100.00 W
       wood: Q =  325.00 W
      brick: Q = 1750.00 W
      glass: Q = 2500.00 W
```

**Concepts taught.** `map` + `sorted` with `key=lambda`, pure function.

<sub>[Runnable file](code/applied/adv046_heat_conduction_fourier_s_law.py)</sub>

### Advanced problem 47 — Bridge Load Distribution (imperative)

A simply-supported bridge of span 20 m has loads at distances from the left support: (5 m, 10 kN), (12 m, 15 kN), (18 m, 8 kN). Compute the reactions at the left and right supports using moment balance.

```python
span = 20.0
loads = [(5.0, 10.0), (12.0, 15.0), (18.0, 8.0)]

moment_about_left = 0.0
total_load = 0.0
for distance, force in loads:
    moment_about_left += distance * force
    total_load += force

R_right = moment_about_left / span
R_left = total_load - R_right

print(f"Total load:     {total_load:.2f} kN")
print(f"Left reaction:  {R_left:.2f} kN")
print(f"Right reaction: {R_right:.2f} kN")
```

**Output:**
```
Total load:     33.00 kN
Left reaction:  14.30 kN
Right reaction: 18.70 kN
```

**Concepts taught.** Two parallel accumulators inside one loop, simple statics application.

<sub>[Runnable file](code/applied/adv047_bridge_load_distribution.py)</sub>

### Advanced problem 48 — Hydrostatic Pressure with Depth (functional)

Compute hydrostatic pressure `P = ρ g h` (gauge, Pa) at depths 0, 5, 10, 25, 50, 100 m in seawater (ρ = 1025 kg/m³). Convert each to atmospheres (1 atm ≈ 101325 Pa).

```python
rho, g = 1025, 9.81
depths = [0, 5, 10, 25, 50, 100]

pressure = lambda h: rho * g * h
to_atm = lambda Pa: Pa / 101325
table = [(h, pressure(h), to_atm(pressure(h))) for h in depths]

for h, Pa, atm in table:
    print(f"depth={h:>4} m → {Pa:>9,.0f} Pa  ({atm:5.2f} atm)")
```

**Output:**
```
depth=   0 m →         0 Pa  ( 0.00 atm)
depth=   5 m →    50,276 Pa  ( 0.50 atm)
depth=  10 m →   100,552 Pa  ( 0.99 atm)
depth=  25 m →   251,381 Pa  ( 2.48 atm)
depth=  50 m →   502,762 Pa  ( 4.96 atm)
depth= 100 m → 1,005,525 Pa  ( 9.92 atm)
```

**Concepts taught.** Function composition (one lambda calling another), comprehension, thousands-separator formatting.

<sub>[Runnable file](code/applied/adv048_hydrostatic_pressure_with_depth.py)</sub>

### Advanced problem 49 — Electrical Power Consumption (imperative)

Several appliances run different daily hours. Compute monthly (30-day) energy consumption in kWh and total cost at $0.12 / kWh.

```python
appliances = [
    ("Fridge",       150, 24),
    ("AC",          1500,  6),
    ("TV",           100,  4),
    ("Laptop",        65,  8),
    ("LED bulbs",     40,  5),
]
rate = 0.12
days = 30

total_kwh = 0.0
total_cost = 0.0
for name, watts, hours in appliances:
    kwh = watts * hours * days / 1000.0
    cost = kwh * rate
    total_kwh += kwh
    total_cost += cost
    print(f"{name:>10}: {kwh:7.2f} kWh  ${cost:6.2f}")

print("-" * 36)
print(f"{'TOTAL':>10}: {total_kwh:7.2f} kWh  ${total_cost:6.2f}")
```

**Output:**
```
    Fridge:  108.00 kWh  $ 12.96
        AC:  270.00 kWh  $ 32.40
        TV:   12.00 kWh  $  1.44
    Laptop:   15.60 kWh  $  1.87
 LED bulbs:    6.00 kWh  $  0.72
------------------------------------
     TOTAL:  411.60 kWh  $ 49.39
```

**Concepts taught.** Tuple unpacking in `for`, two parallel accumulators, table formatting.

<sub>[Runnable file](code/applied/adv049_electrical_power_consumption.py)</sub>

### Advanced problem 50 — Motor RPM from Frequency (functional)

An AC induction motor's synchronous speed is `RPM = 120 · f / poles`. For a 60 Hz supply, compute the synchronous speed for motors with 2, 4, 6, 8, and 12 poles.

```python
freq = 60
pole_counts = [2, 4, 6, 8, 12]

rpm = lambda poles: 120 * freq / poles
results = list(map(lambda p: (p, rpm(p)), pole_counts))

for p, n in results:
    print(f"{p:>2} poles → {n:>5.0f} RPM")
```

**Output:**
```
 2 poles →  3600 RPM
 4 poles →  1800 RPM
 6 poles →  1200 RPM
 8 poles →   900 RPM
12 poles →   600 RPM
```

**Concepts taught.** Lambda capturing a constant via closure, `map` over a list, formatted output.

<sub>[Runnable file](code/applied/adv050_motor_rpm_from_frequency.py)</sub>

## Geology

### Advanced problem 51 — Richter Earthquake Energy (imperative)

The energy released by an earthquake of magnitude M is `E = 10^(1.5 M + 4.8)` joules. Print the energy for several quakes and compare each to the magnitude-4 reference.

```python
quakes = [
    ("Tremor",  3.0),
    ("Light",   4.0),
    ("Moderate",5.5),
    ("Strong",  6.7),
    ("Great",   8.5),
]

reference = 10 ** (1.5 * 4.0 + 4.8)
for label, M in quakes:
    energy = 10 ** (1.5 * M + 4.8)
    multiple = energy / reference
    print(f"M={M:>3.1f} {label:>9}: E={energy:.2e} J  ({multiple:>8,.0f}× M4)")
```

**Output:**
```
M=3.0    Tremor: E=2.00e+09 J  (       0× M4)
M=4.0     Light: E=6.31e+10 J  (       1× M4)
M=5.5  Moderate: E=1.12e+13 J  (     178× M4)
M=6.7    Strong: E=7.08e+14 J  (  11,220× M4)
M=8.5     Great: E=3.55e+17 J  (5,623,413× M4)
```

**Concepts taught.** Loop with formatted output, derived comparison multiple.

<sub>[Runnable file](code/applied/adv051_richter_earthquake_energy.py)</sub>

### Advanced problem 52 — Radiometric Dating with Decay Constant (functional)

Given parent isotope counts `[1000, 800, 600, 400, 200, 100]` in different rock samples, all starting from 1000 atoms, compute each sample's age using `t = -ln(N/N₀) / λ` with λ = 1.21×10⁻⁴ /yr (C-14).

```python
from math import log

N0 = 1000
decay_const = 1.21e-4
samples = [1000, 800, 600, 400, 200, 100]

age = lambda N: 0.0 if N == N0 else -log(N / N0) / decay_const
ages = list(map(lambda N: (N, age(N)), samples))

for N, t in ages:
    print(f"N={N:>5} → age ≈ {t:>10,.0f} years")
```

**Output:**
```
N= 1000 → age ≈          0 years
N=  800 → age ≈      1,844 years
N=  600 → age ≈      4,222 years
N=  400 → age ≈      7,573 years
N=  200 → age ≈     13,301 years
N=  100 → age ≈     19,030 years
```

**Concepts taught.** Lambda with conditional expression for the trivial case, `map`, immutable inputs.

<sub>[Runnable file](code/applied/adv052_radiometric_dating_with_decay_constant.py)</sub>

### Advanced problem 53 — Mohs Hardness Comparison (imperative)

Given a list of mineral hardnesses, sort them and identify which can scratch the others (any mineral can scratch one with strictly lower hardness).

```python
minerals = [("Talc", 1), ("Gypsum", 2), ("Calcite", 3),
            ("Fluorite", 4), ("Apatite", 5), ("Quartz", 7),
            ("Topaz", 8), ("Diamond", 10)]

minerals_sorted = sorted(minerals, key=lambda m: m[1])

print("Hardness ranking (soft → hard):")
for name, h in minerals_sorted:
    print(f"  {h:>2}  {name}")

target = "Calcite"
target_h = next(h for n, h in minerals_sorted if n == target)
scratched_by_target = [n for n, h in minerals_sorted if h < target_h]
print(f"\n{target} can scratch: {scratched_by_target}")
```

**Output:**
```
Hardness ranking (soft → hard):
   1  Talc
   2  Gypsum
   3  Calcite
   4  Fluorite
   5  Apatite
   7  Quartz
   8  Topaz
  10  Diamond

Calcite can scratch: ['Talc', 'Gypsum']
```

**Concepts taught.** `sorted` with key, generator expression with `next`, list comprehension as a filter.

<sub>[Runnable file](code/applied/adv053_mohs_hardness_comparison.py)</sub>

### Advanced problem 54 — Sediment Transport Rate (Stokes) (functional)

Stokes' settling velocity for a small particle in water is `v = (2/9) · (ρ_p − ρ_f) · g · r² / μ`. Compute v for grain radii [1e-5, 5e-5, 1e-4, 5e-4, 1e-3] m, with quartz density 2650, water 1000, viscosity 1e-3 Pa·s.

```python
rho_p, rho_f, g, mu = 2650, 1000, 9.81, 1e-3
radii = [1e-5, 5e-5, 1e-4, 5e-4, 1e-3]

velocity = lambda r: (2 / 9) * (rho_p - rho_f) * g * r ** 2 / mu
table = [(r, velocity(r)) for r in radii]
fast = list(filter(lambda x: x[1] > 0.01, table))

for r, v in table:
    print(f"r={r:.0e} m → v={v:.4e} m/s")
print("Fast settlers (>1 cm/s):", [f"{r:.0e}" for r, _ in fast])
```

**Output:**
```
r=1e-05 m → v=3.5970e-04 m/s
r=5e-05 m → v=8.9925e-03 m/s
r=1e-04 m → v=3.5970e-02 m/s
r=5e-04 m → v=8.9925e-01 m/s
r=1e-03 m → v=3.5970e+00 m/s
Fast settlers (>1 cm/s): ['1e-04', '5e-04', '1e-03']
```

**Concepts taught.** `filter` with predicate, comprehension, lambda.

<sub>[Runnable file](code/applied/adv054_sediment_transport_rate_stokes.py)</sub>

### Advanced problem 55 — Volcanic Explosivity Index Ranking (imperative)

Given a dataset of historical eruptions and their VEI ratings, print them sorted by VEI descending, and report the average VEI.

```python
eruptions = [
    ("Krakatoa 1883", 6),
    ("Mt. St. Helens 1980", 5),
    ("Pinatubo 1991", 6),
    ("Tambora 1815", 7),
    ("Eyjafjallajokull 2010", 4),
    ("Toba ~74000 BCE", 8),
]

eruptions_sorted = sorted(eruptions, key=lambda e: e[1], reverse=True)

total = 0
for name, vei in eruptions_sorted:
    print(f"VEI {vei}: {name}")
    total += vei
average = total / len(eruptions_sorted)
print(f"\nAverage VEI: {average:.2f}")
```

**Output:**
```
VEI 8: Toba ~74000 BCE
VEI 7: Tambora 1815
VEI 6: Krakatoa 1883
VEI 6: Pinatubo 1991
VEI 5: Mt. St. Helens 1980
VEI 4: Eyjafjallajokull 2010

Average VEI: 6.00
```

**Concepts taught.** Sorting with key + `reverse`, accumulator, division.

<sub>[Runnable file](code/applied/adv055_volcanic_explosivity_index_ranking.py)</sub>

### Advanced problem 56 — Plate Tectonic Drift Distance (functional)

Several tectonic plates drift at different rates (mm/year). Compute the distance each will have moved after 1, 10, 100, 1,000, and 10,000 years.

```python
plates = [("Pacific", 70), ("North American", 25),
          ("African", 25), ("Indian", 50)]
years = [1, 10, 100, 1_000, 10_000]

distances = [(name, [(yr, rate * yr) for yr in years])
             for name, rate in plates]

for name, rows in distances:
    print(f"\n{name}:")
    for yr, mm in rows:
        print(f"  after {yr:>5} yr → {mm:>10,} mm ({mm / 1000:>6.1f} m)")
```

**Output:**
```

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
```

**Concepts taught.** Nested list comprehension producing structured data, underscores in numeric literals for readability.

<sub>[Runnable file](code/applied/adv056_plate_tectonic_drift_distance.py)</sub>

### Advanced problem 57 — Mineral Density and Specific Gravity (imperative)

Given mass (g) and volume (cm³) of mineral specimens, compute density and specific gravity (relative to water = 1.00 g/cm³). Flag specimens denser than 5 g/cm³ as "metallic mineral candidate".

```python
specimens = [("A", 27.5, 10.0), ("B", 84.0, 12.0),
             ("C", 17.0, 6.5),  ("D", 99.0, 9.0)]

for name, mass, vol in specimens:
    density = mass / vol
    sg = density / 1.0
    note = "  ← metallic candidate" if density > 5 else ""
    print(f"{name}: ρ={density:5.2f} g/cm³  SG={sg:.2f}{note}")
```

**Output:**
```
A: ρ= 2.75 g/cm³  SG=2.75
B: ρ= 7.00 g/cm³  SG=7.00  ← metallic candidate
C: ρ= 2.62 g/cm³  SG=2.62
D: ρ=11.00 g/cm³  SG=11.00  ← metallic candidate
```

**Concepts taught.** Loop with conditional inline string, tuple unpacking.

<sub>[Runnable file](code/applied/adv057_mineral_density_and_specific_gravity.py)</sub>

### Advanced problem 58 — Erosion Rate Over Time (functional)

A cliff erodes at varying yearly rates measured each decade: [12, 15, 14, 18, 22, 19, 25, 28, 24, 21] mm/yr. Compute the cumulative erosion at each decade end without using `for` loops with mutation.

```python
from itertools import accumulate

rates_per_decade = [12, 15, 14, 18, 22, 19, 25, 28, 24, 21]
erosion_per_decade = list(map(lambda r: r * 10, rates_per_decade))
cumulative_mm = list(accumulate(erosion_per_decade))

for decade, total in enumerate(cumulative_mm, start=1):
    print(f"Decade {decade:>2} ({decade*10:>3} yr): {total/10:.1f} cm "
          f"total erosion")
```

**Output:**
```
Decade  1 ( 10 yr): 12.0 cm total erosion
Decade  2 ( 20 yr): 27.0 cm total erosion
Decade  3 ( 30 yr): 41.0 cm total erosion
Decade  4 ( 40 yr): 59.0 cm total erosion
Decade  5 ( 50 yr): 81.0 cm total erosion
Decade  6 ( 60 yr): 100.0 cm total erosion
Decade  7 ( 70 yr): 125.0 cm total erosion
Decade  8 ( 80 yr): 153.0 cm total erosion
Decade  9 ( 90 yr): 177.0 cm total erosion
Decade 10 (100 yr): 198.0 cm total erosion
```

**Concepts taught.** `itertools.accumulate` (a fold producing each intermediate), `map`, `enumerate` with `start`.

<sub>[Runnable file](code/applied/adv058_erosion_rate_over_time.py)</sub>

### Advanced problem 59 — Soil Composition Analysis (imperative)

A soil sample is 40% sand, 35% silt, 25% clay by mass. Use the USDA soil triangle classification rules (simplified) to print whether the sample is classified loam, clay loam, etc.

```python
sand, silt, clay = 40, 35, 25
total = sand + silt + clay

if total != 100:
    print(f"WARNING: percentages sum to {total}, not 100.")

if clay >= 40:
    soil_type = "clay"
elif clay >= 27 and 20 <= sand <= 45:
    soil_type = "clay loam"
elif sand >= 70:
    soil_type = "sandy"
elif silt >= 80:
    soil_type = "silty"
else:
    soil_type = "loam"

print(f"Sand={sand}% Silt={silt}% Clay={clay}% → {soil_type}")
```

**Output:**
```
Sand=40% Silt=35% Clay=25% → loam
```

**Concepts taught.** Multi-branch `if/elif/else`, chained comparison (`20 <= sand <= 45`), input validation.

<sub>[Runnable file](code/applied/adv059_soil_composition_analysis.py)</sub>

### Advanced problem 60 — Geothermal Gradient (functional)

The temperature inside the Earth rises about 25 °C per km on average. Given a surface temperature of 15 °C, compute the temperature at depths 0, 1, 2, 5, 10, 20 km.

```python
surface_T, gradient = 15, 25
depths_km = [0, 1, 2, 5, 10, 20]

temp_at = lambda d: surface_T + gradient * d
table = list(map(lambda d: (d, temp_at(d)), depths_km))

for d, T in table:
    print(f"depth={d:>2} km → T={T:>4} °C")
```

**Output:**
```
depth= 0 km → T=  15 °C
depth= 1 km → T=  40 °C
depth= 2 km → T=  65 °C
depth= 5 km → T= 140 °C
depth=10 km → T= 265 °C
depth=20 km → T= 515 °C
```

**Concepts taught.** Lambda with closure, `map`, immutable inputs.

<sub>[Runnable file](code/applied/adv060_geothermal_gradient.py)</sub>

## Geography

### Advanced problem 61 — Haversine Distance Between Cities (imperative)

Compute the great-circle distance between cities given their latitude/longitude (degrees), using the Haversine formula. Earth radius 6371 km.

```python
from math import radians, sin, cos, asin, sqrt

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlam = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlam / 2) ** 2
    return 2 * R * asin(sqrt(a))

cities = {
    "New York":  (40.7128,  -74.0060),
    "London":    (51.5074,   -0.1278),
    "Tokyo":     (35.6895,  139.6917),
    "Sydney":    (-33.8688, 151.2093),
}

names = list(cities)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        a, b = names[i], names[j]
        d = haversine_km(*cities[a], *cities[b])
        print(f"{a:>9} ↔ {b:<9}: {d:>8.1f} km")
```

**Output:**
```
 New York ↔ London   :   5570.2 km
 New York ↔ Tokyo    :  10848.8 km
 New York ↔ Sydney   :  15988.8 km
   London ↔ Tokyo    :   9558.7 km
   London ↔ Sydney   :  16993.9 km
    Tokyo ↔ Sydney   :   7826.6 km
```

**Concepts taught.** Function with multiple parameters, nested loops with indices, argument unpacking.

<sub>[Runnable file](code/applied/adv061_haversine_distance_between_cities.py)</sub>

### Advanced problem 62 — Population Density of Countries (functional)

Compute population density (people / km²) for several countries, then list those above 300 (densely populated).

```python
countries = [
    ("Singapore",    5_900_000,    728),
    ("Bangladesh", 165_000_000, 148_460),
    ("Russia",     145_000_000, 17_098_242),
    ("India",    1_400_000_000, 3_287_263),
    ("Canada",      38_000_000, 9_984_670),
]

density = lambda c: (c[0], c[1] / c[2])
densities = list(map(density, countries))
dense = list(filter(lambda d: d[1] > 300, densities))

for name, d in densities:
    print(f"{name:>11}: {d:>10.2f} /km²")
print("\nDensely populated:", [n for n, _ in dense])
```

**Output:**
```
  Singapore:    8104.40 /km²
 Bangladesh:    1111.41 /km²
     Russia:       8.48 /km²
      India:     425.89 /km²
     Canada:       3.81 /km²

Densely populated: ['Singapore', 'Bangladesh', 'India']
```

**Concepts taught.** Numeric literals with underscores, `map` + `filter`, list-comprehension projection.

<sub>[Runnable file](code/applied/adv062_population_density_of_countries.py)</sub>

### Advanced problem 63 — Time-Zone Converter (imperative)

Given an event at 14:00 local time in New York (UTC-5), print the local time in several other cities accounting for the offset.

```python
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
```

**Output:**
```
Event at 14:00 New York time
   London: 19:00
   Berlin: 20:00
    Cairo: 21:00
   Mumbai: 00:30
    Tokyo: 04:00
   Sydney: 05:00
```

**Concepts taught.** Modulo for wrap-around, fractional offset handling, `int` truncation.

<sub>[Runnable file](code/applied/adv063_time_zone_converter.py)</sub>

### Advanced problem 64 — Map-Scale Conversion (functional)

A map is at scale 1 : 50,000. For real distances of 100, 500, 1,000, 2,500, 10,000 m, compute the corresponding map distance in cm.

```python
scale = 50_000
real_distances_m = [100, 500, 1_000, 2_500, 10_000]

map_cm = lambda real_m: real_m * 100 / scale
table = list(map(lambda d: (d, map_cm(d)), real_distances_m))

for d_real, d_map in table:
    print(f"{d_real:>6} m on ground → {d_map:>6.3f} cm on map")
```

**Output:**
```
   100 m on ground →  0.200 cm on map
   500 m on ground →  1.000 cm on map
  1000 m on ground →  2.000 cm on map
  2500 m on ground →  5.000 cm on map
 10000 m on ground → 20.000 cm on map
```

**Concepts taught.** Lambda capturing a constant, `map`, formatted output.

<sub>[Runnable file](code/applied/adv064_map_scale_conversion.py)</sub>

### Advanced problem 65 — Climate Classification (Simplified Köppen) (imperative)

Given annual average temperature (°C) and rainfall (mm), assign a simplified climate label.

```python
locations = [
    ("Cairo",    22, 25),
    ("Mumbai",   27, 2200),
    ("London",   10, 600),
    ("Moscow",    5, 700),
    ("Reykjavik", 4, 800),
    ("Singapore",27, 2500),
]

for name, T, P in locations:
    if T >= 18 and P >= 1500:
        label = "Tropical wet"
    elif T >= 18 and P < 250:
        label = "Hot desert"
    elif T < 0:
        label = "Polar"
    elif T < 10:
        label = "Cold temperate"
    elif P < 400:
        label = "Semi-arid"
    else:
        label = "Temperate"
    print(f"{name:>10}: T={T}°C P={P}mm → {label}")
```

**Output:**
```
     Cairo: T=22°C P=25mm → Hot desert
    Mumbai: T=27°C P=2200mm → Tropical wet
    London: T=10°C P=600mm → Temperate
    Moscow: T=5°C P=700mm → Cold temperate
 Reykjavik: T=4°C P=800mm → Cold temperate
 Singapore: T=27°C P=2500mm → Tropical wet
```

**Concepts taught.** Multi-branch `if/elif/else` with compound conditions using `and`.

<sub>[Runnable file](code/applied/adv065_climate_classification_simplified_k_ppen.py)</sub>

### Advanced problem 66 — Average Rainfall and Outliers (functional)

Monthly rainfall (mm) for a year is `[80, 70, 95, 110, 140, 180, 220, 210, 160, 120, 95, 85]`. Compute the annual mean and identify months whose rainfall exceeds 1.25× the mean.

```python
from functools import reduce

rainfall = [80, 70, 95, 110, 140, 180, 220, 210, 160, 120, 95, 85]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

mean = reduce(lambda acc, x: acc + x, rainfall, 0) / len(rainfall)
threshold = 1.25 * mean
wet_months = list(filter(lambda mp: mp[1] > threshold, zip(months, rainfall)))

print(f"Mean rainfall: {mean:.1f} mm")
print("Wettest months:", [m for m, _ in wet_months])
```

**Output:**
```
Mean rainfall: 130.4 mm
Wettest months: ['Jun', 'Jul', 'Aug']
```

**Concepts taught.** `reduce` for the mean, `filter` over `zip`, list-comprehension projection.

<sub>[Runnable file](code/applied/adv066_average_rainfall_and_outliers.py)</sub>

### Advanced problem 67 — Elevation Profile Along a Trail (imperative)

A hiking trail's elevations (m) at 1-km intervals are [300, 350, 410, 480, 470, 520, 600, 580, 510, 450]. Compute the total ascent and descent over the trail.

```python
elevations = [300, 350, 410, 480, 470, 520, 600, 580, 510, 450]

ascent = 0
descent = 0
for i in range(1, len(elevations)):
    diff = elevations[i] - elevations[i - 1]
    if diff > 0:
        ascent += diff
    else:
        descent -= diff   # accumulate as positive

print(f"Total ascent:  {ascent} m")
print(f"Total descent: {descent} m")
print(f"Net elevation: {elevations[-1] - elevations[0]} m")
```

**Output:**
```
Total ascent:  310 m
Total descent: 160 m
Net elevation: 150 m
```

**Concepts taught.** Loop with `range(1, n)` for pairwise differences, two parallel accumulators.

<sub>[Runnable file](code/applied/adv067_elevation_profile_along_a_trail.py)</sub>

### Advanced problem 68 — Watershed Drainage Area (functional)

A watershed is divided into sub-basins with given areas (km²) and runoff coefficients. Compute the *effective* drainage area for each and the total.

```python
from functools import reduce

basins = [("Upper",  120, 0.65), ("Middle",  90, 0.55),
          ("Lower",   60, 0.40), ("Marsh",   30, 0.20)]

effective = list(map(lambda b: (b[0], b[1] * b[2]), basins))
total_eff = reduce(lambda acc, x: acc + x[1], effective, 0.0)

for name, ea in effective:
    print(f"{name:>7}: effective area = {ea:6.2f} km²")
print(f"{'TOTAL':>7}:                  {total_eff:6.2f} km²")
```

**Output:**
```
  Upper: effective area =  78.00 km²
 Middle: effective area =  49.50 km²
  Lower: effective area =  24.00 km²
  Marsh: effective area =   6.00 km²
  TOTAL:                  157.50 km²
```

**Concepts taught.** `map` with index access in a lambda, `reduce` for a projected sum.

<sub>[Runnable file](code/applied/adv068_watershed_drainage_area.py)</sub>

### Advanced problem 69 — Decimal Degrees ↔ DMS Conversion (imperative)

Convert decimal-degree coordinates to degrees-minutes-seconds (DMS) and back.

```python
def dd_to_dms(dd: float):
    sign = -1 if dd < 0 else 1
    dd = abs(dd)
    degrees = int(dd)
    minutes_full = (dd - degrees) * 60
    minutes = int(minutes_full)
    seconds = (minutes_full - minutes) * 60
    return sign * degrees, minutes, seconds

def dms_to_dd(d: int, m: int, s: float) -> float:
    sign = -1 if d < 0 else 1
    return sign * (abs(d) + m / 60 + s / 3600)

for dd in [40.7128, -74.0060, 51.5074, -33.8688]:
    d, m, s = dd_to_dms(dd)
    dd_back = dms_to_dd(d, m, s)
    print(f"{dd:>9.4f}° → {d}° {m}' {s:5.2f}\"  (round-trip: {dd_back:.4f}°)")
```

**Output:**
```
  40.7128° → 40° 42' 46.08"  (round-trip: 40.7128°)
 -74.0060° → -74° 0' 21.60"  (round-trip: -74.0060°)
  51.5074° → 51° 30' 26.64"  (round-trip: 51.5074°)
 -33.8688° → -33° 52'  7.68"  (round-trip: -33.8688°)
```

**Concepts taught.** Two cooperating functions, sign handling with conditional expression, returning multiple values via tuple.

<sub>[Runnable file](code/applied/adv069_decimal_degrees_dms_conversion.py)</sub>

### Advanced problem 70 — Wind Chill Calculator (functional)

The wind-chill index (Environment Canada formula, Celsius) is `WC = 13.12 + 0.6215·T − 11.37·V^0.16 + 0.3965·T·V^0.16`, valid for T ≤ 10 °C and V ≥ 4.8 km/h. Compute WC for combinations of T = [0, -5, -10, -20] °C and V = [10, 20, 40] km/h.

```python
from itertools import product

temps = [0, -5, -10, -20]
winds = [10, 20, 40]

wind_chill = lambda T, V: (13.12 + 0.6215 * T - 11.37 * V ** 0.16
                           + 0.3965 * T * V ** 0.16)

table = [(T, V, wind_chill(T, V)) for T, V in product(temps, winds)]
dangerous = list(filter(lambda r: r[2] < -25, table))

for T, V, WC in table:
    print(f"T={T:>3}°C V={V:>3} km/h → WC={WC:6.2f} °C")
print("\nDangerous (WC < -25 °C):",
      [(T, V) for T, V, _ in dangerous])
```

**Output:**
```
T=  0°C V= 10 km/h → WC= -3.31 °C
T=  0°C V= 20 km/h → WC= -5.24 °C
T=  0°C V= 40 km/h → WC= -7.40 °C
T= -5°C V= 10 km/h → WC= -9.29 °C
T= -5°C V= 20 km/h → WC=-11.55 °C
T= -5°C V= 40 km/h → WC=-14.08 °C
T=-10°C V= 10 km/h → WC=-15.26 °C
T=-10°C V= 20 km/h → WC=-17.86 °C
T=-10°C V= 40 km/h → WC=-20.77 °C
T=-20°C V= 10 km/h → WC=-27.21 °C
T=-20°C V= 20 km/h → WC=-30.48 °C
T=-20°C V= 40 km/h → WC=-34.13 °C

Dangerous (WC < -25 °C): [(-20, 10), (-20, 20), (-20, 40)]
```

**Concepts taught.** `itertools.product` for Cartesian-product combinations, lambda with two parameters, `filter` with multi-field predicate.

<sub>[Runnable file](code/applied/adv070_wind_chill_calculator.py)</sub>
