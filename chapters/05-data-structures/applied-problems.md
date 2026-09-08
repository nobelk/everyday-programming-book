# Chapter 5 — Data Structures: Applied Problems

Real-world problems drawn from physics, chemistry, mathematics, biology, engineering, geology, and geography. Every formula needs no more than arithmetic, powers, square roots, and a little trigonometry.

Each problem states the situation, gives a short Python program, and shows what that program prints so you can check your own work. The programs are also available as runnable files under [`code/applied/`](code/applied).

**20 problems.**

## Variables (problems 1–20)

### Problem 1 — Kinetic energy of a moving car

**Domain:** Physics

A car of mass 1200 kg travels at 25 m/s. Compute its kinetic energy using `KE = 0.5 × m × v²`.

```python
mass_kg = 1200
velocity_mps = 25
kinetic_energy_j = 0.5 * mass_kg * velocity_mps ** 2
print(f"Kinetic energy: {kinetic_energy_j} J")
```

**Output:** `Kinetic energy: 375000.0 J`

<sub>[Runnable file](code/applied/p001_kinetic_energy_of_a_moving_car.py)</sub>

### Problem 2 — Moles of water in a glass

**Domain:** Chemistry

You pour 18 grams of water (molar mass 18 g/mol). How many moles is that?

```python
mass_g = 18.0
molar_mass_g_per_mol = 18.0
moles = mass_g / molar_mass_g_per_mol
print(f"Moles of water: {moles}")
```

**Output:** `Moles of water: 1.0`

<sub>[Runnable file](code/applied/p002_moles_of_water_in_a_glass.py)</sub>

### Problem 3 — Area of a circular pond

**Domain:** Mathematics

A circular pond has a radius of 7 m. Compute its area using `A = π r²`.

```python
pi = 3.14159
radius_m = 7
area_m2 = pi * radius_m ** 2
print(f"Pond area: {area_m2} m^2")
```

**Output:** `Pond area: 153.93791 m^2`

<sub>[Runnable file](code/applied/p003_area_of_a_circular_pond.py)</sub>

### Problem 4 — Body-mass index (BMI)

**Domain:** Biology

For a person 1.70 m tall weighing 65 kg, compute `BMI = mass / height²`.

```python
mass_kg = 65
height_m = 1.70
bmi = mass_kg / height_m ** 2
print(f"BMI: {bmi:.2f}")
```

**Output:** `BMI: 22.49`

<sub>[Runnable file](code/applied/p004_body_mass_index_bmi.py)</sub>

### Problem 5 — Electrical power of a bulb

**Domain:** Engineering

A bulb runs at 230 V and draws 0.26 A. Compute power using `P = V × I`.

```python
voltage_v = 230
current_a = 0.26
power_w = voltage_v * current_a
print(f"Power: {power_w:.2f} W")
```

**Output:** `Power: 59.80 W`

<sub>[Runnable file](code/applied/p005_electrical_power_of_a_bulb.py)</sub>

### Problem 6 — Density of a rock sample

**Domain:** Geology

A rock sample has mass 540 g and volume 200 cm³. Compute density using `ρ = m / V`.

```python
mass_g = 540
volume_cm3 = 200
density_g_per_cm3 = mass_g / volume_cm3
print(f"Density: {density_g_per_cm3} g/cm^3")
```

**Output:** `Density: 2.7 g/cm^3`

<sub>[Runnable file](code/applied/p006_density_of_a_rock_sample.py)</sub>

### Problem 7 — Travel time between cities

**Domain:** Geography

The road distance from A to B is 480 km and you drive at 60 km/h. How many hours does it take?

```python
distance_km = 480
speed_kmh = 60
time_h = distance_km / speed_kmh
print(f"Travel time: {time_h} hours")
```

**Output:** `Travel time: 8.0 hours`

<sub>[Runnable file](code/applied/p007_travel_time_between_cities.py)</sub>

### Problem 8 — Potential energy of a book on a shelf

**Domain:** Physics

A 1.2 kg book sits on a shelf 2.5 m high. With `g = 9.8`, compute `PE = m × g × h`.

```python
mass_kg = 1.2
g = 9.8
height_m = 2.5
potential_energy_j = mass_kg * g * height_m
print(f"Potential energy: {potential_energy_j} J")
```

**Output:** `Potential energy: 29.4 J`

<sub>[Runnable file](code/applied/p008_potential_energy_of_a_book_on_a_shelf.py)</sub>

### Problem 9 — Celsius to Kelvin

**Domain:** Chemistry

Convert 25 °C to Kelvin using `K = °C + 273.15`.

```python
temp_c = 25
temp_k = temp_c + 273.15
print(f"{temp_c} C = {temp_k} K")
```

**Output:** `25 C = 298.15 K`

<sub>[Runnable file](code/applied/p009_celsius_to_kelvin.py)</sub>

### Problem 10 — Ladder against a wall (Pythagoras)

**Domain:** Mathematics

A 5 m ladder leans against a wall with its base 3 m from the wall. Compute the height it reaches.

```python
ladder_m = 5
base_m = 3
height_m = (ladder_m ** 2 - base_m ** 2) ** 0.5
print(f"Height reached: {height_m} m")
```

**Output:** `Height reached: 4.0 m`

<sub>[Runnable file](code/applied/p010_ladder_against_a_wall_pythagoras.py)</sub>

### Problem 11 — Maximum heart rate for exercise

**Domain:** Biology

A common rule of thumb: `max_hr = 220 − age`. Compute it for a 15-year-old.

```python
age_years = 15
max_hr_bpm = 220 - age_years
print(f"Estimated max heart rate: {max_hr_bpm} bpm")
```

**Output:** `Estimated max heart rate: 205 bpm`

<sub>[Runnable file](code/applied/p011_maximum_heart_rate_for_exercise.py)</sub>

### Problem 12 — Ohm's law — current through a resistor

**Domain:** Engineering

A 12 V battery pushes current through a 4 Ω resistor. Compute `I = V / R`.

```python
voltage_v = 12
resistance_ohm = 4
current_a = voltage_v / resistance_ohm
print(f"Current: {current_a} A")
```

**Output:** `Current: 3.0 A`

<sub>[Runnable file](code/applied/p012_ohm_s_law_current_through_a_resistor.py)</sub>

### Problem 13 — Average speed of a cyclist

**Domain:** Physics

A cyclist covers 42 km in 1.75 hours. Compute average speed.

```python
distance_km = 42
time_h = 1.75
speed_kmh = distance_km / time_h
print(f"Average speed: {speed_kmh} km/h")
```

**Output:** `Average speed: 24.0 km/h`

<sub>[Runnable file](code/applied/p013_average_speed_of_a_cyclist.py)</sub>

### Problem 14 — Kilometres to miles

**Domain:** Geography

Convert a 100 km highway distance to miles (1 km ≈ 0.621371 mi).

```python
distance_km = 100
distance_mi = distance_km * 0.621371
print(f"{distance_km} km = {distance_mi:.4f} miles")
```

**Output:** `100 km = 62.1371 miles`

<sub>[Runnable file](code/applied/p014_kilometres_to_miles.py)</sub>

### Problem 15 — Simple interest on savings

**Domain:** Mathematics

Compute simple interest on ₹5000 at 6% per year for 3 years using `I = P × r × t`.

```python
principal = 5000
rate = 0.06
time_years = 3
interest = principal * rate * time_years
print(f"Interest earned: {interest}")
```

**Output:** `Interest earned: 900.0`

<sub>[Runnable file](code/applied/p015_simple_interest_on_savings.py)</sub>

### Problem 16 — pH of a solution

**Domain:** Chemistry

The hydrogen-ion concentration of lemon juice is 1e-2 mol/L. Compute `pH = −log10([H⁺])`.

```python
import math
h_concentration = 1e-2
ph = -math.log10(h_concentration)
print(f"pH: {ph}")
```

**Output:** `pH: 2.0`

<sub>[Runnable file](code/applied/p016_ph_of_a_solution.py)</sub>

### Problem 17 — Daily calorie need (simplified)

**Domain:** Biology

A rough basal-rate estimate: `BMR ≈ 10·mass + 6.25·height − 5·age + 5` (male, kg-cm-years).

```python
mass_kg = 70
height_cm = 175
age_years = 30
bmr_kcal = 10 * mass_kg + 6.25 * height_cm - 5 * age_years + 5
print(f"BMR: {bmr_kcal} kcal/day")
```

**Output:** `BMR: 1648.75 kcal/day`

<sub>[Runnable file](code/applied/p017_daily_calorie_need_simplified.py)</sub>

### Problem 18 — Stress on a supporting column

**Domain:** Engineering

A pillar supports 50 000 N over a cross-section of 0.25 m². Compute stress `σ = F / A`.

```python
force_n = 50000
area_m2 = 0.25
stress_pa = force_n / area_m2
print(f"Stress: {stress_pa} Pa")
```

**Output:** `Stress: 200000.0 Pa`

<sub>[Runnable file](code/applied/p018_stress_on_a_supporting_column.py)</sub>

### Problem 19 — Earthquake energy ratio (Richter)

**Domain:** Geology

Two earthquakes differ by 2 magnitudes. Compute the energy ratio ≈ `10^(1.5 × 2)`.

```python
magnitude_difference = 2
energy_ratio = 10 ** (1.5 * magnitude_difference)
print(f"Energy ratio: {energy_ratio}")
```

**Output:** `Energy ratio: 1000.0`

<sub>[Runnable file](code/applied/p019_earthquake_energy_ratio_richter.py)</sub>

### Problem 20 — Momentum of a football

**Domain:** Physics

A 0.45 kg football is kicked at 22 m/s. Compute momentum `p = m × v`.

```python
mass_kg = 0.45
velocity_mps = 22
momentum_kgmps = mass_kg * velocity_mps
print(f"Momentum: {momentum_kgmps} kg·m/s")
```

**Output:** `Momentum: 9.9 kg·m/s`

<sub>[Runnable file](code/applied/p020_momentum_of_a_football.py)</sub>
