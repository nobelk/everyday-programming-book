# Chapter 14 — Objects: Find the Bug

Part V · Building Programs — *Everyday Programming*

These exercises cover objects in Python — classes, instance versus class data, duck typing, lists, and copying lists — and each program below contains exactly one bug for you to find and fix.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**25 exercises in 5 sections.**

## 14.1 Classes

### Exercise 14.1.1 — Defining a class

This class should store a rectangle's width and height and report its area.

```python
class Rectangle:
    def __init__(self, width, height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

room = Rectangle(4, 3)
print(room.area())   # 12
```

<sub>[Solution](solutions.md#solution-1411--defining-a-class)</sub>

### Exercise 14.1.2 — Using self

This class converts a Celsius reading to Fahrenheit.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return celsius * 9 / 5 + 32

reading = Temperature(100)
print(reading.to_fahrenheit())   # 212.0
```

<sub>[Solution](solutions.md#solution-1412--using-self)</sub>

### Exercise 14.1.3 — Storing an attribute

This class records a student's name and quiz score, then prints a summary.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def summary(self):
        return f"{self.name} scored {self.grade}"

learner = Student("Ava", 88)
print(learner.summary())   # Ava scored 88
```

<sub>[Solution](solutions.md#solution-1413--storing-an-attribute)</sub>

### Exercise 14.1.4 — Calling a method

This class models a savings account and adds interest to the balance.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self, rate):
        self.balance = self.balance + self.balance * rate

savings = Account(1000)
Account.add_interest(0.05)
print(savings.balance)   # 1050.0
```

<sub>[Solution](solutions.md#solution-1414--calling-a-method)</sub>

### Exercise 14.1.5 — Method calls need parentheses

This class stores a circle's radius and returns its circumference.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

wheel = Circle(10)
print(wheel.circumference)   # 62.8318
```

<sub>[Solution](solutions.md#solution-1415--method-calls-need-parentheses)</sub>

## 14.2 Instance Data vs Class Data

### Exercise 14.2.1 — Instance vs class attribute

Every planet shares the same gravity unit, but each has its own mass. This program should print each planet's name and the shared unit.

```python
class Planet:
    gravity_unit = "m/s^2"

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

earth = Planet("Earth", 5.97e24)
mars = Planet("Mars", 6.42e23)

print(earth.name, earth.gravity_unit)   # Earth m/s^2
print(mars.name, mars.gravity_unit)     # Mars m/s^2
print(earth.unit)                       # m/s^2
```

<sub>[Solution](solutions.md#solution-1421--instance-vs-class-attribute)</sub>

### Exercise 14.2.2 — Shared mutable class attribute

Each runner should keep a private list of lap times, but every runner ends up sharing one list.

```python
class Runner:
    laps = []

    def __init__(self, name):
        self.name = name

    def record(self, seconds):
        self.laps.append(seconds)

amir = Runner("Amir")
beth = Runner("Beth")
amir.record(58)
beth.record(61)
print(amir.laps)   # [58]
print(beth.laps)   # [61]
```

<sub>[Solution](solutions.md#solution-1422--shared-mutable-class-attribute)</sub>

### Exercise 14.2.3 — Updating a class counter

A class attribute should count how many books have been created.

```python
class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        self.count = self.count + 1

Book("Algebra")
Book("Biology")
Book("Chemistry")
print(Book.count)   # 3
```

<sub>[Solution](solutions.md#solution-1423--updating-a-class-counter)</sub>

### Exercise 14.2.4 — Instance overriding shared default

Every thermostat shares a default target, but the kitchen is set warmer for itself only. The bedroom should keep the shared default.

```python
class Thermostat:
    target_c = 20

    def __init__(self, room):
        self.room = room

kitchen = Thermostat("kitchen")
bedroom = Thermostat("bedroom")
Thermostat.target_c = 22

print(kitchen.target_c)   # 22
print(bedroom.target_c)   # 20
```

<sub>[Solution](solutions.md#solution-1424--instance-overriding-shared-default)</sub>

### Exercise 14.2.5 — Reading a class constant

The class stores a fixed sales-tax rate shared by all carts; each cart has its own subtotal. The total should add the tax.

```python
class Cart:
    tax_rate = 0.08

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def total(self):
        return self.subtotal + self.subtotal / self.tax_rate

groceries = Cart(50.0)
print(groceries.total())   # 54.0
```

<sub>[Solution](solutions.md#solution-1425--reading-a-class-constant)</sub>

## 14.3 Duck Typing

### Exercise 14.3.1 — Relying on a shared method

Different shapes each provide an `area()` method, so one function can total them all.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

def total_area(shapes):
    total = 0
    for shape in shapes:
        total = total + shape.area
    return total

print(total_area([Square(4), Triangle(6, 3)]))   # 25.0
```

<sub>[Solution](solutions.md#solution-1431--relying-on-a-shared-method)</sub>

### Exercise 14.3.2 — Same behavior, different types

Any object that can `speak()` can be greeted, regardless of its class.

```python
class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

def greet(animal):
    print("The animal says:", animal.speka())

greet(Cat())
greet(Cow())   # The animal says: Moo
```

<sub>[Solution](solutions.md#solution-1432--same-behavior-different-types)</sub>

### Exercise 14.3.3 — Behavior over type

A function should work with anything that has a `length` attribute.

```python
class Field:
    def __init__(self, length):
        self.length = length

class Pool:
    def __init__(self, length):
        self.length = length

def meters_of(thing):
    return thing.size

print(meters_of(Field(100)))   # 100
print(meters_of(Pool(25)))     # 25
```

<sub>[Solution](solutions.md#solution-1433--behavior-over-type)</sub>

### Exercise 14.3.4 — Duck typing a method call

Different timers each provide `tick()`, so one loop can advance them all.

```python
class Stopwatch:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds = self.seconds + 1

class Metronome:
    def __init__(self):
        self.beats = 0

    def tick(self):
        self.beats = self.beats + 1

def advance(devices):
    for device in devices:
        device.tick

watch = Stopwatch()
advance([watch])
print(watch.seconds)   # 1
```

<sub>[Solution](solutions.md#solution-1434--duck-typing-a-method-call)</sub>

### Exercise 14.3.5 — Trusting the interface

Any sensor that provides a `read()` method can be sampled.

```python
class TempSensor:
    def read(self):
        return 21.5

class HumiditySensor:
    def read(self):
        return 48.0

def sample(sensor):
    return sensor.read

print(sample(TempSensor()))       # 21.5
print(sample(HumiditySensor()))   # 48.0
```

<sub>[Solution](solutions.md#solution-1435--trusting-the-interface)</sub>
