# Chapter 11 — Scoping: Find the Bug

Part IV · Control Flow — *Everyday Programming*

These exercises are about scope — where a name can be found and used (local, enclosing, global, built-in); each program below has exactly one bug, so read it, predict what it should do, and find the single bug.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**30 exercises in 6 sections.**

## 11.1 Local and Global Scope

### Exercise 11.1.1 — reading a global from a function

This program should print the speed limit twice: once from inside `report()` and once from the top level.

```python
speed_limit_kmh = 100

def report():
    print("Inside:", speed_limit_kmh)

report()
print("Outside:", speed_limit)
# Expected:
# Inside: 100
# Outside: 100
```

<sub>[Solution](solutions.md#solution-1111--reading-a-global-from-a-function)</sub>

### Exercise 11.1.2 — a local name stays local

A scientist measures a temperature inside a helper function. The program should print the reading from inside the function only.

```python
def take_reading():
    temperature_c = 21.5
    print("Reading:", temperature_c)

take_reading()
print("Confirmed:", temperature_c)
# Expected:
# Reading: 21.5
```

<sub>[Solution](solutions.md#solution-1112--a-local-name-stays-local)</sub>

### Exercise 11.1.3 — a global constant for area

Using a global value of `pi`, this program should compute the area of a circle with radius 3 and print about 28.27.

```python
pi = 3.14159

def circle_area():
    area = pi * 3 * 3

circle_area()
print("Area:", area)
# expected: Area: 28.27431
```

<sub>[Solution](solutions.md#solution-1113--a-global-constant-for-area)</sub>

### Exercise 11.1.4 — the helper's result must come back out

This program should compute the perimeter of a rectangle and print it at the top level.

```python
def perimeter(length, width):
    edges = 2 * (length + width)

result = perimeter(5, 3)
print("Perimeter:", result)
# Expected:
# Perimeter: 16
```

<sub>[Solution](solutions.md#solution-1114--the-helpers-result-must-come-back-out)</sub>

### Exercise 11.1.5 — global list, read inside the function

This program should print the average of a global list of test scores.

```python
scores = [80, 90, 100]

def average()
    return sum(scores) / len(scores)

print("Average:", average())
# Expected:
# Average: 90.0
```

<sub>[Solution](solutions.md#solution-1115--global-list-read-inside-the-function)</sub>

## 11.2 A Local Variable Can Hide a Global Variable

### Exercise 11.2.1 — local hides global, on purpose

The global `discount` is 0.10. Inside `checkout()` a local `discount` of 0.25 should be used for one sale, but the global should stay 0.10. The program should print the local rate then the global rate.

```python
discount = 0.10

def checkout():
    discount = 0.25
    print("Sale rate:", discount)

checkout()
print("Normal rate:", discount)
# Expected:
# Sale rate: 0.1
# Normal rate: 0.1
```

<sub>[Solution](solutions.md#solution-1121--local-hides-global-on-purpose)</sub>

### Exercise 11.2.2 — the local shadow should win inside

Inside `convert()`, a local `factor` should shadow the global `factor` so the function multiplies by 1000. The program should print 5000.

```python
factor = 1

def convert(kilometers):
    factor = 1000
    return kilometers / factor

print("Meters:", convert(5))
# Expected:
# Meters: 5000
```

<sub>[Solution](solutions.md#solution-1122--the-local-shadow-should-win-inside)</sub>

### Exercise 11.2.3 — shadowing a built-in name

This program should add up a list of grocery prices and print the total.

```python
prices = [2.50, 1.25, 3.00]
sum = 0

def total():
    return sum(prices)

print("Total:", total())
# Expected:
# Total: 6.75
```

<sub>[Solution](solutions.md#solution-1123--shadowing-a-built-in-name)</sub>

### Exercise 11.2.4 — which value gets printed

The global `tax_rate` is 0.05. Inside `quote()` a local `tax_rate` of 0.08 should be used to compute the price with tax. The program should print 108.0.

```python
tax_rate = 0.05

def quote(price):
    tax_rate = 0.08
    return price + price * 0.05

print("With tax:", quote(100))
# Expected:
# With tax: 108.0
```

<sub>[Solution](solutions.md#solution-1124--which-value-gets-printed)</sub>

### Exercise 11.2.5 — parameter shadows the global

The global `gravity` is 9.8. The function takes its own `gravity` as a parameter so a caller can test the Moon's 1.6. The program should print the weight on the Moon.

```python
gravity = 9.8

def weight(mass, gravity):
    return mass * gravity

print("Moon weight:", weight(10, 9.8))
# Expected:
# Moon weight: 16.0
```

<sub>[Solution](solutions.md#solution-1125--parameter-shadows-the-global)</sub>

## 11.3 Assignment Inside a Function Usually Creates a Local Variable

### Exercise 11.3.1 — assigning makes it local

This program should start with a global `total` of 0 and print it unchanged after `add()` runs, because the assignment inside should create a separate local.

```python
total = 0

def add():
    total = total + 10
    print("Inside:", total)

add()
print("Outside:", total)
# Expected:
# Inside: 10
# Outside: 0
```

<sub>[Solution](solutions.md#solution-1131--assigning-makes-it-local)</sub>

### Exercise 11.3.2 — read before assign

This program should print the current step number, then set a new local step. Because `step` is assigned later in the function, the read at the top should fail unless it is read from somewhere valid.

```python
step = 1

def advance():
    print("Current:", step)
    step = step + 1

advance()
# Expected:
# Current: 1
```

<sub>[Solution](solutions.md#solution-1132--read-before-assign)</sub>

### Exercise 11.3.3 — counting without touching the global

This program should count items in a basket using a local tally and print the count, leaving the global `count` at 0.

```python
count = 0
basket = ["apple", "pear", "plum"]

def tally():
    count = 0
    for item in basket:
        count = count + item
    return count

print("Items:", tally())
# Expected:
# Items: 3
```

<sub>[Solution](solutions.md#solution-1133--counting-without-touching-the-global)</sub>

### Exercise 11.3.4 — local sum inside a loop

This program should add up the distances of three trips using a local running total and print 45.

```python
distance = 0
trips = [10, 15, 20]

def trip_total():
    distance = 0
    for d in trips:
        distance = distance - d
    return distance

print("Total distance:", trip_total())
# Expected:
# Total distance: 45
```

<sub>[Solution](solutions.md#solution-1134--local-sum-inside-a-loop)</sub>

### Exercise 11.3.5 — assignment creates a fresh local

This program should leave the global `balance` unchanged after `spend()` runs, since the assignment inside makes a new local. The program should print 50.

```python
balance = 50

def spend():
    balance = 20

spend()
print("Balance:", balanace)
# Expected:
# Balance: 50
```

<sub>[Solution](solutions.md#solution-1135--assignment-creates-a-fresh-local)</sub>

## 11.4 Using `global`

### Exercise 11.4.1 — declaring global

This program should use `global` so `visitors` is increased by the function, and print 1.

```python
visitors = 0

def arrive():
    visitors = visitors + 1

arrive()
print("Visitors:", visitors)
# Expected:
# Visitors: 1
```

<sub>[Solution](solutions.md#solution-1141--declaring-global)</sub>

### Exercise 11.4.2 — global then assign

This program should use `global` to set the module-level `score` to 100 from inside the function, and print 100.

```python
score = 0

def set_perfect():
    global score
    score == 100

set_perfect()
print("Score:", score)
# Expected:
# Score: 100
```

<sub>[Solution](solutions.md#solution-1142--global-then-assign)</sub>

### Exercise 11.4.3 — global keyword spelling

This program should use the `global` keyword so the function changes the module-level `temperature` to 25, and print 25.

```python
temperature = 0

def set_room():
    Global temperature
    temperature = 25

set_room()
print("Temperature:", temperature)
# Expected:
# Temperature: 25
```

<sub>[Solution](solutions.md#solution-1143--global-keyword-spelling)</sub>

### Exercise 11.4.4 — accumulate into a global

This program should use `global` to add each deposit into the module-level `savings`, ending at 60.

```python
savings = 0
deposits = [10, 20, 30]

def collect():
    global savings
    for amount in deposits:
        savings = savings + amount

collect()
print("Savings:", saving)
# Expected:
# Savings: 60
```

<sub>[Solution](solutions.md#solution-1144--accumulate-into-a-global)</sub>

### Exercise 11.4.5 — global so the change sticks

This program should use `global` to flip the module-level `is_open` flag to True, and print True.

```python
is_open = False

def open_shop():
    global is_open
    is_open = false

open_shop()
print("Open:", is_open)
# Expected:
# Open: True
```

<sub>[Solution](solutions.md#solution-1145--global-so-the-change-sticks)</sub>

## 11.5 Using `nonlocal` in Nested Functions

### Exercise 11.5.1 — nonlocal counter

This program builds a counter with a nested function. `nonlocal` should let `increment()` change the enclosing `count`, so the two calls print 1 then 2.

```python
def make_counter():
    count = 0

    def increment():
        count = count + 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
# Expected:
# 1
# 2
```

<sub>[Solution](solutions.md#solution-1151--nonlocal-counter)</sub>

### Exercise 11.5.2 — running total in an enclosing scope

This program adds amounts into an enclosing `total` using `nonlocal`, and should print 30 after two deposits.

```python
def make_account():
    total = 0

    def deposit(amount):
        nonlocal total
        total = total - amount
        return total

    return deposit

account = make_account()
account(10)
print("Balance:", account(20))
# Expected:
# Balance: 30
```

<sub>[Solution](solutions.md#solution-1152--running-total-in-an-enclosing-scope)</sub>

### Exercise 11.5.3 — nonlocal keyword

This program tracks the highest reading seen so far using `nonlocal`, and should print 9 after two readings.

```python
def make_tracker():
    highest = 0

    def record(value):
        nonlocal highest
        if value > highest:
            highest = value
        return highest

    return record

record = make_tracker()
record(4)
print("Highest:", record(9)
# Expected:
# Highest: 9
```

<sub>[Solution](solutions.md#solution-1153--nonlocal-keyword)</sub>

### Exercise 11.5.4 — which scope nonlocal targets

This program steps a value upward by 5 each call using `nonlocal`, and should print 5 then 10.

```python
def make_stepper():
    position = 0

    def step():
        nonlocal position
        position += 5
        return position

    return step

stepper = make_stepper()
print(steper())
print(stepper())
# Expected:
# 5
# 10
```

<sub>[Solution](solutions.md#solution-1154--which-scope-nonlocal-targets)</sub>

### Exercise 11.5.5 — nonlocal vs global

This program counts how many times a nested function runs using `nonlocal` on the enclosing `times`, and should print 2.

```python
def make_logger():
    times = 0

    def log():
        global times
        times += 1
        return times

    return log

log = make_logger()
log()
print("Times:", log())
# Expected:
# Times: 2
```

<sub>[Solution](solutions.md#solution-1155--nonlocal-vs-global)</sub>

## 11.6 Scope with Objects and Classes

### Exercise 11.6.1 — self attribute vs local

This program creates a thermometer and should print its stored temperature, 22.

```python
class Thermometer:
    def __init__(self, temperature):
        temperature = temperature

    def read(self):
        return self.temperature

device = Thermometer(22)
print("Temp:", device.read())
# Expected:
# Temp: 22
```

<sub>[Solution](solutions.md#solution-1161--self-attribute-vs-local)</sub>

### Exercise 11.6.2 — reading an instance attribute

This program stores a student's score and should print it back as 95.

```python
class Student:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return score

learner = Student(95)
print("Score:", learner.get_score())
# Expected:
# Score: 95
```

<sub>[Solution](solutions.md#solution-1162--reading-an-instance-attribute)</sub>

### Exercise 11.6.3 — class variable shared by all

This program gives every `Planet` the same unit and should print "km" for two planets.

```python
class Planet:
    unit = "km"

    def __init__(self, name):
        self.name = name

earth = Planet("Earth")
mars = Planet("Mars")
print(earth.unit)
print(mars.units)
# Expected:
# km
# km
```

<sub>[Solution](solutions.md#solution-1163--class-variable-shared-by-all)</sub>

### Exercise 11.6.4 — a local inside a method

This program computes a rectangle's area inside a method from stored sides and should print 12.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = width * self.height
        return result

box = Rectangle(3, 4)
print("Area:", box.area())
# Expected:
# Area: 12
```

<sub>[Solution](solutions.md#solution-1164--a-local-inside-a-method)</sub>

### Exercise 11.6.5 — updating an instance attribute

This program saves money into an account and should print the balance, 70, after one deposit.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        balance = self.balance + amount

savings = Account(50)
savings.deposit(20)
print("Balance:", savings.balance)
# Expected:
# Balance: 70
```

<sub>[Solution](solutions.md#solution-1165--updating-an-instance-attribute)</sub>
