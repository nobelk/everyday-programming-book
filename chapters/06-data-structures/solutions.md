# Chapter 6 — Data Structures: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 5.1 `int`

### Solution 6.1.1 — Total points

**Bug type:** Logical

The third section was subtracted instead of added, giving 25 instead of 75. Change the `-` to `+` so all three sections are summed.

```python
section1 = 20
section2 = 30
section3 = 25

total = section1 + section2 + section3
print(total)   # 75
```

<sub>[Exercise](find-the-bug.md#exercise-511--total-points) · [Runnable file](code/find_the_bug/ex_05_01_01_total_points.py)</sub>

### Solution 6.1.2 — Students per team

**Bug type:** Logical

The `/` operator always produces a float (6.0), but a whole number of students per team is wanted. Use integer division `//` to get the int 6.

```python
students = 30
teams = 5

per_team = students // teams
print(per_team)   # 6
```

<sub>[Exercise](find-the-bug.md#exercise-512--students-per-team) · [Runnable file](code/find_the_bug/ex_05_01_02_students_per_team.py)</sub>

### Solution 6.1.3 — Seconds in an hour

**Bug type:** Logical

The two counts must be multiplied, not added; `60 + 60` gives 120, not 3600. Use `*`.

```python
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)   # 3600
```

<sub>[Exercise](find-the-bug.md#exercise-513--seconds-in-an-hour) · [Runnable file](code/find_the_bug/ex_05_01_03_seconds_in_an_hour.py)</sub>

### Solution 6.1.4 — Counting by tens

**Bug type:** Runtime

`"10"` is a string, so `count + "10"` raises a `TypeError` (you cannot add an int and a str). Use the int literal `10`.

```python
count = 100
count = count + 10
print(count)   # 110
```

<sub>[Exercise](find-the-bug.md#exercise-514--counting-by-tens) · [Runnable file](code/find_the_bug/ex_05_01_04_counting_by_tens.py)</sub>

### Solution 6.1.5 — Apples per box

**Bug type:** Logical

`%` gives the remainder (2 leftover apples), not the number of full boxes. Use integer division `//` to get 3.

```python
apples = 17
per_box = 5

full_boxes = apples // per_box
print(full_boxes)   # 3
```

<sub>[Exercise](find-the-bug.md#exercise-515--apples-per-box) · [Runnable file](code/find_the_bug/ex_05_01_05_apples_per_box.py)</sub>

## 5.2 `float`

### Solution 6.2.1 — Average temperature

**Bug type:** Logical

Without parentheses, only `reading3 / 3` is divided (operator precedence), so the sum is wrong. Wrap the addition in parentheses before dividing.

```python
reading1 = 20.0
reading2 = 22.0
reading3 = 24.0

average = (reading1 + reading2 + reading3) / 3
print(average)   # 22.0
```

<sub>[Exercise](find-the-bug.md#exercise-521--average-temperature) · [Runnable file](code/find_the_bug/ex_05_02_01_average_temperature.py)</sub>

### Solution 6.2.2 — Splitting a bill

**Bug type:** Logical

`//` discards the fractional part, giving 12 instead of 12.5. Use true division `/` so the result is a float.

```python
bill = 50
people = 4

each = bill / people
print(each)   # 12.5
```

<sub>[Exercise](find-the-bug.md#exercise-522--splitting-a-bill) · [Runnable file](code/find_the_bug/ex_05_02_02_splitting_a_bill.py)</sub>

### Solution 6.2.3 — Rounding a price

**Bug type:** Logical

`round(price)` with no second argument rounds to a whole number (3). Pass `2` to round to two decimal places.

```python
price = 3.14159
rounded = round(price, 2)
print(rounded)   # 3.14
```

<sub>[Exercise](find-the-bug.md#exercise-523--rounding-a-price) · [Runnable file](code/find_the_bug/ex_05_02_03_rounding_a_price.py)</sub>

### Solution 6.2.4 — Half of a measurement

**Bug type:** Syntax

The closing parenthesis of `print(...)` is missing, so the program will not parse. Add the `)` after `half`.

```python
length = 9.0
half = length / 2
print(half)   # 4.5
```

<sub>[Exercise](find-the-bug.md#exercise-524--half-of-a-measurement) · [Runnable file](code/find_the_bug/ex_05_02_04_half_of_a_measurement.py)</sub>

### Solution 6.2.5 — Celsius to Fahrenheit

**Bug type:** Logical

Operator precedence makes `celsius * 9 / 5 - 32` subtract 32 instead of adding it, and the +32 must come after the multiply/divide. Add parentheses or use `+ 32`: the formula is `celsius * 9 / 5 + 32`.

```python
celsius = 100.0
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)   # 212.0
```

<sub>[Exercise](find-the-bug.md#exercise-525--celsius-to-fahrenheit) · [Runnable file](code/find_the_bug/ex_05_02_05_celsius_to_fahrenheit.py)</sub>

## 5.3 `bool`

### Solution 6.3.1 — Is it freezing?

**Bug type:** Logical

"Below freezing" means less than 0, but the test used `>`, which is False for -5. Use `<` so the comparison returns True.

```python
temp = -5
is_freezing = temp < 0
print(is_freezing)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-531--is-it-freezing) · [Runnable file](code/find_the_bug/ex_05_03_01_is_it_freezing.py)</sub>

### Solution 6.3.2 — Passing grade

**Bug type:** Runtime

`Passed` (capital P) is a different, undefined name, so printing it raises a `NameError`. Print the variable `passed`.

```python
grade = 72
passed = grade >= 60
print(passed)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-532--passing-grade) · [Runnable file](code/find_the_bug/ex_05_03_02_passing_grade.py)</sub>

### Solution 6.3.3 — Both lights on

**Bug type:** Logical

"Both" requires `and`; `or` is True when either light is on. Use `and` so the result is False here.

```python
light1_on = True
light2_on = False

ready = light1_on and light2_on
print(ready)   # False
```

<sub>[Exercise](find-the-bug.md#exercise-533--both-lights-on) · [Runnable file](code/find_the_bug/ex_05_03_03_both_lights_on.py)</sub>

### Solution 6.3.4 — Empty cart

**Bug type:** Logical

`is_empty = items = 0` is a chained assignment that sets `is_empty` to `0`, not the comparison you intended; it runs but prints `0`. Comparing values needs `==`, so write `is_empty = items == 0`.

```python
items = 0
is_empty = items == 0
print(is_empty)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-534--empty-cart) · [Runnable file](code/find_the_bug/ex_05_03_04_empty_cart.py)</sub>

### Solution 6.3.5 — Within speed limit

**Bug type:** Logical

Being within the limit means the speed is at or below it, but `>` tests the opposite. Use `<=` so 60 within 65 gives True.

```python
speed = 60
limit = 65

within_limit = speed <= limit
print(within_limit)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-535--within-speed-limit) · [Runnable file](code/find_the_bug/ex_05_03_05_within_speed_limit.py)</sub>

## 5.4 Strings

### Solution 6.4.1 — First letter

**Bug type:** Logical

String indexing starts at 0, so `city[1]` is the second letter ("o"). Use index `0` for the first letter.

```python
city = "Tokyo"
first = city[0]
print(first)   # T
```

<sub>[Exercise](find-the-bug.md#exercise-541--first-letter) · [Runnable file](code/find_the_bug/ex_05_04_01_first_letter.py)</sub>

### Solution 6.4.2 — Shouting

**Bug type:** Logical

`word.upper` refers to the method without calling it, so it prints a method object, not the text. Add parentheses to call it: `word.upper()`.

```python
word = "hello"
loud = word.upper()
print(loud)   # HELLO
```

<sub>[Exercise](find-the-bug.md#exercise-542--shouting) · [Runnable file](code/find_the_bug/ex_05_04_02_shouting.py)</sub>

### Solution 6.4.3 — Full name

**Bug type:** Logical

Concatenation does not insert a space, so the result is "MayaSingh". Add a space string between the names.

```python
first = "Maya"
last = "Singh"

full = first + " " + last
print(full)   # Maya Singh
```

<sub>[Exercise](find-the-bug.md#exercise-543--full-name) · [Runnable file](code/find_the_bug/ex_05_04_03_full_name.py)</sub>

### Solution 6.4.4 — Length of a word

**Bug type:** Runtime

`word()` tries to call the string as if it were a function, raising a `TypeError`. Pass the string itself to `len`.

```python
word = "science"
count = len(word)
print(count)   # 7
```

<sub>[Exercise](find-the-bug.md#exercise-544--length-of-a-word) · [Runnable file](code/find_the_bug/ex_05_04_04_length_of_a_word.py)</sub>

### Solution 6.4.5 — Last three characters

**Bug type:** Logical

`code[-3]` is a single character ("7"), not the last three. Slice with `code[-3:]` to get "789".

```python
code = "ABC789"
last_three = code[-3:]
print(last_three)   # 789
```

<sub>[Exercise](find-the-bug.md#exercise-545--last-three-characters) · [Runnable file](code/find_the_bug/ex_05_04_05_last_three_characters.py)</sub>

## 5.5 `None`

### Solution 6.5.1 — No reading yet

**Bug type:** Logical

`None` is not the same as the string `"None"`, so the comparison is always False. Compare to the real `None` value with `is None`.

```python
reading = None
no_data = reading is None
print(no_data)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-551--no-reading-yet) · [Runnable file](code/find_the_bug/ex_05_05_01_no_reading_yet.py)</sub>

### Solution 6.5.2 — Default color

**Bug type:** Logical

The function changes `color` but never returns it, so it returns `None`. Add a `return color` statement.

```python
def choose_color(color):
    if color is None:
        color = "blue"
    return color

print(choose_color(None))   # blue
```

<sub>[Exercise](find-the-bug.md#exercise-552--default-color) · [Runnable file](code/find_the_bug/ex_05_05_02_default_color.py)</sub>

### Solution 6.5.3 — Checking for a value

**Bug type:** Logical

The test `is not None` is False when the value is `None`, so the program runs the wrong branch and prints "has value". Use `is None` so a `None` value prints "missing".

```python
favorite = None

if favorite is None:
    print("missing")
else:
    print("has value")
# expected: missing
```

<sub>[Exercise](find-the-bug.md#exercise-553--checking-for-a-value) · [Runnable file](code/find_the_bug/ex_05_05_03_checking_for_a_value.py)</sub>

### Solution 6.5.4 — Length of nothing

**Bug type:** Runtime

`len(None)` raises a `TypeError` because `None` has no length. Check for `None` first and use 0 in that case.

```python
temps = None
count = len(temps) if temps is not None else 0
print(count)   # 0
```

<sub>[Exercise](find-the-bug.md#exercise-554--length-of-nothing) · [Runnable file](code/find_the_bug/ex_05_05_04_length_of_nothing.py)</sub>

### Solution 6.5.5 — Comparing to None

**Bug type:** Runtime

`Not_set` (capital N) is undefined, so printing it raises a `NameError`. Print the variable `not_set`.

```python
username = None
not_set = username is None
print(not_set)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-555--comparing-to-none) · [Runnable file](code/find_the_bug/ex_05_05_05_comparing_to_none.py)</sub>

## 5.6 Lists

### Solution 6.6.1 — First fruit

**Bug type:** Logical

List indexing starts at 0, so `fruits[1]` is "banana". Use index `0` for the first fruit.

```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple
```

<sub>[Exercise](find-the-bug.md#exercise-561--first-fruit) · [Runnable file](code/find_the_bug/ex_05_06_01_first_fruit.py)</sub>

### Solution 6.6.2 — Adding an item

**Bug type:** Runtime

Lists have no `add` method, so this raises an `AttributeError`. Use `append` to add to a list.

```python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(len(fruits))   # 4
```

<sub>[Exercise](find-the-bug.md#exercise-562--adding-an-item) · [Runnable file](code/find_the_bug/ex_05_06_02_adding_an_item.py)</sub>

### Solution 6.6.3 — Last score

**Bug type:** Runtime

The list has indexes 0, 1, 2, so `scores[3]` is out of range and raises an `IndexError`. The last item is at index 2 (or use `-1`).

```python
scores = [70, 95, 88]
print(scores[-1])   # 88
```

<sub>[Exercise](find-the-bug.md#exercise-563--last-score) · [Runnable file](code/find_the_bug/ex_05_06_03_last_score.py)</sub>

### Solution 6.6.4 — Changing a value

**Bug type:** Syntax

Item assignment uses square brackets, not parentheses; `prices(1) = 5.0` is not valid Python. Use `prices[1] = 5.0`.

```python
prices = [2.0, 3.0, 4.0]
prices[1] = 5.0
print(prices)   # [2.0, 5.0, 4.0]
```

<sub>[Exercise](find-the-bug.md#exercise-564--changing-a-value) · [Runnable file](code/find_the_bug/ex_05_06_04_changing_a_value.py)</sub>

### Solution 6.6.5 — How many items

**Bug type:** Logical

`len(shopping)` already gives 3; subtracting 1 makes it 2. Remove the `- 1`.

```python
shopping = ["milk", "eggs", "bread"]
count = len(shopping)
print(count)   # 3
```

<sub>[Exercise](find-the-bug.md#exercise-565--how-many-items) · [Runnable file](code/find_the_bug/ex_05_06_05_how_many_items.py)</sub>

## 5.7 Tuples

### Solution 6.7.1 — Map coordinates

**Bug type:** Logical

Index 0 is the latitude; `location[1]` returns the longitude. Use index `0`.

```python
location = (41.8781, -87.6298)
print(location[0])   # 41.8781
```

<sub>[Exercise](find-the-bug.md#exercise-571--map-coordinates) · [Runnable file](code/find_the_bug/ex_05_07_01_map_coordinates.py)</sub>

### Solution 6.7.2 — A fixed pair

**Bug type:** Runtime

Tuples are immutable, so `size[0] = 1280` raises a `TypeError`. You cannot change one element in place; build a new tuple instead.

```python
size = (1920, 1080)
size = (1280, size[1])
print(size)   # (1280, 1080)
```

<sub>[Exercise](find-the-bug.md#exercise-572--a-fixed-pair) · [Runnable file](code/find_the_bug/ex_05_07_02_a_fixed_pair.py)</sub>

### Solution 6.7.3 — Unpacking coordinates

**Bug type:** Logical

Assigning the whole tuple to each name does not unpack it. Unpack both values at once with `lat, lon = coords`.

```python
coords = (35.7, 139.7)
lat, lon = coords
print(f"lat {lat}, lon {lon}")   # lat 35.7, lon 139.7
```

<sub>[Exercise](find-the-bug.md#exercise-573--unpacking-coordinates) · [Runnable file](code/find_the_bug/ex_05_07_03_unpacking_coordinates.py)</sub>

### Solution 6.7.4 — A single value

**Bug type:** Runtime

`(42)` is just the number 42 in parentheses, not a tuple, so `len(single)` raises a `TypeError` on an int. A one-element tuple needs a trailing comma: `(42,)`.

```python
single = (42,)
print(len(single))   # 1
```

<sub>[Exercise](find-the-bug.md#exercise-574--a-single-value) · [Runnable file](code/find_the_bug/ex_05_07_04_a_single_value.py)</sub>

### Solution 6.7.5 — Days in a tuple

**Bug type:** Logical

Index 1 is the second item ("Tue"); `days[2]` returns "Wed". Use index `1`.

```python
days = ("Mon", "Tue", "Wed")
print(days[1])   # Tue
```

<sub>[Exercise](find-the-bug.md#exercise-575--days-in-a-tuple) · [Runnable file](code/find_the_bug/ex_05_07_05_days_in_a_tuple.py)</sub>

## 5.8 Sets

### Solution 6.8.1 — Unique colors

**Bug type:** Logical

Square brackets create a list, which keeps the duplicate "red", so `len` is 4. Use curly braces to make a set, which drops duplicates and gives 3.

```python
colors = {"red", "blue", "red", "green"}
print(len(colors))   # 3
```

<sub>[Exercise](find-the-bug.md#exercise-581--unique-colors) · [Runnable file](code/find_the_bug/ex_05_08_01_unique_colors.py)</sub>

### Solution 6.8.2 — Adding a member

**Bug type:** Runtime

Sets have no `append` method, so this raises an `AttributeError`. Use `add` to put an item in a set.

```python
cities = {"New York", "London", "Tokyo"}
cities.add("Sydney")
print(len(cities))   # 4
```

<sub>[Exercise](find-the-bug.md#exercise-582--adding-a-member) · [Runnable file](code/find_the_bug/ex_05_08_02_adding_a_member.py)</sub>

### Solution 6.8.3 — Is it a member?

**Bug type:** Logical

The program tests "yellow", which is not in the set, so it prints False. Test for "blue" to get True.

```python
colors = {"red", "blue", "green"}
print("blue" in colors)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-583--is-it-a-member) · [Runnable file](code/find_the_bug/ex_05_08_03_is_it_a_member.py)</sub>

### Solution 6.8.4 — Shared subjects

**Bug type:** Logical

`|` is union (all subjects from both); shared items need intersection `&`. Use `maya & leo` to get just `{"math"}`.

```python
maya = {"math", "science", "art"}
leo = {"math", "history"}

shared = maya & leo
print(shared)   # {'math'}
```

<sub>[Exercise](find-the-bug.md#exercise-584--shared-subjects) · [Runnable file](code/find_the_bug/ex_05_08_04_shared_subjects.py)</sub>

### Solution 6.8.5 — Building a set

**Bug type:** Runtime

`{}` creates an empty dictionary, not a set, so `seen.add` raises an `AttributeError`. Use `set()` to create an empty set.

```python
seen = set()
seen.add("apple")
print(seen)   # {'apple'}
```

<sub>[Exercise](find-the-bug.md#exercise-585--building-a-set) · [Runnable file](code/find_the_bug/ex_05_08_05_building_a_set.py)</sub>

## 5.9 Dictionaries

### Solution 6.9.1 — Looking up a name

**Bug type:** Runtime

Keys are case-sensitive; `"Name"` is not in the dict, so this raises a `KeyError`. Use the actual key `"name"`.

```python
student = {"name": "Maya", "grade": 10}
print(student["name"])   # Maya
```

<sub>[Exercise](find-the-bug.md#exercise-591--looking-up-a-name) · [Runnable file](code/find_the_bug/ex_05_09_01_looking_up_a_name.py)</sub>

### Solution 6.9.2 — Updating a grade

**Bug type:** Syntax

Dictionary assignment uses square brackets, not parentheses; `student("grade") = 11` is invalid. Use `student["grade"] = 11`.

```python
student = {"name": "Maya", "grade": 10}
student["grade"] = 11
print(student["grade"])   # 11
```

<sub>[Exercise](find-the-bug.md#exercise-592--updating-a-grade) · [Runnable file](code/find_the_bug/ex_05_09_02_updating_a_grade.py)</sub>

### Solution 6.9.3 — Missing key

**Bug type:** Runtime

Indexing a missing key with `[]` raises a `KeyError`. Use `.get` with a default so it returns "not found" instead.

```python
student = {"name": "Maya", "grade": 10}
subject = student.get("favorite_subject", "not found")
print(subject)   # not found
```

<sub>[Exercise](find-the-bug.md#exercise-593--missing-key) · [Runnable file](code/find_the_bug/ex_05_09_03_missing_key.py)</sub>

### Solution 6.9.4 — Safe default with get

**Bug type:** Runtime

`Subject` (capital S) is undefined, so printing it raises a `NameError`. Print the variable `subject`.

```python
student = {"favorite_subject": "science"}
subject = student.get("favorite_subject", "unknown")
print(subject)   # science
```

<sub>[Exercise](find-the-bug.md#exercise-594--safe-default-with-get) · [Runnable file](code/find_the_bug/ex_05_09_04_safe_default_with_get.py)</sub>

### Solution 6.9.5 — Adding an entry

**Bug type:** Runtime

`==` compares values; it does not store anything, so the key "phone" is never added and the next line raises a `KeyError`. Use a single `=` to assign the new entry.

```python
contact = {"name": "Leo"}
contact["phone"] = "555-0100"
print(contact["phone"])   # 555-0100
```

<sub>[Exercise](find-the-bug.md#exercise-595--adding-an-entry) · [Runnable file](code/find_the_bug/ex_05_09_05_adding_an_entry.py)</sub>

## 5.10 Variables and Types

### Solution 6.10.1 — Reading a number

**Bug type:** Runtime

`age_text` is a string, so `age_text + 5` mixes str and int and raises a `TypeError`. Convert the text with `int()` before adding.

```python
age_text = "25"
age = int(age_text) + 5
print(age)   # 30
```

<sub>[Exercise](find-the-bug.md#exercise-5101--reading-a-number) · [Runnable file](code/find_the_bug/ex_05_10_01_reading_a_number.py)</sub>

### Solution 6.10.2 — Building a message

**Bug type:** Runtime

You cannot concatenate a str and an int, so this raises a `TypeError`. Convert the number with `str()` first.

```python
score = 90
message = "Score: " + str(score)
print(message)   # Score: 90
```

<sub>[Exercise](find-the-bug.md#exercise-5102--building-a-message) · [Runnable file](code/find_the_bug/ex_05_10_02_building_a_message.py)</sub>

### Solution 6.10.3 — Checking a type

**Bug type:** Logical

The price is a float, but the check compares against `int`, so it reports False. Compare against `float`.

```python
price = 3.99
print(type(price))   # <class 'float'>
print(type(price) == float)   # True
```

<sub>[Exercise](find-the-bug.md#exercise-5103--checking-a-type) · [Runnable file](code/find_the_bug/ex_05_10_03_checking_a_type.py)</sub>

### Solution 6.10.4 — Converting to float

**Bug type:** Runtime

`int("2.5")` raises a `ValueError` because the text is not a whole number. Use `float()` to convert it.

```python
weight_text = "2.5"
weight = float(weight_text)
print(weight * 2)   # 5.0
```

<sub>[Exercise](find-the-bug.md#exercise-5104--converting-to-float) · [Runnable file](code/find_the_bug/ex_05_10_04_converting_to_float.py)</sub>

### Solution 6.10.5 — Whole-number average

**Bug type:** Runtime

`average` is wrapped in `str()`, so `int("85.5")` raises a `ValueError`. Keep the average numeric and apply `int()` directly.

```python
score1 = 80
score2 = 91

average = (score1 + score2) / 2
print(int(average))   # 85
```

<sub>[Exercise](find-the-bug.md#exercise-5105--whole-number-average) · [Runnable file](code/find_the_bug/ex_05_10_05_whole_number_average.py)</sub>
