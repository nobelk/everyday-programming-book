# Chapter 11 — Functions: Applied Problems

Real-world problems drawn from physics, chemistry, mathematics, biology, engineering, geology, and geography. Every formula needs no more than arithmetic, powers, square roots, and a little trigonometry.

Each problem states the situation, gives a short Python program, and shows what that program prints so you can check your own work. The programs are also available as runnable files under [`code/applied/`](code/applied).

**40 problems.**

## Functions (problems 61–80)

### Problem 61 — Newton's second law

**Domain:** Physics

Write `force(mass, acceleration)` returning `m × a`.

```python
def force(mass_kg, acceleration_mps2):
    return mass_kg * acceleration_mps2

print(force(10, 9.8))
```

**Output:** `98.0`

<sub>[Runnable file](code/applied/p061_newton_s_second_law.py)</sub>

### Problem 62 — Celsius ↔ Fahrenheit

**Domain:** Chemistry

Two functions: `c_to_f` and `f_to_c`.

```python
def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

print(c_to_f(100))
print(f_to_c(32))
```

**Output:**
```
212.0
0.0
```

<sub>[Runnable file](code/applied/p062_celsius_fahrenheit.py)</sub>

### Problem 63 — Factorial (iterative)

**Domain:** Mathematics

Write `factorial(n)` using a loop.

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(6))
```

**Output:** `720`

<sub>[Runnable file](code/applied/p063_factorial_iterative.py)</sub>

### Problem 64 — Body-surface area (Mosteller)

**Domain:** Biology

`BSA = √(height × mass / 3600)` (height in cm, mass in kg).

```python
import math

def bsa(height_cm, mass_kg):
    return math.sqrt(height_cm * mass_kg / 3600)

print(round(bsa(170, 65), 3))
```

**Output:** `1.752`

<sub>[Runnable file](code/applied/p064_body_surface_area_mosteller.py)</sub>

### Problem 65 — Beam deflection under a point load (approx.)

**Domain:** Engineering

For a simply-supported beam with centre load: `δ = F L³ / (48 E I)`.

```python
def deflection(force_n, length_m, e_pa, inertia_m4):
    return force_n * length_m ** 3 / (48 * e_pa * inertia_m4)

print(f"{deflection(1000, 2, 2e11, 8e-6):.6f} m")
```

**Output:** `0.000104 m`

<sub>[Runnable file](code/applied/p065_beam_deflection_under_a_point_load_approx.py)</sub>

### Problem 66 — Earthquake energy from magnitude

**Domain:** Geology

`log10(E) = 1.5 M + 4.8` (energy in joules).

```python
def earthquake_energy(magnitude):
    return 10 ** (1.5 * magnitude + 4.8)

print(f"{earthquake_energy(6):.2e} J")
```

**Output:** `6.31e+13 J`

<sub>[Runnable file](code/applied/p066_earthquake_energy_from_magnitude.py)</sub>

### Problem 67 — Great-circle distance (simplified flat-earth)

**Domain:** Geography

For small distances, `d ≈ √(Δx² + Δy²)`, treating 1° ≈ 111 km.

```python
import math

def approx_distance_km(lat1, lon1, lat2, lon2):
    dx_km = (lon2 - lon1) * 111
    dy_km = (lat2 - lat1) * 111
    return math.sqrt(dx_km ** 2 + dy_km ** 2)

print(round(approx_distance_km(28.6, 77.2, 19.1, 72.9), 1))  # Delhi → Mumbai rough
```

**Output:** `1157.5`

<sub>[Runnable file](code/applied/p067_great_circle_distance_simplified_flat_earth.py)</sub>

### Problem 68 — Terminal velocity (simplified)

**Domain:** Physics

`v_t = √(2 m g / (ρ A C))`.

```python
import math

def terminal_velocity(mass_kg, air_density, area_m2, drag_coeff):
    return math.sqrt(2 * mass_kg * 9.8 / (air_density * area_m2 * drag_coeff))

print(round(terminal_velocity(70, 1.2, 0.7, 1.0), 2))
```

**Output:** `40.41`

<sub>[Runnable file](code/applied/p068_terminal_velocity_simplified.py)</sub>

### Problem 69 — Ideal-gas law — pressure

**Domain:** Chemistry

`P = n R T / V`.

```python
def pressure(n_moles, temp_k, volume_l):
    R = 0.0821  # L·atm/(mol·K)
    return n_moles * R * temp_k / volume_l

print(round(pressure(1, 298, 22.4), 3))
```

**Output:** `1.092`

<sub>[Runnable file](code/applied/p069_ideal_gas_law_pressure.py)</sub>

### Problem 70 — Sine via the math module

**Domain:** Mathematics

Return the sine of an angle given in degrees.

```python
import math

def sin_deg(angle_deg):
    return math.sin(math.radians(angle_deg))

print(round(sin_deg(30), 4))
```

**Output:** `0.5`

<sub>[Runnable file](code/applied/p070_sine_via_the_math_module.py)</sub>

### Problem 71 — Heart-rate training zone

**Domain:** Biology

Zone 2 is 60–70% of max. Return the (low, high) bpm.

```python
def zone_2(age_years):
    max_hr = 220 - age_years
    return (0.60 * max_hr, 0.70 * max_hr)

print(zone_2(15))
```

**Output:** `(123.0, 143.5)`

<sub>[Runnable file](code/applied/p071_heart_rate_training_zone.py)</sub>

### Problem 72 — Machine efficiency

**Domain:** Engineering

`η = useful / input × 100%`.

```python
def efficiency(useful_j, input_j):
    return useful_j / input_j * 100

print(f"{efficiency(400, 1000):.1f}%")
```

**Output:** `40.0%`

<sub>[Runnable file](code/applied/p072_machine_efficiency.py)</sub>

### Problem 73 — Greatest common divisor (iterative)

**Domain:** Mathematics

Use Euclid's algorithm in a loop.

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 180))
```

**Output:** `12`

<sub>[Runnable file](code/applied/p073_greatest_common_divisor_iterative.py)</sub>

### Problem 74 — Wave speed

**Domain:** Physics

`v = f × λ`.

```python
def wave_speed(frequency_hz, wavelength_m):
    return frequency_hz * wavelength_m

print(wave_speed(440, 0.78))
```

**Output:** `343.2`

<sub>[Runnable file](code/applied/p074_wave_speed.py)</sub>

### Problem 75 — Time-zone difference in hours

**Domain:** Geography

Given two UTC offsets, return the difference.

```python
def tz_difference(offset_a, offset_b):
    return offset_b - offset_a

print(tz_difference(5.5, -5))  # India → New York
```

**Output:** `-10.5`

<sub>[Runnable file](code/applied/p075_time_zone_difference_in_hours.py)</sub>

### Problem 76 — Mohs hardness — can A scratch B?

**Domain:** Geology

Return `True` if mineral A can scratch mineral B.

```python
def can_scratch(hardness_a, hardness_b):
    return hardness_a > hardness_b

print(can_scratch(7, 3))  # quartz vs calcite
```

**Output:** `True`

<sub>[Runnable file](code/applied/p076_mohs_hardness_can_a_scratch_b.py)</sub>

### Problem 77 — Least common multiple

**Domain:** Mathematics

Build `lcm` on top of `gcd`.

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(12, 18))
```

**Output:** `36`

<sub>[Runnable file](code/applied/p077_least_common_multiple.py)</sub>

### Problem 78 — Oxygen consumption (METs)

**Domain:** Biology

VO2 ≈ METs × 3.5 mL/kg/min. Convert to litres/min for a person of given mass.

```python
def vo2_lpm(mets, mass_kg):
    return mets * 3.5 * mass_kg / 1000

print(round(vo2_lpm(8, 70), 3))
```

**Output:** `1.96`

<sub>[Runnable file](code/applied/p078_oxygen_consumption_mets.py)</sub>

### Problem 79 — Horsepower to watts

**Domain:** Engineering

1 hp ≈ 745.7 W.

```python
def hp_to_w(hp):
    return hp * 745.7

print(hp_to_w(2))
```

**Output:** `1491.4`

<sub>[Runnable file](code/applied/p079_horsepower_to_watts.py)</sub>

### Problem 80 — Molarity of a solution

**Domain:** Chemistry

`M = moles / litres`.

```python
def molarity(moles, volume_l):
    return moles / volume_l

print(molarity(0.5, 2.0))
```

**Output:** `0.25`

<sub>[Runnable file](code/applied/p080_molarity_of_a_solution.py)</sub>

## Recursion (problems 81–100)

### Problem 81 — Factorial (recursive)

**Domain:** Mathematics

Same as Problem 63, but recursive.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

**Output:** `120`

<sub>[Runnable file](code/applied/p081_factorial_recursive.py)</sub>

### Problem 82 — Fibonacci number

**Domain:** Mathematics

Rabbit-population classic: `F(n) = F(n−1) + F(n−2)`.

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
```

**Output:** `55`

<sub>[Runnable file](code/applied/p082_fibonacci_number.py)</sub>

### Problem 83 — Sum of digits

**Domain:** Mathematics

Add the digits of 12 345 by peeling off the last one.

```python
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(digit_sum(12345))
```

**Output:** `15`

<sub>[Runnable file](code/applied/p083_sum_of_digits.py)</sub>

### Problem 84 — Power function

**Domain:** Mathematics

Compute `x^n` for a non-negative integer `n`.

```python
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 10))
```

**Output:** `1024`

<sub>[Runnable file](code/applied/p084_power_function.py)</sub>

### Problem 85 — Height of a bouncing ball

**Domain:** Physics

Each bounce keeps 70% of the previous height. Peak height after `n` bounces?

```python
def bounce_height(initial_m, n):
    if n == 0:
        return initial_m
    return 0.7 * bounce_height(initial_m, n - 1)

print(round(bounce_height(10, 5), 3))
```

**Output:** `1.681`

<sub>[Runnable file](code/applied/p085_height_of_a_bouncing_ball.py)</sub>

### Problem 86 — Remaining radioactive atoms

**Domain:** Chemistry

Amount left after `n` half-lives.

```python
def remaining(initial, n):
    if n == 0:
        return initial
    return remaining(initial, n - 1) / 2

print(remaining(1000, 4))
```

**Output:** `62.5`

<sub>[Runnable file](code/applied/p086_remaining_radioactive_atoms.py)</sub>

### Problem 87 — Shrinking cell population

**Domain:** Biology

A dying culture loses 10% of cells each hour. Count after `h` hours.

```python
def cells_after(initial, h):
    if h == 0:
        return initial
    return 0.9 * cells_after(initial, h - 1)

print(round(cells_after(1000, 6), 1))
```

**Output:** `531.4`

<sub>[Runnable file](code/applied/p087_shrinking_cell_population.py)</sub>

### Problem 88 — Age of a rock stack layer by layer

**Domain:** Geology

Each sedimentary layer is `years_per_layer` older than the one above. Age of layer `n`.

```python
def layer_age(n, years_per_layer):
    if n == 0:
        return 0
    return years_per_layer + layer_age(n - 1, years_per_layer)

print(layer_age(5, 1200))
```

**Output:** `6000`

<sub>[Runnable file](code/applied/p088_age_of_a_rock_stack_layer_by_layer.py)</sub>

### Problem 89 — Greatest common divisor (Euclidean)

**Domain:** Mathematics

Recursive version of Problem 73.

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 180))
```

**Output:** `12`

<sub>[Runnable file](code/applied/p089_greatest_common_divisor_euclidean.py)</sub>

### Problem 90 — Count the digits of a number

**Domain:** Mathematics

How many digits does 987 654 have?

```python
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(987654))
```

**Output:** `6`

<sub>[Runnable file](code/applied/p090_count_the_digits_of_a_number.py)</sub>

### Problem 91 — Reverse a number

**Domain:** Mathematics

Turn 1234 into 4321.

```python
def reverse_number(n, acc=0):
    if n == 0:
        return acc
    return reverse_number(n // 10, acc * 10 + n % 10)

print(reverse_number(1234))
```

**Output:** `4321`

<sub>[Runnable file](code/applied/p091_reverse_a_number.py)</sub>

### Problem 92 — Decimal → binary as a string

**Domain:** Mathematics / Engineering

Convert a non-negative integer to its binary representation.

```python
def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)

print(to_binary(13))
```

**Output:** `1101`

<sub>[Runnable file](code/applied/p092_decimal_binary_as_a_string.py)</sub>

### Problem 93 — Recursive halving of a signal

**Domain:** Engineering

A signal's amplitude halves at every filter stage. Amplitude after `k` stages.

```python
def amplitude_after(initial, k):
    if k == 0:
        return initial
    return amplitude_after(initial, k - 1) / 2

print(amplitude_after(1024, 8))
```

**Output:** `4.0`

<sub>[Runnable file](code/applied/p093_recursive_halving_of_a_signal.py)</sub>

### Problem 94 — Sum of the first N natural numbers (recursive)

**Domain:** Mathematics

Recursive twin of Problem 41.

```python
def triangle_sum(n):
    if n == 0:
        return 0
    return n + triangle_sum(n - 1)

print(triangle_sum(100))
```

**Output:** `5050`

<sub>[Runnable file](code/applied/p094_sum_of_the_first_n_natural_numbers_recursive.py)</sub>

### Problem 95 — River-tributary count

**Domain:** Geography

A river system branches: each branch splits into 2 new branches for `n` levels. Total tributaries?

```python
def tributaries(n):
    if n == 0:
        return 1
    return 2 * tributaries(n - 1)

print(tributaries(6))
```

**Output:** `64`

<sub>[Runnable file](code/applied/p095_river_tributary_count.py)</sub>

### Problem 96 — Number of ancestors `g` generations back

**Domain:** Biology

You have 2 parents, 4 grandparents, 8 great-grandparents… How many ancestors at generation `g`?

```python
def ancestors(g):
    if g == 0:
        return 1   # you
    return 2 * ancestors(g - 1)

print(ancestors(10))
```

**Output:** `1024`

<sub>[Runnable file](code/applied/p096_number_of_ancestors_g_generations_back.py)</sub>

### Problem 97 — Tower of Hanoi — move count

**Domain:** Mathematics

Minimum moves to transfer `n` disks is `2^n − 1`, expressible recursively.

```python
def hanoi_moves(n):
    if n == 0:
        return 0
    return 2 * hanoi_moves(n - 1) + 1

print(hanoi_moves(8))
```

**Output:** `255`

<sub>[Runnable file](code/applied/p097_tower_of_hanoi_move_count.py)</sub>

### Problem 98 — Zeno's paradox — partial distance

**Domain:** Physics

Sum of 1/2 + 1/4 + 1/8 + … up to `n` terms (approaches 1).

```python
def zeno(n):
    if n == 0:
        return 0
    return 0.5 ** n + zeno(n - 1)

print(round(zeno(10), 6))
```

**Output:** `0.999023`

<sub>[Runnable file](code/applied/p098_zeno_s_paradox_partial_distance.py)</sub>

### Problem 99 — Pascal's triangle entry C(n, k)

**Domain:** Mathematics

`C(n, k) = C(n−1, k−1) + C(n−1, k)`, with base cases at the triangle's edges.

```python
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

print(pascal(6, 2))
```

**Output:** `15`

<sub>[Runnable file](code/applied/p099_pascal_s_triangle_entry_c_n_k.py)</sub>

### Problem 100 — Successive dilutions

**Domain:** Chemistry

Each dilution multiplies the concentration by 0.1 (a "1-in-10" dilution). Concentration after `n` dilutions?

```python
def diluted(initial_molar, n):
    if n == 0:
        return initial_molar
    return 0.1 * diluted(initial_molar, n - 1)

print(diluted(1.0, 5))
```

**Output:** `1.0000000000000004e-05` (floating-point round-off makes this ever-so-slightly off from `1e-05` — a useful lesson in itself.)

<sub>[Runnable file](code/applied/p100_successive_dilutions.py)</sub>
