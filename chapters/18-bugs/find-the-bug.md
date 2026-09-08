# Chapter 18 — Bugs: Find the Bug

Part VI · Quality — *Everyday Programming*

Each program below has exactly one bug. The four sections sort the bugs by type — syntax, runtime, logical, and a set you debug with `print` — so you learn to recognize the whole taxonomy; read each program, predict what it should do, then find the single bug.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**20 exercises in 4 sections.**

## 18.1 Syntax Bugs

### Exercise 18.1.1 — Rectangle perimeter

This program should print the perimeter of a rectangle that is 8 metres by 5 metres.

```python
def perimeter(length, width)
    return 2 * (length + width)

print(perimeter(8, 5))   # expected: 26
```

<sub>[Solution](solutions.md#solution-1811--rectangle-perimeter)</sub>

### Exercise 18.1.2 — Tip calculator

This program should add a 15% tip to a $40 restaurant bill.

```python
bill = 40.0
tip_rate = 0.15
total = bill + (bill * tip_rate
print(total)   # expected: 46.0
```

<sub>[Solution](solutions.md#solution-1812--tip-calculator)</sub>

### Exercise 18.1.3 — Passing grade

This program should report whether a test score of 72 is a passing grade.

```python
score = 72
if score = 60:
    print("Pass")
else:
    print("Pass")
```

<sub>[Solution](solutions.md#solution-1813--passing-grade)</sub>

### Exercise 18.1.4 — Weekly distance

This program should print the total distance walked over three days.

```python
monday = 3.2
tuesday = 4.1
wednesday = 2.7
total = monday + tuesday wednesday
print(total)   # expected: 10.0
```

<sub>[Solution](solutions.md#solution-1814--weekly-distance)</sub>

### Exercise 18.1.5 — Counting change

This program should print each coin value in a small pile of change.

```python
coins = [25, 10, 5, 1]
for coin in coins:
print(coin)
```

<sub>[Solution](solutions.md#solution-1815--counting-change)</sub>

## 18.2 Runtime Bugs

### Exercise 18.2.1 — Average speed

This program should print average speed as distance divided by time.

```python
def average_speed(distance, hours):
    return distance / hours

print(average_speed(120, 0))
```

<sub>[Solution](solutions.md#solution-1821--average-speed)</sub>

### Exercise 18.2.2 — Final price with tax

This program should print a $50 item's price after 8% sales tax.

```python
price = 50.0
tax_rate = 0.08
final_price = price + (price * tax)
print(final_price)   # expected: 54.0
```

<sub>[Solution](solutions.md#solution-1822--final-price-with-tax)</sub>

### Exercise 18.2.3 — Doubling a recipe

This program should double the cups of flour in a recipe.

```python
cups_of_flour = "2"
doubled = cups_of_flour * 2.0
print(doubled)   # expected: 4.0
```

<sub>[Solution](solutions.md#solution-1823--doubling-a-recipe)</sub>

### Exercise 18.2.4 — Last student's score

This program should print the score of the last student in the list.

```python
scores = [88, 91, 79, 95]
last_index = len(scores)
print(scores[last_index])   # expected: 95
```

<sub>[Solution](solutions.md#solution-1824--last-students-score)</sub>

### Exercise 18.2.5 — Looking up a planet

This program should print the number of moons for Mars.

```python
moons = {"Earth": 1, "Mars": 2, "Venus": 0}
print(moons["mars"])   # expected: 2
```

<sub>[Solution](solutions.md#solution-1825--looking-up-a-planet)</sub>

## 18.3 Logical Bugs

### Exercise 18.3.1 — Rectangle area

This program should print the area of a 6 by 4 rectangle.

```python
def area(length, width):
    return length + width

print(area(6, 4))   # expected: 24
```

<sub>[Solution](solutions.md#solution-1831--rectangle-area)</sub>

### Exercise 18.3.2 — Average of three grades

This program should print the average of three test grades.

```python
def average(a, b, c):
    return a + b + c / 3

print(average(80, 90, 100))   # expected: 90.0
```

<sub>[Solution](solutions.md#solution-1832--average-of-three-grades)</sub>

### Exercise 18.3.3 — Counting to ten

This program should print the numbers 1 through 10.

```python
for number in range(1, 10):
    print(number)
```

<sub>[Solution](solutions.md#solution-1833--counting-to-ten)</sub>

### Exercise 18.3.4 — Discounted price

This program should print the price of a $80 jacket after a 25% discount.

```python
price = 80.0
discount_rate = 0.25
final_price = price * discount_rate
print(final_price)   # expected: 60.0
```

<sub>[Solution](solutions.md#solution-1834--discounted-price)</sub>

### Exercise 18.3.5 — Fahrenheit to Celsius

This program should convert 212 degrees Fahrenheit to Celsius.

```python
def f_to_c(f):
    return (f - 32) * 9 / 5

print(f_to_c(212))   # expected: 100.0
```

<sub>[Solution](solutions.md#solution-1835--fahrenheit-to-celsius)</sub>

## 18.4 Basic Debugging: Find and Fix Bugs

### Exercise 18.4.1 — Total grocery cost

This program should print the total cost of three grocery items, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def total_cost(apples, bread, milk):
    subtotal = apples + bread - milk
    return subtotal

print(total_cost(3.50, 2.25, 1.75))   # expected: 7.5
```

<sub>[Solution](solutions.md#solution-1841--total-grocery-cost)</sub>

### Exercise 18.4.2 — Circle circumference

This program should print the circumference of a circle with radius 5, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def circumference(radius):
    pi = 3.14159
    return pi * radius

print(circumference(5))   # expected: about 31.4
```

<sub>[Solution](solutions.md#solution-1842--circle-circumference)</sub>

### Exercise 18.4.3 — Sum of a list

This program should print the sum of the daily rainfall totals, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
rainfall = [1.2, 0.8, 2.0, 1.5]
total = 0
for amount in rainfall:
    total = amount
print(total)   # expected: 5.5
```

<sub>[Solution](solutions.md#solution-1843--sum-of-a-list)</sub>

### Exercise 18.4.4 — Sale price

This program should print the savings on a $120 item at 30% off, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def savings(price, discount_rate):
    sale_price = price * discount_rate
    return price - sale_price

print(savings(120, 0.30))   # expected: 36.0
```

<sub>[Solution](solutions.md#solution-1844--sale-price)</sub>

### Exercise 18.4.5 — Speed from distance and time

This program should print speed in kilometres per hour, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def speed(distance_km, time_hours):
    result = time_hours / distance_km
    return result

print(speed(150, 3))   # expected: 50.0
```

<sub>[Solution](solutions.md#solution-1845--speed-from-distance-and-time)</sub>
