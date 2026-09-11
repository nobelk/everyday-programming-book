# Chapter 10 — Control Flow: Applied Problems

Real-world problems drawn from physics, chemistry, mathematics, biology, engineering, geology, and geography. Every formula needs no more than arithmetic, powers, square roots, and a little trigonometry.

Each problem states the situation, gives a short Python program, and shows what that program prints so you can check your own work. The programs are also available as runnable files under [`code/applied/`](code/applied).

**40 problems.**

## Conditionals (problems 21–40)

### Problem 21 — BMI category

**Domain:** Biology

Classify a BMI as Underweight (<18.5), Normal (<25), Overweight (<30), or Obese (≥30).

```python
bmi = 27.3
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI {bmi} is {category}")
```

**Output:** `BMI 27.3 is Overweight`

<sub>[Runnable file](code/applied/p021_bmi_category.py)</sub>

### Problem 22 — Will an object float?

**Domain:** Physics

An object floats in water if its density is less than 1.0 g/cm³.

```python
density = 0.8
if density < 1.0:
    print("Object floats")
else:
    print("Object sinks")
```

**Output:** `Object floats`

<sub>[Runnable file](code/applied/p022_will_an_object_float.py)</sub>

### Problem 23 — Acid, base or neutral?

**Domain:** Chemistry

Given a pH, print "Acidic", "Neutral", or "Basic".

```python
ph = 8.2
if ph < 7:
    print("Acidic")
elif ph == 7:
    print("Neutral")
else:
    print("Basic")
```

**Output:** `Basic`

<sub>[Runnable file](code/applied/p023_acid_base_or_neutral.py)</sub>

### Problem 24 — Largest of three test scores

**Domain:** Mathematics

Print the highest of three scores.

```python
a, b, c = 72, 85, 78
if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c
print(f"Highest: {largest}")
```

**Output:** `Highest: 85`

<sub>[Runnable file](code/applied/p024_largest_of_three_test_scores.py)</sub>

### Problem 25 — Safe load on a bridge

**Domain:** Engineering

A footbridge is rated 3 000 kg. Tell a group whether they can cross.

```python
group_mass_kg = 2750
if group_mass_kg <= 3000:
    print("Safe to cross")
else:
    print("Too heavy")
```

**Output:** `Safe to cross`

<sub>[Runnable file](code/applied/p025_safe_load_on_a_bridge.py)</sub>

### Problem 26 — Earthquake severity

**Domain:** Geology

Classify a Richter magnitude as Minor (<4), Light (<5), Moderate (<6), Strong (<7), Major (<8), or Great (≥8).

```python
magnitude = 6.3
if magnitude < 4:
    level = "Minor"
elif magnitude < 5:
    level = "Light"
elif magnitude < 6:
    level = "Moderate"
elif magnitude < 7:
    level = "Strong"
elif magnitude < 8:
    level = "Major"
else:
    level = "Great"
print(f"Magnitude {magnitude}: {level}")
```

**Output:** `Magnitude 6.3: Strong`

<sub>[Runnable file](code/applied/p026_earthquake_severity.py)</sub>

### Problem 27 — Climate zone by temperature

**Domain:** Geography

Given an average annual temperature, label the climate as Polar (<0), Cold (<10), Temperate (<20), or Tropical (≥20).

```python
temp_c = 14
if temp_c < 0:
    zone = "Polar"
elif temp_c < 10:
    zone = "Cold"
elif temp_c < 20:
    zone = "Temperate"
else:
    zone = "Tropical"
print(f"{temp_c} C → {zone}")
```

**Output:** `14 C → Temperate`

<sub>[Runnable file](code/applied/p027_climate_zone_by_temperature.py)</sub>

### Problem 28 — Blood-pressure category

**Domain:** Biology

Using systolic pressure, classify as Low (<90), Normal (<120), Elevated (<130), High (<140), or Hypertensive (≥140).

```python
systolic = 135
if systolic < 90:
    category = "Low"
elif systolic < 120:
    category = "Normal"
elif systolic < 130:
    category = "Elevated"
elif systolic < 140:
    category = "High"
else:
    category = "Hypertensive"
print(f"Systolic {systolic}: {category}")
```

**Output:** `Systolic 135: High`

<sub>[Runnable file](code/applied/p028_blood_pressure_category.py)</sub>

### Problem 29 — Phase of water

**Domain:** Physics

Given a temperature at 1 atm, is the water ice, liquid, or steam?

```python
temp_c = 105
if temp_c <= 0:
    phase = "ice"
elif temp_c < 100:
    phase = "liquid water"
else:
    phase = "steam"
print(f"At {temp_c} C water is {phase}")
```

**Output:** `At 105 C water is steam`

<sub>[Runnable file](code/applied/p029_phase_of_water.py)</sub>

### Problem 30 — Exothermic or endothermic?

**Domain:** Chemistry

If the enthalpy change ΔH is negative, the reaction is exothermic; otherwise endothermic.

```python
delta_h_kj = -92
if delta_h_kj < 0:
    print("Exothermic")
else:
    print("Endothermic")
```

**Output:** `Exothermic`

<sub>[Runnable file](code/applied/p030_exothermic_or_endothermic.py)</sub>

### Problem 31 — Even or odd number of petals

**Domain:** Mathematics

A flower has 13 petals — is that even or odd?

```python
petals = 13
if petals % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:** `Odd`

<sub>[Runnable file](code/applied/p031_even_or_odd_number_of_petals.py)</sub>

### Problem 32 — Classify an animal by number of legs

**Domain:** Biology

Given leg count, label the animal (0 → snake-like, 2 → biped, 4 → quadruped, 6 → insect, 8 → arachnid).

```python
legs = 6
if legs == 0:
    kind = "snake-like"
elif legs == 2:
    kind = "biped"
elif legs == 4:
    kind = "quadruped"
elif legs == 6:
    kind = "insect"
elif legs == 8:
    kind = "arachnid"
else:
    kind = "unknown"
print(f"{legs} legs → {kind}")
```

**Output:** `6 legs → insect`

<sub>[Runnable file](code/applied/p032_classify_an_animal_by_number_of_legs.py)</sub>

### Problem 33 — Fuel efficiency rating

**Domain:** Engineering

A car's km per litre is rated Poor (<10), Average (<15), Good (<20), or Excellent (≥20).

```python
kmpl = 17
if kmpl < 10:
    rating = "Poor"
elif kmpl < 15:
    rating = "Average"
elif kmpl < 20:
    rating = "Good"
else:
    rating = "Excellent"
print(f"{kmpl} km/L → {rating}")
```

**Output:** `17 km/L → Good`

<sub>[Runnable file](code/applied/p033_fuel_efficiency_rating.py)</sub>

### Problem 34 — Rock identification by density

**Domain:** Geology

A rock with density <2.5 is likely sedimentary, 2.5–3.0 igneous, above 3.0 metamorphic (very rough rule).

```python
density = 2.8
if density < 2.5:
    rock = "Sedimentary"
elif density <= 3.0:
    rock = "Igneous"
else:
    rock = "Metamorphic"
print(f"Density {density} → {rock}")
```

**Output:** `Density 2.8 → Igneous`

<sub>[Runnable file](code/applied/p034_rock_identification_by_density.py)</sub>

### Problem 35 — Northern or southern hemisphere?

**Domain:** Geography

Positive latitude → northern; negative → southern; 0 → equator.

```python
latitude = -23.5
if latitude > 0:
    print("Northern hemisphere")
elif latitude < 0:
    print("Southern hemisphere")
else:
    print("On the equator")
```

**Output:** `Southern hemisphere`

<sub>[Runnable file](code/applied/p035_northern_or_southern_hemisphere.py)</sub>

### Problem 36 — Will a ball clear a wall?

**Domain:** Physics

A ball is thrown and reaches a height of 4.5 m at the wall. The wall is 5.0 m tall — does it clear?

```python
ball_height_m = 4.5
wall_height_m = 5.0
if ball_height_m >= wall_height_m:
    print("Clears the wall")
else:
    print("Hits the wall")
```

**Output:** `Hits the wall`

<sub>[Runnable file](code/applied/p036_will_a_ball_clear_a_wall.py)</sub>

### Problem 37 — Solubility category

**Domain:** Chemistry

Solubility (g per 100 g water) <0.1 is insoluble, <1 slightly soluble, else soluble.

```python
solubility = 0.35
if solubility < 0.1:
    label = "Insoluble"
elif solubility < 1:
    label = "Slightly soluble"
else:
    label = "Soluble"
print(f"Solubility {solubility} → {label}")
```

**Output:** `Solubility 0.35 → Slightly soluble`

<sub>[Runnable file](code/applied/p037_solubility_category.py)</sub>

### Problem 38 — Quadratic — real or complex roots?

**Domain:** Mathematics

Compute the discriminant `b² − 4ac` and say whether roots are real or complex.

```python
a, b, c = 1, 3, 5
discriminant = b * b - 4 * a * c
if discriminant >= 0:
    print("Real roots")
else:
    print("Complex roots")
```

**Output:** `Complex roots`

<sub>[Runnable file](code/applied/p038_quadratic_real_or_complex_roots.py)</sub>

### Problem 39 — Blood-donor eligibility

**Domain:** Biology

Must be at least 17 years old AND weigh at least 50 kg.

```python
age_years = 18
mass_kg = 55
if age_years >= 17 and mass_kg >= 50:
    print("Eligible to donate")
else:
    print("Not eligible")
```

**Output:** `Eligible to donate`

<sub>[Runnable file](code/applied/p039_blood_donor_eligibility.py)</sub>

### Problem 40 — Traffic-light action

**Domain:** Engineering

Given the current light, print the instruction for a driver.

```python
light = "yellow"
if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow down")
elif light == "red":
    print("Stop")
else:
    print("Unknown signal")
```

**Output:** `Slow down`

<sub>[Runnable file](code/applied/p040_traffic_light_action.py)</sub>

## Loops (problems 41–60)

### Problem 41 — Sum of first N natural numbers

**Domain:** Mathematics

Add up 1 + 2 + … + 100.

```python
total = 0
for i in range(1, 101):
    total = total + i
print(f"Sum: {total}")
```

**Output:** `Sum: 5050`

<sub>[Runnable file](code/applied/p041_sum_of_first_n_natural_numbers.py)</sub>

### Problem 42 — Position of a falling stone each second

**Domain:** Physics

Print the distance fallen after each second for 5 seconds using `d = 0.5 g t²`.

```python
g = 9.8
for t in range(1, 6):
    distance_m = 0.5 * g * t * t
    print(f"t = {t} s, fallen {distance_m} m")
```

**Output:**
```
t = 1 s, fallen 4.9 m
t = 2 s, fallen 19.6 m
t = 3 s, fallen 44.1 m
t = 4 s, fallen 78.4 m
t = 5 s, fallen 122.5 m
```

<sub>[Runnable file](code/applied/p042_position_of_a_falling_stone_each_second.py)</sub>

### Problem 43 — Radioactive half-life decay

**Domain:** Chemistry

Starting with 1000 atoms, print how many remain after each of 5 half-lives.

```python
atoms = 1000
for half_life in range(1, 6):
    atoms = atoms / 2
    print(f"After {half_life} half-lives: {atoms} atoms")
```

**Output:**
```
After 1 half-lives: 500.0 atoms
After 2 half-lives: 250.0 atoms
After 3 half-lives: 125.0 atoms
After 4 half-lives: 62.5 atoms
After 5 half-lives: 31.25 atoms
```

<sub>[Runnable file](code/applied/p043_radioactive_half_life_decay.py)</sub>

### Problem 44 — Bacterial growth

**Domain:** Biology

A bacterium divides every 20 min. Starting with 1, how many are there after 6 divisions?

```python
bacteria = 1
for division in range(1, 7):
    bacteria = bacteria * 2
    print(f"Division {division}: {bacteria} bacteria")
```

**Output (final line):** `Division 6: 64 bacteria`

<sub>[Runnable file](code/applied/p044_bacterial_growth.py)</sub>

### Problem 45 — Resistors in series

**Domain:** Engineering

Add up four resistor values.

```python
resistors_ohm = [10, 22, 47, 100]
total_r = 0
for r in resistors_ohm:
    total_r = total_r + r
print(f"Total resistance: {total_r} Ohm")
```

**Output:** `Total resistance: 179 Ohm`

<sub>[Runnable file](code/applied/p045_resistors_in_series.py)</sub>

### Problem 46 — Sediment build-up over a century

**Domain:** Geology

A lake bed gains 2 mm of sediment per year. Total in 100 years?

```python
total_mm = 0
for year in range(1, 101):
    total_mm = total_mm + 2
print(f"Total sediment in 100 years: {total_mm} mm")
```

**Output:** `Total sediment in 100 years: 200 mm`

<sub>[Runnable file](code/applied/p046_sediment_build_up_over_a_century.py)</sub>

### Problem 47 — Annual rainfall average

**Domain:** Geography

Average 12 monthly rainfall readings.

```python
monthly_mm = [12, 18, 40, 80, 120, 250, 300, 280, 170, 60, 20, 10]
total = 0
for mm in monthly_mm:
    total = total + mm
average = total / len(monthly_mm)
print(f"Average rainfall: {average} mm/month")
```

**Output:** `Average rainfall: 113.33333333333333 mm/month`

<sub>[Runnable file](code/applied/p047_annual_rainfall_average.py)</sub>

### Problem 48 — Multiplication table

**Domain:** Mathematics

Print the 7-times table up to 7×10.

```python
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

**Output (first 3 lines):**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
```

<sub>[Runnable file](code/applied/p048_multiplication_table.py)</sub>

### Problem 49 — Bouncing-ball total distance

**Domain:** Physics

A ball dropped from 10 m loses 20% of its height each bounce. Total distance after 5 bounces (up and down).

```python
height_m = 10
total_distance = height_m
for bounce in range(5):
    height_m = height_m * 0.8
    total_distance = total_distance + 2 * height_m
print(f"Total distance: {total_distance:.2f} m")
```

**Output:** `Total distance: 63.79 m`

<sub>[Runnable file](code/applied/p049_bouncing_ball_total_distance.py)</sub>

### Problem 50 — Titration volume running total

**Domain:** Chemistry

Add drops of base (0.05 mL each) until 25 drops are added; report volume after every 5 drops.

```python
volume_ml = 0
for drop in range(1, 26):
    volume_ml = volume_ml + 0.05
    if drop % 5 == 0:
        print(f"After {drop} drops: {volume_ml:.2f} mL")
```

**Output:**
```
After 5 drops: 0.25 mL
After 10 drops: 0.50 mL
After 15 drops: 0.75 mL
After 20 drops: 1.00 mL
After 25 drops: 1.25 mL
```

<sub>[Runnable file](code/applied/p050_titration_volume_running_total.py)</sub>

### Problem 51 — Rabbit population over 8 generations

**Domain:** Biology

Each generation triples the rabbits. Start with 2.

```python
rabbits = 2
for gen in range(1, 9):
    rabbits = rabbits * 3
    print(f"Gen {gen}: {rabbits} rabbits")
```

**Output (last line):** `Gen 8: 13122 rabbits`

<sub>[Runnable file](code/applied/p051_rabbit_population_over_8_generations.py)</sub>

### Problem 52 — Compound interest year by year

**Domain:** Engineering / Mathematics

₹1000 at 8% compounded annually for 5 years.

```python
amount = 1000
rate = 0.08
for year in range(1, 6):
    amount = amount * (1 + rate)
    print(f"Year {year}: {amount:.2f}")
```

**Output:**
```
Year 1: 1080.00
Year 2: 1166.40
Year 3: 1259.71
Year 4: 1360.49
Year 5: 1469.33
```

<sub>[Runnable file](code/applied/p052_compound_interest_year_by_year.py)</sub>

### Problem 53 — Divisors of a number

**Domain:** Mathematics

Print every positive divisor of 36.

```python
n = 36
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
```

**Output (single column):** `1 2 3 4 6 9 12 18 36`

<sub>[Runnable file](code/applied/p053_divisors_of_a_number.py)</sub>

### Problem 54 — Pendulum period for several lengths

**Domain:** Physics

`T = 2π √(L / g)`. Print the period for L = 0.5, 1.0, 1.5, 2.0 m.

```python
import math
g = 9.8
for length_m in [0.5, 1.0, 1.5, 2.0]:
    period_s = 2 * math.pi * math.sqrt(length_m / g)
    print(f"L = {length_m} m → T = {period_s:.3f} s")
```

**Output:**
```
L = 0.5 m → T = 1.419 s
L = 1.0 m → T = 2.007 s
L = 1.5 m → T = 2.458 s
L = 2.0 m → T = 2.838 s
```

<sub>[Runnable file](code/applied/p054_pendulum_period_for_several_lengths.py)</sub>

### Problem 55 — Large-population countries

**Domain:** Geography

From a small list, print only countries with more than 100 million people.

```python
populations_millions = {
    "India": 1428, "USA": 334, "Sri Lanka": 22,
    "Nepal": 30, "Brazil": 216, "Japan": 124,
}
for country, pop in populations_millions.items():
    if pop > 100:
        print(f"{country}: {pop} million")
```

**Output:**
```
India: 1428 million
USA: 334 million
Brazil: 216 million
Japan: 124 million
```

<sub>[Runnable file](code/applied/p055_large_population_countries.py)</sub>

### Problem 56 — Temperature gradient down a mine

**Domain:** Geology

Surface is 20 °C; temperature rises 25 °C per km of depth. Print temperature every 500 m to 3 km.

```python
surface_c = 20
for depth_m in range(500, 3001, 500):
    temp_c = surface_c + 25 * (depth_m / 1000)
    print(f"{depth_m} m → {temp_c} C")
```

**Output:**
```
500 m → 32.5 C
1000 m → 45.0 C
1500 m → 57.5 C
2000 m → 70.0 C
2500 m → 82.5 C
3000 m → 95.0 C
```

<sub>[Runnable file](code/applied/p056_temperature_gradient_down_a_mine.py)</sub>

### Problem 57 — Primes up to N (simple check)

**Domain:** Mathematics

Print every prime from 2 to 30.

```python
for n in range(2, 31):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
```

**Output:** `2 3 5 7 11 13 17 19 23 29`

<sub>[Runnable file](code/applied/p057_primes_up_to_n_simple_check.py)</sub>

### Problem 58 — Heart-rate readings during exercise

**Domain:** Biology

Given a list of minute-by-minute bpm readings, print the highest.

```python
readings_bpm = [72, 88, 102, 118, 131, 144, 152, 149, 140, 128]
max_bpm = readings_bpm[0]
for bpm in readings_bpm:
    if bpm > max_bpm:
        max_bpm = bpm
print(f"Peak heart rate: {max_bpm} bpm")
```

**Output:** `Peak heart rate: 152 bpm`

<sub>[Runnable file](code/applied/p058_heart_rate_readings_during_exercise.py)</sub>

### Problem 59 — Highest sensor reading

**Domain:** Engineering

A strain-gauge produced these micro-strain values — find the maximum.

```python
readings = [120, 135, 142, 160, 158, 170, 165]
peak = 0
for r in readings:
    if r > peak:
        peak = r
print(f"Peak strain: {peak} µε")
```

**Output:** `Peak strain: 170 µε`

<sub>[Runnable file](code/applied/p059_highest_sensor_reading.py)</sub>

### Problem 60 — Rainwater collected by a row of cylinders

**Domain:** Physics / Geography

Five rain gauges hold different volumes. Print the running total as you empty them.

```python
gauges_ml = [120, 85, 140, 95, 110]
total_ml = 0
for i, v in enumerate(gauges_ml, start=1):
    total_ml = total_ml + v
    print(f"After gauge {i}: total = {total_ml} mL")
```

**Output:**
```
After gauge 1: total = 120 mL
After gauge 2: total = 205 mL
After gauge 3: total = 345 mL
After gauge 4: total = 440 mL
After gauge 5: total = 550 mL
```

<sub>[Runnable file](code/applied/p060_rainwater_collected_by_a_row_of_cylinders.py)</sub>
