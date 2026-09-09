# Chapter 15 — Modules: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 13.1 Python Standard Library

### Solution 15.1.1 — Square root with math

**Bug type:** Runtime

The Pythagorean theorem adds the squares of the legs, but this code subtracts them, so `math.sqrt` receives 9-16=-7 and raises a `ValueError` (math domain error). Change the `-` to `+`.

```python
import math

leg_a = 3
leg_b = 4
hypotenuse = math.sqrt(leg_a ** 2 + leg_b ** 2)
print(hypotenuse)   # 5.0
```

<sub>[Exercise](find-the-bug.md#exercise-1311--square-root-with-math) · [Runnable file](code/find_the_bug/ex_13_01_01_square_root_with_math.py)</sub>

### Solution 15.1.2 — Circle area with pi

**Bug type:** Runtime

`math.pi` is a value (a float), not a function, so calling it as `math.pi()` raises `TypeError: 'float' object is not callable`. Remove the parentheses and multiply by the value directly.

```python
import math

radius = 5
area = math.pi * radius ** 2
print(area)   # about 78.54
```

<sub>[Exercise](find-the-bug.md#exercise-1312--circle-area-with-pi) · [Runnable file](code/find_the_bug/ex_13_01_02_circle_area_with_pi.py)</sub>

### Solution 15.1.3 — Rolling a die

**Bug type:** Logical

`random.randint(a, b)` includes *both* endpoints, so `randint(1, 7)` can return 7, which is impossible on a six-sided die. Use `random.randint(1, 6)`.

```python
import random

roll = random.randint(1, 6)
print(roll)   # a number from 1 to 6
```

<sub>[Exercise](find-the-bug.md#exercise-1313--rolling-a-die) · [Runnable file](code/find_the_bug/ex_13_01_03_rolling_a_die.py)</sub>

### Solution 15.1.4 — Average test score

**Bug type:** Runtime

The module was imported as `statistics`, but the call uses `statistic` (missing the final `s`), raising `NameError`. Use the same name in the call that you used in the import.

```python
import statistics

scores = [80, 90, 100, 70]
average = statistics.mean(scores)
print(statistics.mean(scores))   # 85
```

<sub>[Exercise](find-the-bug.md#exercise-1314--average-test-score) · [Runnable file](code/find_the_bug/ex_13_01_04_average_test_score.py)</sub>

### Solution 15.1.5 — Rounding a price up

**Bug type:** Runtime

With `from math import ceil`, the name brought into scope is `ceil`, not `math`, so `math.ceil(price)` raises `NameError`. Call `ceil(price)` directly.

```python
from math import ceil

price = 4.20
rounded_up = ceil(price)
print(rounded_up)   # 5
```

<sub>[Exercise](find-the-bug.md#exercise-1315--rounding-a-price-up) · [Runnable file](code/find_the_bug/ex_13_01_05_rounding_a_price_up.py)</sub>

## 13.2 Writing Your Own Module

### Solution 15.2.1 — Importing your own helper

**Bug type:** Runtime

The import line asks for `c_to_k`, but `conversions.py` only defines `c_to_f`, so the import raises `ImportError`. Import the function that actually exists.

```python
# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

# file: main.py
from conversions import c_to_f

print(c_to_f(100))   # 212.0
```

<sub>[Exercise](find-the-bug.md#exercise-1321--importing-your-own-helper) · [Runnable file](code/find_the_bug/ex_13_02_01_importing_your_own_helper.py)</sub>

### Solution 15.2.2 — Calling with the module prefix

**Bug type:** Runtime

With `import geometry`, the function must be called through its module as `geometry.rectangle_area(...)`; the bare name `rectangle_area` is undefined and raises `NameError`. Add the module prefix.

```python
# file: geometry.py
def rectangle_area(width, height):
    return width * height

# file: main.py
import geometry

print(geometry.rectangle_area(4, 6))   # 24
```

<sub>[Exercise](find-the-bug.md#exercise-1322--calling-with-the-module-prefix) · [Runnable file](code/find_the_bug/ex_13_02_02_calling_with_the_module_prefix.py)</sub>

### Solution 15.2.3 — The main guard

**Bug type:** Syntax

The guard uses a single `=` (assignment) instead of `==` (comparison), which is a syntax error inside an `if` condition. Use `==` to compare `__name__` with `"__main__"`.

```python
# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    print(c_to_f(100))   # 212.0
```

<sub>[Exercise](find-the-bug.md#exercise-1323--the-main-guard) · [Runnable file](code/find_the_bug/ex_13_02_03_the_main_guard.py)</sub>

### Solution 15.2.4 — Spelling the function name

**Bug type:** Runtime

The call misspells the function as `square_permieter`; the module `shapes` has no such attribute, so it raises `AttributeError`. Spell it `square_perimeter` to match the definition.

```python
# file: shapes.py
def square_perimeter(side):
    return 4 * side

# file: main.py
import shapes

print(shapes.square_perimeter(5))   # 20
```

<sub>[Exercise](find-the-bug.md#exercise-1324--spelling-the-function-name) · [Runnable file](code/find_the_bug/ex_13_02_04_spelling_the_function_name.py)</sub>

### Solution 15.2.5 — Kelvin conversion formula

**Bug type:** Logical

The Celsius-to-Kelvin formula adds 273.15, but the function subtracts it, giving -273.15 instead of 273.15. Change the operator to `+`.

```python
# file: conversions.py
def c_to_k(celsius):
    return celsius + 273.15

# file: main.py
from conversions import c_to_k

print(c_to_k(0))   # 273.15
```

<sub>[Exercise](find-the-bug.md#exercise-1325--kelvin-conversion-formula) · [Runnable file](code/find_the_bug/ex_13_02_05_kelvin_conversion_formula.py)</sub>
