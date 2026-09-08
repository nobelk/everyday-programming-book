# Chapter 18 — Bugs: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 18.1 Syntax Bugs

### Solution 18.1.1 — Rectangle perimeter

**Bug type:** Syntax

The `def` header is missing the colon that must end every function definition line, so Python cannot parse the file. Adding the colon lets the function be defined and called.

```python
def perimeter(length, width):
    return 2 * (length + width)

print(perimeter(8, 5))   # 26
```

<sub>[Exercise](find-the-bug.md#exercise-1811--rectangle-perimeter) · [Runnable file](code/find_the_bug/ex_18_01_01_rectangle_perimeter.py)</sub>

### Solution 18.1.2 — Tip calculator

**Bug type:** Syntax

The opening parenthesis after `bill *` is never closed, leaving an unbalanced bracket that the parser rejects. Closing the parenthesis fixes the expression.

```python
bill = 40.0
tip_rate = 0.15
total = bill + (bill * tip_rate)
print(total)   # 46.0
```

<sub>[Exercise](find-the-bug.md#exercise-1812--tip-calculator) · [Runnable file](code/find_the_bug/ex_18_01_02_tip_calculator.py)</sub>

### Solution 18.1.3 — Passing grade

**Bug type:** Syntax

The condition uses `=` (assignment) where a comparison `==` is required, which is a syntax error inside an `if`. Using `>=` expresses the intended ``score is at least 60'' test.

```python
score = 72
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

<sub>[Exercise](find-the-bug.md#exercise-1813--passing-grade) · [Runnable file](code/find_the_bug/ex_18_01_03_passing_grade.py)</sub>

### Solution 18.1.4 — Weekly distance

**Bug type:** Syntax

There is a missing operator (or comma) between `tuesday` and `wednesday`; two names sitting side by side cannot be parsed. Adding the `+` sums all three days.

```python
monday = 3.2
tuesday = 4.1
wednesday = 2.7
total = monday + tuesday + wednesday
print(total)   # 10.0
```

<sub>[Exercise](find-the-bug.md#exercise-1814--weekly-distance) · [Runnable file](code/find_the_bug/ex_18_01_04_weekly_distance.py)</sub>

### Solution 18.1.5 — Counting change

**Bug type:** Syntax

The `print` line is not indented under the `for`, so Python raises an `IndentationError` because a loop body is expected. Indenting the line by four spaces puts it inside the loop.

```python
coins = [25, 10, 5, 1]
for coin in coins:
    print(coin)
```

<sub>[Exercise](find-the-bug.md#exercise-1815--counting-change) · [Runnable file](code/find_the_bug/ex_18_01_05_counting_change.py)</sub>

## 18.2 Runtime Bugs

### Solution 18.2.1 — Average speed

**Bug type:** Runtime

Calling the function with `hours = 0` divides by zero at run time, raising `ZeroDivisionError`. Guarding against a zero time (or passing a real duration) avoids the crash.

```python
def average_speed(distance, hours):
    if hours == 0:
        return "Time cannot be zero"
    return distance / hours

print(average_speed(120, 2))   # 60.0
```

<sub>[Exercise](find-the-bug.md#exercise-1821--average-speed) · [Runnable file](code/find_the_bug/ex_18_02_01_average_speed.py)</sub>

### Solution 18.2.2 — Final price with tax

**Bug type:** Runtime

The expression references `tax`, but the variable defined above is `tax_rate`, so Python raises a `NameError`. Using the correct name computes the taxed price.

```python
price = 50.0
tax_rate = 0.08
final_price = price + (price * tax_rate)
print(final_price)   # 54.0
```

<sub>[Exercise](find-the-bug.md#exercise-1822--final-price-with-tax) · [Runnable file](code/find_the_bug/ex_18_02_02_final_price_with_tax.py)</sub>

### Solution 18.2.3 — Doubling a recipe

**Bug type:** Runtime

`cups_of_flour` is a string, and multiplying a string by a float raises `TypeError`. Storing the quantity as a number lets the multiplication work.

```python
cups_of_flour = 2.0
doubled = cups_of_flour * 2.0
print(doubled)   # 4.0
```

<sub>[Exercise](find-the-bug.md#exercise-1823--doubling-a-recipe) · [Runnable file](code/find_the_bug/ex_18_02_03_doubling_a_recipe.py)</sub>

### Solution 18.2.4 — Last student's score

**Bug type:** Runtime

`len(scores)` is 4, but valid indices run 0 to 3, so `scores[4]` raises `IndexError`. The last element is at index `len(scores) - 1` (or simply `-1`).

```python
scores = [88, 91, 79, 95]
last_index = len(scores) - 1
print(scores[last_index])   # 95
```

<sub>[Exercise](find-the-bug.md#exercise-1824--last-students-score) · [Runnable file](code/find_the_bug/ex_18_02_04_last_student_s_score.py)</sub>

### Solution 18.2.5 — Looking up a planet

**Bug type:** Runtime

The key `"mars"` is lowercase, but the dictionary key is `"Mars"`; dictionary lookups are case sensitive, so this raises `KeyError`. Matching the stored key returns the value.

```python
moons = {"Earth": 1, "Mars": 2, "Venus": 0}
print(moons["Mars"])   # 2
```

<sub>[Exercise](find-the-bug.md#exercise-1825--looking-up-a-planet) · [Runnable file](code/find_the_bug/ex_18_02_05_looking_up_a_planet.py)</sub>

## 18.3 Logical Bugs

### Solution 18.3.1 — Rectangle area

**Bug type:** Logical

The program runs but uses `+` where area requires multiplication, so it returns 10 instead of 24. Multiplying length by width gives the correct area.

```python
def area(length, width):
    return length * width

print(area(6, 4))   # 24
```

<sub>[Exercise](find-the-bug.md#exercise-1831--rectangle-area) · [Runnable file](code/find_the_bug/ex_18_03_01_rectangle_area.py)</sub>

### Solution 18.3.2 — Average of three grades

**Bug type:** Logical

Operator precedence divides only `c` by 3 before adding, so the result is wrong. Parenthesizing the sum before dividing computes the true average.

```python
def average(a, b, c):
    return (a + b + c) / 3

print(average(80, 90, 100))   # 90.0
```

<sub>[Exercise](find-the-bug.md#exercise-1832--average-of-three-grades) · [Runnable file](code/find_the_bug/ex_18_03_02_average_of_three_grades.py)</sub>

### Solution 18.3.3 — Counting to ten

**Bug type:** Logical

`range(1, 10)` stops at 9 because the upper bound is excluded, so 10 is never printed (an off-by-one error). Using `range(1, 11)` includes 10.

```python
for number in range(1, 11):
    print(number)
```

<sub>[Exercise](find-the-bug.md#exercise-1833--counting-to-ten) · [Runnable file](code/find_the_bug/ex_18_03_03_counting_to_ten.py)</sub>

### Solution 18.3.4 — Discounted price

**Bug type:** Logical

Multiplying by the discount rate gives the amount taken off, not the price paid, so the result is 20 instead of 60. The customer pays the remaining fraction, `1 - discount_rate`.

```python
price = 80.0
discount_rate = 0.25
final_price = price * (1 - discount_rate)
print(final_price)   # 60.0
```

<sub>[Exercise](find-the-bug.md#exercise-1834--discounted-price) · [Runnable file](code/find_the_bug/ex_18_03_04_discounted_price.py)</sub>

### Solution 18.3.5 — Fahrenheit to Celsius

**Bug type:** Logical

The conversion factor is inverted: Fahrenheit to Celsius multiplies by `5 / 9`, not `9 / 5`. Swapping the fraction gives the right temperature.

```python
def f_to_c(f):
    return (f - 32) * 5 / 9

print(f_to_c(212))   # 100.0
```

<sub>[Exercise](find-the-bug.md#exercise-1835--fahrenheit-to-celsius) · [Runnable file](code/find_the_bug/ex_18_03_05_fahrenheit_to_celsius.py)</sub>

## 18.4 Basic Debugging: Find and Fix Bugs

### Solution 18.4.1 — Total grocery cost

**Bug type:** Logical

Printing the subtotal reveals it is too low: the milk price is subtracted instead of added. Changing the `-` to `+` totals all three items.

```python
def total_cost(apples, bread, milk):
    subtotal = apples + bread + milk
    return subtotal

print(total_cost(3.50, 2.25, 1.75))   # 7.5
```

<sub>[Exercise](find-the-bug.md#exercise-1841--total-grocery-cost) · [Runnable file](code/find_the_bug/ex_18_04_01_total_grocery_cost.py)</sub>

### Solution 18.4.2 — Circle circumference

**Bug type:** Logical

Printing the returned value shows it is half the expected size: the formula omits the factor of 2 (circumference is `2 * pi * radius`). Adding the 2 corrects it.

```python
def circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

print(circumference(5))   # about 31.4
```

<sub>[Exercise](find-the-bug.md#exercise-1842--circle-circumference) · [Runnable file](code/find_the_bug/ex_18_04_02_circle_circumference.py)</sub>

### Solution 18.4.3 — Sum of a list

**Bug type:** Logical

Printing `total` inside the loop shows it only ever holds the latest value: the line replaces the running sum instead of adding to it. Using `+=` accumulates the total.

```python
rainfall = [1.2, 0.8, 2.0, 1.5]
total = 0
for amount in rainfall:
    total += amount
print(total)   # 5.5
```

<sub>[Exercise](find-the-bug.md#exercise-1843--sum-of-a-list) · [Runnable file](code/find_the_bug/ex_18_04_03_sum_of_a_list.py)</sub>

### Solution 18.4.4 — Sale price

**Bug type:** Logical

Printing `sale_price` shows it equals the discount amount, not the discounted price, so the subtraction yields the wrong savings. The savings are simply `price * discount_rate`.

```python
def savings(price, discount_rate):
    return price * discount_rate

print(savings(120, 0.30))   # 36.0
```

<sub>[Exercise](find-the-bug.md#exercise-1844--sale-price) · [Runnable file](code/find_the_bug/ex_18_04_04_sale_price.py)</sub>

### Solution 18.4.5 — Speed from distance and time

**Bug type:** Logical

Printing `result` reveals the division is inverted: speed is distance divided by time, not time divided by distance. Swapping the operands gives the correct speed.

```python
def speed(distance_km, time_hours):
    result = distance_km / time_hours
    return result

print(speed(150, 3))   # 50.0
```

<sub>[Exercise](find-the-bug.md#exercise-1845--speed-from-distance-and-time) · [Runnable file](code/find_the_bug/ex_18_04_05_speed_from_distance_and_time.py)</sub>
