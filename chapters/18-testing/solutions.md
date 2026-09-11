# Chapter 18 — Testing: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 17.1 Why Test Python Functions

### Solution 18.1.1 — Rectangle area check

**Bug type:** Logical

The function adds length and width instead of multiplying them, so it returns 7 and the assert fails. Area of a rectangle is length times width.

```python
def rectangle_area(length, width):
    return length * width

assert rectangle_area(4, 3) == 12
print("passed")
```

<sub>[Exercise](find-the-bug.md#exercise-1711--rectangle-area-check) · [Runnable file](code/find_the_bug/ex_17_01_01_rectangle_area_check.py)</sub>

### Solution 18.1.2 — Celsius to Fahrenheit check

**Bug type:** Logical

The function is correct, but the expected value in the test is wrong: 100 °C is 212 °F, not 211. The fix corrects the expected value.

```python
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

assert c_to_f(100) == 212
print("passed")
```

<sub>[Exercise](find-the-bug.md#exercise-1712--celsius-to-fahrenheit-check) · [Runnable file](code/find_the_bug/ex_17_01_02_celsius_to_fahrenheit_check.py)</sub>

### Solution 18.1.3 — Average of three grades

**Bug type:** Logical

Operator precedence divides only `c` by 3 before adding, instead of dividing the whole sum. Parentheses around the sum fix the formula so the average is computed correctly.

```python
def average(a, b, c):
    return (a + b + c) / 3

assert average(80, 90, 100) == 90
print("passed")
```

<sub>[Exercise](find-the-bug.md#exercise-1713--average-of-three-grades) · [Runnable file](code/find_the_bug/ex_17_01_03_average_of_three_grades.py)</sub>

### Solution 18.1.4 — Percent of a total

**Bug type:** Syntax

The function header is missing the colon at the end of the `def` line, so the file will not parse. Adding the colon fixes it.

```python
def percent(part, whole):
    return part / whole * 100

assert percent(25, 50) == 50
print("passed")
```

<sub>[Exercise](find-the-bug.md#exercise-1714--percent-of-a-total) · [Runnable file](code/find_the_bug/ex_17_01_04_percent_of_a_total.py)</sub>

### Solution 18.1.5 — Total cost with tax

**Bug type:** Logical

The function is correct (20 + 2 = 22), but the expected value in the assert is 20 instead of 22, so the check fails. The fix corrects the expected value.

```python
def total_with_tax(price):
    return price + price * 0.10

assert total_with_tax(20) == 22
print("passed")
```

<sub>[Exercise](find-the-bug.md#exercise-1715--total-cost-with-tax) · [Runnable file](code/find_the_bug/ex_17_01_05_total_cost_with_tax.py)</sub>

## 17.2 Testing with Pytest

### Solution 18.2.1 — Perimeter test

**Bug type:** Logical

The function correctly returns 4 × 5 = 20, but the test asserts 25, so it fails. The fix corrects the expected value to 20.

```python
def square_perimeter(side):
    return 4 * side

def test_square_perimeter():
    assert square_perimeter(5) == 20
```

<sub>[Exercise](find-the-bug.md#exercise-1721--perimeter-test) · [Runnable file](code/find_the_bug/ex_17_02_01_perimeter_test.py)</sub>

### Solution 18.2.2 — Speed test

**Bug type:** Logical

Speed is distance divided by time, but the function multiplies them, returning 200 instead of 50. Changing `*` to `/` fixes the formula.

```python
def speed(distance, time):
    return distance / time

def test_speed():
    assert speed(100, 2) == 50
```

<sub>[Exercise](find-the-bug.md#exercise-1722--speed-test) · [Runnable file](code/find_the_bug/ex_17_02_02_speed_test.py)</sub>

### Solution 18.2.3 — Discount test

**Bug type:** Logical

A pytest test should check with `assert` and not `return` a value; the trailing `return True` makes the test look like it passes regardless. Removing it leaves the assertion as the real check.

```python
def discounted_price(price, percent_off):
    return price - price * percent_off / 100

def test_discounted_price():
    assert discounted_price(50, 20) == 40
```

<sub>[Exercise](find-the-bug.md#exercise-1723--discount-test) · [Runnable file](code/find_the_bug/ex_17_02_03_discount_test.py)</sub>

### Solution 18.2.4 — Counting even numbers

**Bug type:** Logical

pytest only discovers functions whose names start with `test_`; `check_count_evens` will never be collected or run. Renaming it to `test_count_evens` lets pytest find it.

```python
def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])

def test_count_evens():
    assert count_evens([1, 2, 3, 4, 6]) == 3
```

<sub>[Exercise](find-the-bug.md#exercise-1724--counting-even-numbers) · [Runnable file](code/find_the_bug/ex_17_02_04_counting_even_numbers.py)</sub>

### Solution 18.2.5 — Doubling a recipe

**Bug type:** Syntax

The assert uses a single `=` (assignment) instead of `==` (comparison), which is a syntax error. Using `==` fixes the comparison.

```python
def double_recipe(cups):
    return cups * 2

def test_double_recipe():
    assert double_recipe(3) == 6
```

<sub>[Exercise](find-the-bug.md#exercise-1725--doubling-a-recipe) · [Runnable file](code/find_the_bug/ex_17_02_05_doubling_a_recipe.py)</sub>

## 17.3 Helpful Tips

### Solution 18.3.1 — Sum of an empty list

**Bug type:** Logical

The function correctly returns 0 for an empty list, but the test asserts 1, so the edge-case check fails. The fix corrects the expected value to 0.

```python
def total(numbers):
    running = 0
    for n in numbers:
        running += n
    return running

def test_total_empty():
    assert total([]) == 0
```

<sub>[Exercise](find-the-bug.md#exercise-1731--sum-of-an-empty-list) · [Runnable file](code/find_the_bug/ex_17_03_01_sum_of_an_empty_list.py)</sub>

### Solution 18.3.2 — Floating-point area

**Bug type:** Logical

Comparing a floating-point result with plain `==` fails here because `area_circle(2)` is 12.566370…, not exactly 12.566. Wrap the expected value in `pytest.approx` to allow a tiny tolerance.

```python
import math
import pytest

def area_circle(radius):
    return math.pi * radius ** 2

def test_area_circle():
    assert area_circle(2) == pytest.approx(12.566, abs=1e-3)
```

<sub>[Exercise](find-the-bug.md#exercise-1732--floating-point-area) · [Runnable file](code/find_the_bug/ex_17_03_02_floating_point_area.py)</sub>

### Solution 18.3.3 — Absolute value of negatives

**Bug type:** Logical

For a negative input the function returns the number unchanged instead of negating it, so `abs_value(-7)` gives -7. Returning `-number` in the negative branch fixes the edge case.

```python
def abs_value(number):
    if number < 0:
        return -number
    return number

def test_abs_value_negative():
    assert abs_value(-7) == 7
```

<sub>[Exercise](find-the-bug.md#exercise-1733--absolute-value-of-negatives) · [Runnable file](code/find_the_bug/ex_17_03_03_absolute_value_of_negatives.py)</sub>

### Solution 18.3.4 — Parametrized squares

**Bug type:** Logical

The third parameter case expects 20, but 5² = 25, so that case fails. Correcting the expected value to 25 makes all parametrized cases pass.

```python
import pytest

def square(n):
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (2, 4),
    (5, 25),
])
def test_square(n, expected):
    assert square(n) == expected
```

<sub>[Exercise](find-the-bug.md#exercise-1734--parametrized-squares) · [Runnable file](code/find_the_bug/ex_17_03_04_parametrized_squares.py)</sub>

### Solution 18.3.5 — Approximate division

**Bug type:** Logical

Setting `abs=0` gives `pytest.approx` zero tolerance, so 0.3333… never matches 0.3333 and the test fails. Using a small tolerance (or the default) lets the approximate comparison succeed.

```python
import pytest

def divide(a, b):
    return a / b

def test_divide():
    assert divide(1, 3) == pytest.approx(0.3333, abs=1e-4)
```

<sub>[Exercise](find-the-bug.md#exercise-1735--approximate-division) · [Runnable file](code/find_the_bug/ex_17_03_05_approximate_division.py)</sub>
