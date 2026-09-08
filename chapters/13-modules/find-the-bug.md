# Chapter 13 — Modules: Find the Bug

Part V · Simple and Complex Programs — *Everyday Programming*

These programs use Python's modules — both the Standard Library and small modules you write yourself; each one below hides exactly one bug, so read closely and find it.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**10 exercises in 2 sections.**

## 13.1 Python Standard Library

### Exercise 13.1.1 — Square root with math

This program should print the length of the hypotenuse of a right triangle with legs 3 and 4 (it should be 5.0).

```python
import math

leg_a = 3
leg_b = 4
hypotenuse = math.sqrt(leg_a ** 2 - leg_b ** 2)
print(hypotenuse)   # 5.0
```

<sub>[Solution](solutions.md#solution-1311--square-root-with-math)</sub>

### Exercise 13.1.2 — Circle area with pi

This program should compute the area of a circle with radius 5 using π r².

```python
import math

radius = 5
area = math.pi() * radius ** 2
print(area)   # about 78.54
```

<sub>[Solution](solutions.md#solution-1312--circle-area-with-pi)</sub>

### Exercise 13.1.3 — Rolling a die

This program should print a random whole number from 1 to 6, like rolling a single die.

```python
import random

roll = random.randint(1, 7)
print(roll)   # a number from 1 to 6
```

<sub>[Solution](solutions.md#solution-1313--rolling-a-die)</sub>

### Exercise 13.1.4 — Average test score

This program should print the average of four test scores using the statistics module.

```python
import statistics

scores = [80, 90, 100, 70]
average = statistics.mean(scores)
print(statistic.mean(scores))   # expected: 85
```

<sub>[Solution](solutions.md#solution-1314--average-test-score)</sub>

### Exercise 13.1.5 — Rounding a price up

This program should round a price of $4.20 up to the next whole dollar using a from-import.

```python
from math import ceil

price = 4.20
rounded_up = math.ceil(price)
print(rounded_up)   # 5
```

<sub>[Solution](solutions.md#solution-1315--rounding-a-price-up)</sub>

## 13.2 Writing Your Own Module

### Exercise 13.2.1 — Importing your own helper

This two-file program should convert 100 degrees Celsius to Fahrenheit (212.0).

```python
# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

# file: main.py
from conversions import c_to_k

print(c_to_f(100))   # 212.0
```

<sub>[Solution](solutions.md#solution-1321--importing-your-own-helper)</sub>

### Exercise 13.2.2 — Calling with the module prefix

This two-file program should print the area of a 4-by-6 rectangle (24).

```python
# file: geometry.py
def rectangle_area(width, height):
    return width * height

# file: main.py
import geometry

print(rectangle_area(4, 6))   # 24
```

<sub>[Solution](solutions.md#solution-1322--calling-with-the-module-prefix)</sub>

### Exercise 13.2.3 — The main guard

This module should print a sample conversion only when run directly, but it should still work when imported.

```python
# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

if __name__ = "__main__":
    print(c_to_f(100))   # 212.0
```

<sub>[Solution](solutions.md#solution-1323--the-main-guard)</sub>

### Exercise 13.2.4 — Spelling the function name

This two-file program should print the perimeter of a square with side 5 (20).

```python
# file: shapes.py
def square_perimeter(side):
    return 4 * side

# file: main.py
import shapes

print(shapes.square_permieter(5))   # 20
```

<sub>[Solution](solutions.md#solution-1324--spelling-the-function-name)</sub>

### Exercise 13.2.5 — Kelvin conversion formula

This two-file program should convert 0 degrees Celsius to Kelvin (273.15).

```python
# file: conversions.py
def c_to_k(celsius):
    return celsius - 273.15

# file: main.py
from conversions import c_to_k

print(c_to_k(0))   # 273.15
```

<sub>[Solution](solutions.md#solution-1325--kelvin-conversion-formula)</sub>
