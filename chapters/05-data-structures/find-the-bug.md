# Chapter 5 — Data Structures: Find the Bug

Part III · Data and Operations — *Everyday Programming*

Each program below works with a data structure — ints, floats, bools, strings, `None`, lists, tuples, sets, or dictionaries — and every one hides exactly one bug; read each carefully and find the single mistake.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**50 exercises in 10 sections.**

## 5.1 `int`

### Exercise 5.1.1 — Total points

A quiz has 3 sections worth 20, 30, and 25 points. The program should print the total, 75.

```python
section1 = 20
section2 = 30
section3 = 25

total = section1 + section2 - section3
print(total)   # 75
```

<sub>[Solution](solutions.md#solution-511--total-points)</sub>

### Exercise 5.1.2 — Students per team

Thirty students are split evenly into 5 teams. The program should print the whole number 6.

```python
students = 30
teams = 5

per_team = students / teams
print(per_team)   # 6
```

<sub>[Solution](solutions.md#solution-512--students-per-team)</sub>

### Exercise 5.1.3 — Seconds in an hour

There are 60 seconds in a minute and 60 minutes in an hour. The program should print 3600.

```python
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute + minutes_per_hour
print(seconds_per_hour)   # 3600
```

<sub>[Solution](solutions.md#solution-513--seconds-in-an-hour)</sub>

### Exercise 5.1.4 — Counting by tens

The program should add 10 to a starting count and print 110.

```python
count = 100
count = count + "10"
print(count)   # 110
```

<sub>[Solution](solutions.md#solution-514--counting-by-tens)</sub>

### Exercise 5.1.5 — Apples per box

You have 17 apples and want 5 per box. The program should print how many full boxes (3) you can fill.

```python
apples = 17
per_box = 5

full_boxes = apples % per_box
print(full_boxes)   # 3
```

<sub>[Solution](solutions.md#solution-515--apples-per-box)</sub>

## 5.2 `float`

### Exercise 5.2.1 — Average temperature

Three readings are 20.0, 22.0, and 24.0 degrees. The program should print the average, 22.0.

```python
reading1 = 20.0
reading2 = 22.0
reading3 = 24.0

average = reading1 + reading2 + reading3 / 3
print(average)   # 22.0
```

<sub>[Solution](solutions.md#solution-521--average-temperature)</sub>

### Exercise 5.2.2 — Splitting a bill

A 50-dollar bill is split between 4 people. The program should print 12.5.

```python
bill = 50
people = 4

each = bill // people
print(each)   # 12.5
```

<sub>[Solution](solutions.md#solution-522--splitting-a-bill)</sub>

### Exercise 5.2.3 — Rounding a price

A price of 3.14159 dollars should be rounded to 2 decimal places, printing 3.14.

```python
price = 3.14159
rounded = round(price)
print(rounded)   # 3.14
```

<sub>[Solution](solutions.md#solution-523--rounding-a-price)</sub>

### Exercise 5.2.4 — Half of a measurement

A board is 9.0 meters long. The program should print half its length, 4.5.

```python
length = 9.0
half = length / 2
print(half   # 4.5
```

<sub>[Solution](solutions.md#solution-524--half-of-a-measurement)</sub>

### Exercise 5.2.5 — Celsius to Fahrenheit

The program converts 100.0 degrees Celsius to Fahrenheit and should print 212.0.

```python
celsius = 100.0
fahrenheit = celsius * 9 / 5 - 32
print(fahrenheit)   # 212.0
```

<sub>[Solution](solutions.md#solution-525--celsius-to-fahrenheit)</sub>

## 5.3 `bool`

### Exercise 5.3.1 — Is it freezing?

Water freezes at 0 degrees Celsius. The program should report `True` when the temperature is below freezing. With temp = -5 it should print True.

```python
temp = -5
is_freezing = temp > 0
print(is_freezing)   # True
```

<sub>[Solution](solutions.md#solution-531--is-it-freezing)</sub>

### Exercise 5.3.2 — Passing grade

A grade of 60 or more passes. With a grade of 72, the program should print `True`.

```python
grade = 72
passed = grade >= 60
print(Passed)   # True
```

<sub>[Solution](solutions.md#solution-532--passing-grade)</sub>

### Exercise 5.3.3 — Both lights on

A room is "ready" only if both lights are on. The program should print `False` here, since one light is off.

```python
light1_on = True
light2_on = False

ready = light1_on or light2_on
print(ready)   # False
```

<sub>[Solution](solutions.md#solution-533--both-lights-on)</sub>

### Exercise 5.3.4 — Empty cart

A cart is empty when it has 0 items. The program should print `True`.

```python
items = 0
is_empty = items = 0
print(is_empty)   # True
```

<sub>[Solution](solutions.md#solution-534--empty-cart)</sub>

### Exercise 5.3.5 — Within speed limit

The limit is 65. A car going 60 is within the limit, so the program should print `True`.

```python
speed = 60
limit = 65

within_limit = speed > limit
print(within_limit)   # True
```

<sub>[Solution](solutions.md#solution-535--within-speed-limit)</sub>

## 5.4 Strings

### Exercise 5.4.1 — First letter

The program should print the first letter of a city name: T.

```python
city = "Tokyo"
first = city[1]
print(first)   # T
```

<sub>[Solution](solutions.md#solution-541--first-letter)</sub>

### Exercise 5.4.2 — Shouting

The program should print a greeting in all capitals: HELLO.

```python
word = "hello"
loud = word.upper
print(loud)   # HELLO
```

<sub>[Solution](solutions.md#solution-542--shouting)</sub>

### Exercise 5.4.3 — Full name

The program should join a first and last name with a space: "Maya Singh".

```python
first = "Maya"
last = "Singh"

full = first + last
print(full)   # Maya Singh
```

<sub>[Solution](solutions.md#solution-543--full-name)</sub>

### Exercise 5.4.4 — Length of a word

The program should print the number of letters in "science": 7.

```python
word = "science"
count = len(word())
print(count)   # 7
```

<sub>[Solution](solutions.md#solution-544--length-of-a-word)</sub>

### Exercise 5.4.5 — Last three characters

The program should print the last three characters of a code: "789".

```python
code = "ABC789"
last_three = code[-3]
print(last_three)   # 789
```

<sub>[Solution](solutions.md#solution-545--last-three-characters)</sub>

## 5.5 `None`

### Exercise 5.5.1 — No reading yet

A sensor has no reading. The program should print `True` because the reading is `None`.

```python
reading = None
no_data = reading == "None"
print(no_data)   # True
```

<sub>[Solution](solutions.md#solution-551--no-reading-yet)</sub>

### Exercise 5.5.2 — Default color

The function should return a default color when none is given. Calling it with nothing should print "blue".

```python
def choose_color(color):
    if color is None:
        color = "blue"

print(choose_color(None))   # blue
```

<sub>[Solution](solutions.md#solution-552--default-color)</sub>

### Exercise 5.5.3 — Checking for a value

When a value is `None`, the program should print "missing".

```python
favorite = None

if favorite is not None:
    print("missing")
else:
    print("has value")
# expected: missing
```

<sub>[Solution](solutions.md#solution-553--checking-for-a-value)</sub>

### Exercise 5.5.4 — Length of nothing

A list of temperatures has not been filled in yet, so it is `None`. The program tries to count it and should instead detect the missing list and print 0.

```python
temps = None
count = len(temps)
print(count)   # 0
```

<sub>[Solution](solutions.md#solution-554--length-of-nothing)</sub>

### Exercise 5.5.5 — Comparing to None

The program should check whether a username has been set, printing `True` when it is still `None`.

```python
username = None
not_set = username is None
print(Not_set)   # True
```

<sub>[Solution](solutions.md#solution-555--comparing-to-none)</sub>

## 5.6 Lists

### Exercise 5.6.1 — First fruit

The program should print the first fruit in the list: "apple".

```python
fruits = ["apple", "banana", "orange"]
print(fruits[1])   # apple
```

<sub>[Solution](solutions.md#solution-561--first-fruit)</sub>

### Exercise 5.6.2 — Adding an item

The program should add "grape" to the list and print 4 items in total.

```python
fruits = ["apple", "banana", "orange"]
fruits.add("grape")
print(len(fruits))   # 4
```

<sub>[Solution](solutions.md#solution-562--adding-an-item)</sub>

### Exercise 5.6.3 — Last score

The program should print the last score in the list: 88.

```python
scores = [70, 95, 88]
print(scores[3])   # 88
```

<sub>[Solution](solutions.md#solution-563--last-score)</sub>

### Exercise 5.6.4 — Changing a value

The program should change the second price to 5.0 and print the list.

```python
prices = [2.0, 3.0, 4.0]
prices(1) = 5.0
print(prices)   # [2.0, 5.0, 4.0]
```

<sub>[Solution](solutions.md#solution-564--changing-a-value)</sub>

### Exercise 5.6.5 — How many items

The program should print how many items are in the shopping list: 3.

```python
shopping = ["milk", "eggs", "bread"]
count = len(shopping) - 1
print(count)   # 3
```

<sub>[Solution](solutions.md#solution-565--how-many-items)</sub>

## 5.7 Tuples

### Exercise 5.7.1 — Map coordinates

A location is stored as a (latitude, longitude) tuple. The program should print the latitude, 41.8781.

```python
location = (41.8781, -87.6298)
print(location[1])   # 41.8781
```

<sub>[Solution](solutions.md#solution-571--map-coordinates)</sub>

### Exercise 5.7.2 — A fixed pair

This program should change the width to 1280 and print `(1280, 1080)`.

```python
size = (1920, 1080)
size[0] = 1280
print(size)   # expected: (1280, 1080)
```

<sub>[Solution](solutions.md#solution-572--a-fixed-pair)</sub>

### Exercise 5.7.3 — Unpacking coordinates

The program should unpack a tuple into two variables and print "lat 35.7, lon 139.7".

```python
coords = (35.7, 139.7)
lat = coords
lon = coords
print(f"lat {lat}, lon {lon}")   # lat 35.7, lon 139.7
```

<sub>[Solution](solutions.md#solution-573--unpacking-coordinates)</sub>

### Exercise 5.7.4 — A single value

The program should make a one-element tuple holding the number 42 and print its length, 1.

```python
single = (42)
print(len(single))   # 1
```

<sub>[Solution](solutions.md#solution-574--a-single-value)</sub>

### Exercise 5.7.5 — Days in a tuple

A tuple holds three weekday names. The program should print the second one, "Tue".

```python
days = ("Mon", "Tue", "Wed")
print(days[2])   # Tue
```

<sub>[Solution](solutions.md#solution-575--days-in-a-tuple)</sub>

## 5.8 Sets

### Exercise 5.8.1 — Unique colors

A set removes duplicates. The program should print how many unique colors there are: 3.

```python
colors = ["red", "blue", "red", "green"]
print(len(colors))   # 3
```

<sub>[Solution](solutions.md#solution-581--unique-colors)</sub>

### Exercise 5.8.2 — Adding a member

The program should add "Sydney" to the set of cities and print 4 members in total.

```python
cities = {"New York", "London", "Tokyo"}
cities.append("Sydney")
print(len(cities))   # 4
```

<sub>[Solution](solutions.md#solution-582--adding-a-member)</sub>

### Exercise 5.8.3 — Is it a member?

The program should check whether "blue" is in the set and print `True`.

```python
colors = {"red", "blue", "green"}
print("yellow" in colors)   # True
```

<sub>[Solution](solutions.md#solution-583--is-it-a-member)</sub>

### Exercise 5.8.4 — Shared subjects

Two students list their subjects. The program should print the subjects they share: {"math"}.

```python
maya = {"math", "science", "art"}
leo = {"math", "history"}

shared = maya | leo
print(shared)   # {'math'}
```

<sub>[Solution](solutions.md#solution-584--shared-subjects)</sub>

### Exercise 5.8.5 — Building a set

The program should start with an empty set, add one item, and print the set with that item.

```python
seen = {}
seen.add("apple")
print(seen)   # {'apple'}
```

<sub>[Solution](solutions.md#solution-585--building-a-set)</sub>

## 5.9 Dictionaries

### Exercise 5.9.1 — Looking up a name

A student record stores a name. The program should print "Maya".

```python
student = {"name": "Maya", "grade": 10}
print(student["Name"])   # Maya
```

<sub>[Solution](solutions.md#solution-591--looking-up-a-name)</sub>

### Exercise 5.9.2 — Updating a grade

The program should change the grade to 11 and print 11.

```python
student = {"name": "Maya", "grade": 10}
student("grade") = 11
print(student["grade"])   # 11
```

<sub>[Solution](solutions.md#solution-592--updating-a-grade)</sub>

### Exercise 5.9.3 — Missing key

The program should safely look up a missing subject and print "not found" instead of crashing.

```python
student = {"name": "Maya", "grade": 10}
subject = student["favorite_subject"]
print(subject)   # not found
```

<sub>[Solution](solutions.md#solution-593--missing-key)</sub>

### Exercise 5.9.4 — Safe default with get

Using `.get`, the program should print "science" when the key exists.

```python
student = {"favorite_subject": "science"}
subject = student.get("favorite_subject", "unknown")
print(Subject)   # science
```

<sub>[Solution](solutions.md#solution-594--safe-default-with-get)</sub>

### Exercise 5.9.5 — Adding an entry

The program should add a phone number to the contact and print it.

```python
contact = {"name": "Leo"}
contact["phone"] == "555-0100"
print(contact["phone"])   # 555-0100
```

<sub>[Solution](solutions.md#solution-595--adding-an-entry)</sub>

## 5.10 Variables and Types

### Exercise 5.10.1 — Reading a number

Input arrives as text. The program should turn "25" into a number and print 30 after adding 5.

```python
age_text = "25"
age = age_text + 5
print(age)   # 30
```

<sub>[Solution](solutions.md#solution-5101--reading-a-number)</sub>

### Exercise 5.10.2 — Building a message

The program should combine a label and a number into one sentence: "Score: 90".

```python
score = 90
message = "Score: " + score
print(message)   # Score: 90
```

<sub>[Solution](solutions.md#solution-5102--building-a-message)</sub>

### Exercise 5.10.3 — Checking a type

The program should report the type of a price as `float`.

```python
price = 3.99
print(type(price))   # <class 'float'>
print(type(price) == int)   # expected: True
```

<sub>[Solution](solutions.md#solution-5103--checking-a-type)</sub>

### Exercise 5.10.4 — Converting to float

The program should turn the text "2.5" into a float and print double it, 5.0.

```python
weight_text = "2.5"
weight = int(weight_text)
print(weight * 2)   # 5.0
```

<sub>[Solution](solutions.md#solution-5104--converting-to-float)</sub>

### Exercise 5.10.5 — Whole-number average

Two test scores are 80 and 91. The program should print their average as a whole number, 85.

```python
score1 = 80
score2 = 91

average = str((score1 + score2) / 2)
print(int(average))   # 85
```

<sub>[Solution](solutions.md#solution-5105--whole-number-average)</sub>
