# Chapter 18 — Testing: Find the Bug

Part VI · Quality — *Everyday Programming*

These exercises cover testing — writing small checks that confirm a Python function behaves as expected. Each program below contains exactly one bug, either in the function under test or in the test itself. Find the single bug in each program.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**15 exercises in 3 sections.**

## 17.1 Why Test Python Functions

### Exercise 18.1.1 — Rectangle area check

The function should return the area of a rectangle, and the assert should pass for a 4 × 3 rectangle.

```python
def rectangle_area(length, width):
    return length + width

assert rectangle_area(4, 3) == 12
print("passed")
```

<sub>[Solution](solutions.md#solution-1711--rectangle-area-check)</sub>

### Exercise 18.1.2 — Celsius to Fahrenheit check

The function converts Celsius to Fahrenheit, and the assert should confirm that 100 °C is 212 °F.

```python
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

assert c_to_f(100) == 211
print("passed")
```

<sub>[Solution](solutions.md#solution-1712--celsius-to-fahrenheit-check)</sub>

### Exercise 18.1.3 — Average of three grades

The function should return the average of three test grades, and the assert should pass for grades 80, 90, and 100.

```python
def average(a, b, c):
    return a + b + c / 3

assert average(80, 90, 100) == 90
print("passed")
```

<sub>[Solution](solutions.md#solution-1713--average-of-three-grades)</sub>

### Exercise 18.1.4 — Percent of a total

The function should return what percent `part` is of `whole`, and the assert should pass for 25 out of 50.

```python
def percent(part, whole)
    return part / whole * 100

assert percent(25, 50) == 50
print("passed")
```

<sub>[Solution](solutions.md#solution-1714--percent-of-a-total)</sub>

### Exercise 18.1.5 — Total cost with tax

The function should add 10% tax to a price, and the assert should pass for a $20 item costing $22.

```python
def total_with_tax(price):
    return price + price * 0.10

assert total_with_tax(20) == 20
print("passed")
```

<sub>[Solution](solutions.md#solution-1715--total-cost-with-tax)</sub>

## 17.2 Testing with Pytest

### Exercise 18.2.1 — Perimeter test

This pytest function checks that the perimeter of a square with side 5 is 20.

```python
def square_perimeter(side):
    return 4 * side

def test_square_perimeter():
    assert square_perimeter(5) == 25
```

<sub>[Solution](solutions.md#solution-1721--perimeter-test)</sub>

### Exercise 18.2.2 — Speed test

This pytest function should verify that traveling 100 km in 2 hours gives a speed of 50 km/h.

```python
def speed(distance, time):
    return distance * time

def test_speed():
    assert speed(100, 2) == 50
```

<sub>[Solution](solutions.md#solution-1722--speed-test)</sub>

### Exercise 18.2.3 — Discount test

This pytest function should check that a 20% discount on a $50 item leaves a $40 price.

```python
def discounted_price(price, percent_off):
    return price - price * percent_off / 100

def test_discounted_price():
    assert discounted_price(50, 20) == 40
    return True
```

<sub>[Solution](solutions.md#solution-1723--discount-test)</sub>

### Exercise 18.2.4 — Counting even numbers

This pytest function should confirm that there are 3 even numbers in the list `[1, 2, 3, 4, 6]`.

```python
def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])

def check_count_evens():
    assert count_evens([1, 2, 3, 4, 6]) == 3
```

<sub>[Solution](solutions.md#solution-1724--counting-even-numbers)</sub>

### Exercise 18.2.5 — Doubling a recipe

This pytest function should verify that doubling 3 cups of flour gives 6 cups.

```python
def double_recipe(cups):
    return cups * 2

def test_double_recipe():
    assert double_recipe(3) = 6
```

<sub>[Solution](solutions.md#solution-1725--doubling-a-recipe)</sub>

## 17.3 Helpful Tips

### Exercise 18.3.1 — Sum of an empty list

This pytest function tests the edge case of summing an empty list, which should give 0.

```python
def total(numbers):
    running = 0
    for n in numbers:
        running += n
    return running

def test_total_empty():
    assert total([]) == 1
```

<sub>[Solution](solutions.md#solution-1731--sum-of-an-empty-list)</sub>

### Exercise 18.3.2 — Floating-point area

This test checks the area of a circle of radius 2 (about 12.566) and should pass.

```python
import math

def area_circle(radius):
    return math.pi * radius ** 2

def test_area_circle():
    assert area_circle(2) == 12.566
```

<sub>[Solution](solutions.md#solution-1732--floating-point-area)</sub>

### Exercise 18.3.3 — Absolute value of negatives

This pytest function tests the edge case of a negative input, expecting `abs_value(-7)` to be 7.

```python
def abs_value(number):
    if number < 0:
        return number
    return number

def test_abs_value_negative():
    assert abs_value(-7) == 7
```

<sub>[Solution](solutions.md#solution-1733--absolute-value-of-negatives)</sub>

### Exercise 18.3.4 — Parametrized squares

This parametrized pytest checks that squaring 0, 2, and 5 gives 0, 4, and 25.

```python
import pytest

def square(n):
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (2, 4),
    (5, 20),
])
def test_square(n, expected):
    assert square(n) == expected
```

<sub>[Solution](solutions.md#solution-1734--parametrized-squares)</sub>

### Exercise 18.3.5 — Approximate division

This pytest function uses `pytest.approx` to check that dividing 1 by 3 is about 0.3333.

```python
import pytest

def divide(a, b):
    return a / b

def test_divide():
    assert divide(1, 3) == pytest.approx(0.3333, abs=0)
```

<sub>[Solution](solutions.md#solution-1735--approximate-division)</sub>
