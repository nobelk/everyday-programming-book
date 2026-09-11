# Chapter 20 — Common Pitfalls: Find the Bug

Part VII · Reference — *Everyday Programming*

Each program below has exactly one bug drawn from a common Python pitfall; read the prompt, run the code in your head, and find the single mistake.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**130 exercises in 26 sections.**

## 20.1 Forgetting the `:` after `if`, `for`, `while`, or `def`

### Exercise 20.1.1 — Missing colon after `if`

This program should print `"Fever"` when a temperature is at or above 38 degrees Celsius.

```python
temperature = 39
if temperature >= 38
    print("Fever")
```

<sub>[Solution](solutions.md#solution-2011--missing-colon-after-if)</sub>

### Exercise 20.1.2 — Missing colon after `for`

This program should print each planet's distance from the Sun in millions of kilometers.

```python
distances = [58, 108, 150]
for distance in distances
    print(distance)
```

<sub>[Solution](solutions.md#solution-2012--missing-colon-after-for)</sub>

### Exercise 20.1.3 — Missing colon after `while`

This program should count down from 3 to 1 for a rocket launch.

```python
seconds = 3
while seconds > 0
    print(seconds)
    seconds = seconds - 1
```

<sub>[Solution](solutions.md#solution-2013--missing-colon-after-while)</sub>

### Exercise 20.1.4 — Missing colon after `def`

This program should define a function that returns the area of a rectangle and print it.

```python
def rectangle_area(width, height)
    return width * height

print(rectangle_area(4, 5))  # 20
```

<sub>[Solution](solutions.md#solution-2014--missing-colon-after-def)</sub>

### Exercise 20.1.5 — Missing colon after `elif`

This program should label a test score as a pass, a borderline, or a fail.

```python
score = 55
if score >= 60:
    print("Pass")
elif score >= 50
    print("Borderline")
else:
    print("Fail")
```

<sub>[Solution](solutions.md#solution-2015--missing-colon-after-elif)</sub>

## 20.2 Using the wrong indentation

### Exercise 20.2.1 — Body not indented

This program should greet a registered member.

```python
member = "Alex"
if member == "Alex":
print("Welcome back")
```

<sub>[Solution](solutions.md#solution-2021--body-not-indented)</sub>

### Exercise 20.2.2 — Inconsistent indentation in a loop

This program should add up the rainfall for three days.

```python
rainfall = [12, 8, 15]
total = 0
for amount in rainfall:
    total = total + amount
      print(total)  # 35
```

<sub>[Solution](solutions.md#solution-2022--inconsistent-indentation-in-a-loop)</sub>

### Exercise 20.2.3 — Function body not indented

This program should return the perimeter of a square and print it.

```python
def square_perimeter(side):
return 4 * side

print(square_perimeter(6))  # 24
```

<sub>[Solution](solutions.md#solution-2023--function-body-not-indented)</sub>

### Exercise 20.2.4 — Over-indented statement

This program should print whether water is boiling at the given temperature.

```python
temperature = 100
if temperature >= 100:
        print("Boiling")
    print("Done checking")
```

<sub>[Solution](solutions.md#solution-2024--over-indented-statement)</sub>

### Exercise 20.2.5 — Indentation mixing two blocks

This program should print each grade and then announce the report is finished.

```python
grades = [88, 91, 79]
for grade in grades:
    print(grade)
  print("Report complete")
```

<sub>[Solution](solutions.md#solution-2025--indentation-mixing-two-blocks)</sub>

## 20.3 Confusing assignment with equality

### Exercise 20.3.1 — Assignment inside an `if`

This program should check whether a thermostat is set to 20 degrees.

```python
thermostat = 20
if thermostat = 20:
    print("Comfortable")
```

<sub>[Solution](solutions.md#solution-2031--assignment-inside-an-if)</sub>

### Exercise 20.3.2 — Assignment when comparing a password length

This program should confirm a password has exactly 8 characters.

```python
length = 8
if length = 8:
    print("Valid length")
```

<sub>[Solution](solutions.md#solution-2032--assignment-when-comparing-a-password-length)</sub>

### Exercise 20.3.3 — Equality used where assignment is meant

This program should set a starting balance and print it.

```python
balance == 100
print(balance)  # 100
```

<sub>[Solution](solutions.md#solution-2033--equality-used-where-assignment-is-meant)</sub>

### Exercise 20.3.4 — Assignment inside a `while`

This program should keep doubling a sample count until it reaches at least 50.

```python
count = 5
while count = count * 2:
    print(count)
```

<sub>[Solution](solutions.md#solution-2034--assignment-inside-a-while)</sub>

### Exercise 20.3.5 — Equality used for assignment

This program should record a measured speed and print it in km/h.

```python
speed == 60
print("Speed:", speed)  # Speed: 60
```

<sub>[Solution](solutions.md#solution-2035--equality-used-for-assignment)</sub>

## 20.4 Using a variable before it is created

### Exercise 20.4.1 — Printing before assigning

This program should report the number of students in a class.

```python
print(students)
students = 30
```

<sub>[Solution](solutions.md#solution-2041--printing-before-assigning)</sub>

### Exercise 20.4.2 — Using a sum before it exists

This program should add the first two test marks together.

```python
first = 70
second = 85
print(total)
total = first + second
```

<sub>[Solution](solutions.md#solution-2042--using-a-sum-before-it-exists)</sub>

### Exercise 20.4.3 — Using a result before computing it

This program should compute and print the area of a circle with radius 3.

```python
radius = 3
print(area)
area = 3.14159 * radius * radius
```

<sub>[Solution](solutions.md#solution-2043--using-a-result-before-computing-it)</sub>

### Exercise 20.4.4 — Reading a counter that is set later

This program should print how many laps a runner completed.

```python
print("Laps:", laps)
laps = 4
```

<sub>[Solution](solutions.md#solution-2044--reading-a-counter-that-is-set-later)</sub>

### Exercise 20.4.5 — Using a price before defining it

This program should print the total cost of 3 notebooks.

```python
quantity = 3
print(quantity * price)
price = 2
```

<sub>[Solution](solutions.md#solution-2045--using-a-price-before-defining-it)</sub>

## 20.5 Misspelling variable names

### Exercise 20.5.1 — Misspelled variable in a print

This program should print a welcome message.

```python
greeting = "Good morning"
print(greting)
```

<sub>[Solution](solutions.md#solution-2051--misspelled-variable-in-a-print)</sub>

### Exercise 20.5.2 — Misspelled variable in a calculation

This program should print the distance traveled at 60 km/h for 2 hours.

```python
speed = 60
hours = 2
distance = sped * hours
print(distance)  # 120
```

<sub>[Solution](solutions.md#solution-2052--misspelled-variable-in-a-calculation)</sub>

### Exercise 20.5.3 — Inconsistent capitalization

This program should print a city's recorded high temperature.

```python
Temperature = 31
print(temperature)
```

<sub>[Solution](solutions.md#solution-2053--inconsistent-capitalization)</sub>

### Exercise 20.5.4 — Misspelled variable when updating

This program should add a tip to a restaurant bill and print the total.

```python
bill = 40
tip = 6
total = bil + tip
print(total)  # 46
```

<sub>[Solution](solutions.md#solution-2054--misspelled-variable-when-updating)</sub>

### Exercise 20.5.5 — Misspelled list name

This program should print the average of three exam scores.

```python
scores = [80, 90, 100]
average = sum(score) / len(scores)
print(average)  # 90.0
```

<sub>[Solution](solutions.md#solution-2055--misspelled-list-name)</sub>

## 20.6 Mixing strings and numbers without converting types

### Exercise 20.6.1 — Joining text and a number

This program should print a label with the day's step count.

```python
steps = 8000
print("Steps today: " + steps)
```

<sub>[Solution](solutions.md#solution-2061--joining-text-and-a-number)</sub>

### Exercise 20.6.2 — Adding a number to a string label

This program should print how many liters of water to drink.

```python
liters = 2
print("Drink " + liters + " liters")
```

<sub>[Solution](solutions.md#solution-2062--adding-a-number-to-a-string-label)</sub>

### Exercise 20.6.3 — Concatenating a price into a message

This program should announce the ticket price.

```python
price = 15
message = "Ticket costs $" + price
print(message)
```

<sub>[Solution](solutions.md#solution-2063--concatenating-a-price-into-a-message)</sub>

### Exercise 20.6.4 — Combining a count with text

This program should report how many books are on a shelf.

```python
books = 12
print(books + " books on the shelf")
```

<sub>[Solution](solutions.md#solution-2064--combining-a-count-with-text)</sub>

### Exercise 20.6.5 — Treating a string as a number

This program should add a bonus of 10 points to a stored score.

```python
score = "75"
print(score + 10)
```

<sub>[Solution](solutions.md#solution-2065--treating-a-string-as-a-number)</sub>

## 20.7 Forgetting to convert `input()` to a number

### Exercise 20.7.1 — Adding to raw input

This program should ask for a year and print the next year.

```python
year = input("Enter the year: ")
print(year + 1)
```

<sub>[Solution](solutions.md#solution-2071--adding-to-raw-input)</sub>

### Exercise 20.7.2 — Doubling a typed quantity

This program should double the number of cookies the user enters.

```python
cookies = input("How many cookies? ")
print(cookies * 2 == 24)  # for input 12
```

<sub>[Solution](solutions.md#solution-2072--doubling-a-typed-quantity)</sub>

### Exercise 20.7.3 — Summing two typed numbers

This program should add two typed prices and print the total.

```python
first = int(input("First price: "))
second = input("Second price: ")
print(first + second)
```

<sub>[Solution](solutions.md#solution-2073--summing-two-typed-numbers)</sub>

### Exercise 20.7.4 — Comparing typed age to a limit

This program should print `"Adult"` when the typed age is at least 18.

```python
age = input("Your age: ")
if age >= 18:
    print("Adult")
```

<sub>[Solution](solutions.md#solution-2074--comparing-typed-age-to-a-limit)</sub>

### Exercise 20.7.5 — Averaging a typed temperature

This program should halve the temperature the user types.

```python
temperature = input("Temperature: ")
print(temperature / 2)
```

<sub>[Solution](solutions.md#solution-2075--averaging-a-typed-temperature)</sub>

## 20.8 Using `/` when you want a whole-number result

### Exercise 20.8.1 — Splitting students into teams

This program should print how many full teams of 4 can be made from 30 students.

```python
students = 30
team_size = 4
print(students / team_size)  # 7
```

<sub>[Solution](solutions.md#solution-2081--splitting-students-into-teams)</sub>

### Exercise 20.8.2 — Pages per chapter

This program should print how many whole pages each of 5 chapters gets from 52 pages.

```python
pages = 52
chapters = 5
print(pages / chapters)  # 10
```

<sub>[Solution](solutions.md#solution-2082--pages-per-chapter)</sub>

### Exercise 20.8.3 — Counting full boxes

This program should print how many full boxes of 6 eggs come from 40 eggs.

```python
eggs = 40
per_box = 6
full_boxes = eggs / per_box
print(full_boxes)  # 6
```

<sub>[Solution](solutions.md#solution-2083--counting-full-boxes)</sub>

### Exercise 20.8.4 — Whole minutes from seconds

This program should print the number of whole minutes in 200 seconds.

```python
seconds = 200
minutes = seconds / 60
print(minutes)  # 3
```

<sub>[Solution](solutions.md#solution-2084--whole-minutes-from-seconds)</sub>

### Exercise 20.8.5 — Sharing marbles evenly

This program should print how many marbles each of 3 children gets from 25 marbles.

```python
marbles = 25
children = 3
print(marbles / children)  # 8
```

<sub>[Solution](solutions.md#solution-2085--sharing-marbles-evenly)</sub>

## 20.9 Using `^` for powers instead of `**`

### Exercise 20.9.1 — Area of a square

This program should print the area of a square with side 5 (side squared).

```python
side = 5
print(side ^ 2)  # 25
```

<sub>[Solution](solutions.md#solution-2091--area-of-a-square)</sub>

### Exercise 20.9.2 — Cube of a number

This program should print 4 raised to the third power.

```python
base = 4
print(base ^ 3)  # 64
```

<sub>[Solution](solutions.md#solution-2092--cube-of-a-number)</sub>

### Exercise 20.9.3 — Compound growth

This program should print 2 raised to the tenth power.

```python
print(2 ^ 10)  # 1024
```

<sub>[Solution](solutions.md#solution-2093--compound-growth)</sub>

### Exercise 20.9.4 — Volume of a cube

This program should print the volume of a cube with edge 3 (edge cubed).

```python
edge = 3
volume = edge ^ 3
print(volume)  # 27
```

<sub>[Solution](solutions.md#solution-2094--volume-of-a-cube)</sub>

### Exercise 20.9.5 — Energy term squared

This program should print the speed squared for a kinetic-energy calculation.

```python
speed = 6
print(speed ^ 2)  # 36
```

<sub>[Solution](solutions.md#solution-2095--energy-term-squared)</sub>

## 20.10 Modifying a list item that does not exist

### Exercise 20.10.1 — Setting a fourth temperature

This program should replace a placeholder list with three real readings, then store a fourth.

```python
readings = [20, 22, 21]
readings[3] = 23
print(readings)
```

<sub>[Solution](solutions.md#solution-20101--setting-a-fourth-temperature)</sub>

### Exercise 20.10.2 — Recording a new score

This program should store a new game score after the existing three.

```python
scores = [10, 15, 20]
scores[3] = 25
print(scores)
```

<sub>[Solution](solutions.md#solution-20102--recording-a-new-score)</sub>

### Exercise 20.10.3 — Filling in a weekly total

This program should set the fourth week's sales figure.

```python
weekly_sales = [100, 120, 90]
weekly_sales[3] = 110
print(weekly_sales)
```

<sub>[Solution](solutions.md#solution-20103--filling-in-a-weekly-total)</sub>

### Exercise 20.10.4 — Adding a fourth runner's time

This program should store a fourth lap time at the next position.

```python
lap_times = [45, 47, 44]
lap_times[len(lap_times)] = 46
print(lap_times)
```

<sub>[Solution](solutions.md#solution-20104--adding-a-fourth-runners-time)</sub>

### Exercise 20.10.5 — Appending a measurement

This program should add one more pH reading to the list.

```python
ph_values = [7.0, 6.8, 7.2]
ph_values[3] = 6.9
print(ph_values)
```

<sub>[Solution](solutions.md#solution-20105--appending-a-measurement)</sub>

## 20.11 Going past the end of a list

### Exercise 20.11.1 — Reading the last color

This program should print the last color in the list.

```python
colors = ["red", "green", "blue"]
print(colors[3])
```

<sub>[Solution](solutions.md#solution-20111--reading-the-last-color)</sub>

### Exercise 20.11.2 — Printing each day's high

This program should print all four recorded high temperatures.

```python
highs = [28, 30, 29, 31]
for i in range(5):
    print(highs[i])
```

<sub>[Solution](solutions.md#solution-20112--printing-each-days-high)</sub>

### Exercise 20.11.3 — Showing the third prize

This program should print the third prize from the list.

```python
prizes = ["gold", "silver"]
print(prizes[2])
```

<sub>[Solution](solutions.md#solution-20113--showing-the-third-prize)</sub>

### Exercise 20.11.4 — Last item by length

This program should print the last student's name in the list.

```python
students = ["Mia", "Noah", "Liam"]
print(students[len(students)])
```

<sub>[Solution](solutions.md#solution-20114--last-item-by-length)</sub>

### Exercise 20.11.5 — Looping one step too far

This program should print every price in the list.

```python
prices = [3, 5, 9]
index = 0
while index <= len(prices):
    print(prices[index])
    index = index + 1
```

<sub>[Solution](solutions.md#solution-20115--looping-one-step-too-far)</sub>

## 20.12 Using parentheses instead of brackets for lists

### Exercise 20.12.1 — Building a shopping list

This program should make a list of groceries and add one more item.

```python
groceries = ("milk", "bread", "eggs")
groceries.append("butter")
print(groceries)
```

<sub>[Solution](solutions.md#solution-20121--building-a-shopping-list)</sub>

### Exercise 20.12.2 — Collecting daily steps

This program should create a list of step counts and add today's count.

```python
steps = (8000, 9500, 7000)
steps.append(10000)
print(steps)
```

<sub>[Solution](solutions.md#solution-20122--collecting-daily-steps)</sub>

### Exercise 20.12.3 — A list of temperatures

This program should change the first temperature reading to 19.

```python
temperatures = (21, 22, 20)
temperatures[0] = 19
print(temperatures)
```

<sub>[Solution](solutions.md#solution-20123--a-list-of-temperatures)</sub>

### Exercise 20.12.4 — Listing class names

This program should build a list of subjects and add one more.

```python
subjects = ("Math", "Science")
subjects.append("History")
print(subjects)
```

<sub>[Solution](solutions.md#solution-20124--listing-class-names)</sub>

### Exercise 20.12.5 — A list of scores to extend

This program should start a list of scores and append a new one.

```python
scores = (88, 92)
scores.append(75)
print(scores)
```

<sub>[Solution](solutions.md#solution-20125--a-list-of-scores-to-extend)</sub>

## 20.13 Forgetting that strings are immutable

### Exercise 20.13.1 — Capitalizing a name

This program should change the first letter of a name to a capital `"S"`.

```python
name = "sam"
name[0] = "S"
print(name)
```

<sub>[Solution](solutions.md#solution-20131--capitalizing-a-name)</sub>

### Exercise 20.13.2 — Fixing a typo in a word

This program should change `"hpllo"` into `"hello"` by replacing one letter.

```python
word = "hpllo"
word[1] = "e"
print(word)
```

<sub>[Solution](solutions.md#solution-20132--fixing-a-typo-in-a-word)</sub>

### Exercise 20.13.3 — Replacing a digit in a code

This program should change the first character of a code to `"9"`.

```python
code = "12345"
code[0] = "9"
print(code)
```

<sub>[Solution](solutions.md#solution-20133--replacing-a-digit-in-a-code)</sub>

### Exercise 20.13.4 — Masking a letter

This program should hide the last letter of a word with an asterisk.

```python
secret = "open"
secret[3] = "*"
print(secret)
```

<sub>[Solution](solutions.md#solution-20134--masking-a-letter)</sub>

### Exercise 20.13.5 — Correcting a unit label

This program should change the first letter of `"km"` to make `"Km"`.

```python
unit = "km"
unit[0] = "K"
print(unit)
```

<sub>[Solution](solutions.md#solution-20135--correcting-a-unit-label)</sub>

## 20.14 Using `is` instead of `==` for value comparison

### Exercise 20.14.1 — Checking a student's full name

This program should announce a match when the typed name equals the enrolled name.

```python
enrolled_name = "Ada Lovelace"
typed_name = " ".join(["Ada", "Lovelace"])
if typed_name is enrolled_name:
    print("Name matches our records")
else:
    print("Name does not match")
```

<sub>[Solution](solutions.md#solution-20141--checking-a-students-full-name)</sub>

### Exercise 20.14.2 — Matching a password phrase

The program should grant access when the typed phrase equals the stored phrase.

```python
stored_phrase = "open sesame"
typed_phrase = " ".join(["open", "sesame"])
if typed_phrase is stored_phrase:
    print("Access granted")
else:
    print("Access denied")
```

<sub>[Solution](solutions.md#solution-20142--matching-a-password-phrase)</sub>

### Exercise 20.14.3 — Confirming a recipe title

A recipe title is built from its words and should match the saved title.

```python
saved_title = "Banana Bread"
first = "Banana"
second = "Bread"
built_title = first + " " + second
if built_title is saved_title:
    print("Recipe title matches")
else:
    print("Recipe title differs")
```

<sub>[Solution](solutions.md#solution-20143--confirming-a-recipe-title)</sub>

### Exercise 20.14.4 — Comparing two shopping lists

The program should report that two grocery lists hold the same items.

```python
cart_one = ["milk", "eggs", "bread"]
cart_two = ["milk", "eggs", "bread"]
if cart_one is cart_two:
    print("The carts hold the same items")
else:
    print("The carts differ")
```

<sub>[Solution](solutions.md#solution-20144--comparing-two-shopping-lists)</sub>

### Exercise 20.14.5 — Verifying a reading list

The program checks whether the books read so far match the planned reading list.

```python
planned = ["Physics", "Algebra", "Biology"]
read_so_far = ["Physics", "Algebra", "Biology"]
if read_so_far is planned:
    print("You finished the planned books!")
else:
    print("Some planned books remain")
```

<sub>[Solution](solutions.md#solution-20145--verifying-a-reading-list)</sub>

## 20.15 Forgetting to call a function with parentheses

### Exercise 20.15.1 — Reading the current temperature

This program should print the temperature returned by the function.

```python
def current_temperature():
    return 21.5

print("Temperature:", current_temperature)
```

<sub>[Solution](solutions.md#solution-20151--reading-the-current-temperature)</sub>

### Exercise 20.15.2 — Counting words in a sentence

The program should report how many words a sentence contains.

```python
def word_count(sentence):
    return len(sentence.split())

note = "the cat sat on the mat"
print("Words:", word_count)
```

<sub>[Solution](solutions.md#solution-20152--counting-words-in-a-sentence)</sub>

### Exercise 20.15.3 — Rolling for a starting number

The program should print a fixed starting score produced by a helper.

```python
def starting_score():
    return 100

score = starting_score
print("You begin with", score, "points")
```

<sub>[Solution](solutions.md#solution-20153--rolling-for-a-starting-number)</sub>

### Exercise 20.15.4 — Area of a circle

This program should compute and print the area of a circle with radius 4.

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", circle_area(4))
print("Half area:", circle_area / 2)
```

<sub>[Solution](solutions.md#solution-20154--area-of-a-circle)</sub>

### Exercise 20.15.5 — Greeting the next runner

The program should print a greeting for the runner.

```python
def greet_runner(name):
    return "Good luck, " + name + "!"

message = greet_runner
print(message)
```

<sub>[Solution](solutions.md#solution-20155--greeting-the-next-runner)</sub>

## 20.16 Not returning a value from a function

### Exercise 20.16.1 — Converting miles to kilometers

This program should print the distance in kilometers for 5 miles.

```python
def miles_to_km(miles):
    km = miles * 1.60934

print("Kilometers:", miles_to_km(5))
```

<sub>[Solution](solutions.md#solution-20161--converting-miles-to-kilometers)</sub>

### Exercise 20.16.2 — Averaging three test grades

The program should print the average of three grades.

```python
def average(a, b, c):
    total = a + b + c
    average_value = total / 3

print("Average:", average(80, 90, 100))
```

<sub>[Solution](solutions.md#solution-20162--averaging-three-test-grades)</sub>

### Exercise 20.16.3 — Doubling a recipe

This program should return the doubled amount of flour.

```python
def double_amount(cups):
    doubled = cups * 2

flour = double_amount(2.5)
print("Use", flour, "cups of flour")
```

<sub>[Solution](solutions.md#solution-20163--doubling-a-recipe)</sub>

### Exercise 20.16.4 — Perimeter of a rectangle

The program should print the perimeter of a 6 by 4 rectangle.

```python
def perimeter(length, width):
    p = 2 * (length + width)

print("Perimeter:", perimeter(6, 4))
```

<sub>[Solution](solutions.md#solution-20164--perimeter-of-a-rectangle)</sub>

### Exercise 20.16.5 — Tax on a purchase

This program should return the tax owed on a $200 purchase at 8 percent.

```python
def tax_owed(price, rate):
    tax = price * rate / 100

print("Tax:", tax_owed(200, 8))
```

<sub>[Solution](solutions.md#solution-20165--tax-on-a-purchase)</sub>

## 20.17 Changing a global variable inside a function by accident

### Exercise 20.17.1 — Tallying rainfall

The program should add today's rainfall to the running total and print it.

```python
total_rain = 0.0

def add_rain(today):
    total_rain = total_rain + today

add_rain(1.2)
print("Total rainfall:", total_rain)
```

<sub>[Solution](solutions.md#solution-20171--tallying-rainfall)</sub>

### Exercise 20.17.2 — Keeping a running balance

This program should subtract a withdrawal from the account balance.

```python
balance = 500

def withdraw(amount):
    balance = balance - amount

withdraw(120)
print("Balance:", balance)
```

<sub>[Solution](solutions.md#solution-20172--keeping-a-running-balance)</sub>

### Exercise 20.17.3 — Counting visitors

The program should increase the visitor count by one each time someone enters.

```python
visitors = 0

def enter():
    visitors = visitors + 1

enter()
print("Visitors:", visitors)
```

<sub>[Solution](solutions.md#solution-20173--counting-visitors)</sub>

### Exercise 20.17.4 — Accumulating distance

This program should add a new leg of a trip to the total distance traveled.

```python
distance_km = 0

def drive(leg):
    distance_km = distance_km + leg

drive(45)
print("Distance:", distance_km)
```

<sub>[Solution](solutions.md#solution-20174--accumulating-distance)</sub>

### Exercise 20.17.5 — Building a points streak

The program should multiply the current streak by 2 each round.

```python
streak = 1

def double_streak():
    streak = streak * 2

double_streak()
print("Streak:", streak)
```

<sub>[Solution](solutions.md#solution-20175--building-a-points-streak)</sub>

## 20.18 Forgetting to close a file

### Exercise 20.18.1 — Saving a shopping list

This program should write the shopping list to a file and leave no file handle open.

```python
groceries = "milk\neggs\nbread\n"
list_file = open("groceries.txt", "w")
list_file.write(groceries)
print("Shopping list saved")
```

<sub>[Solution](solutions.md#solution-20181--saving-a-shopping-list)</sub>

### Exercise 20.18.2 — Logging a temperature reading

The program should append one temperature reading to a log file safely.

```python
log = open("temps.txt", "a")
log.write("21.5\n")
```

<sub>[Solution](solutions.md#solution-20182--logging-a-temperature-reading)</sub>

### Exercise 20.18.3 — Recording a high score

This program should save the player's high score to disk safely.

```python
high_score = 4200
score_file = open("highscore.txt", "w")
score_file.write(str(high_score))
print("High score recorded")
```

<sub>[Solution](solutions.md#solution-20183--recording-a-high-score)</sub>

### Exercise 20.18.4 — Writing a daily journal entry

The program should write one journal line to a file safely.

```python
entry = "Today I walked 10000 steps.\n"
journal = open("journal.txt", "w")
journal.write(entry)
print("Entry written")
```

<sub>[Solution](solutions.md#solution-20184--writing-a-daily-journal-entry)</sub>

### Exercise 20.18.5 — Storing a measured weight

This program should save a measured weight in kilograms to a file safely.

```python
weight_kg = 72.4
weight_file = open("weight.txt", "w")
weight_file.write(f"{weight_kg}\n")
```

<sub>[Solution](solutions.md#solution-20185--storing-a-measured-weight)</sub>

## 20.19 Using a broad `except:` and hiding errors

### Exercise 20.19.1 — Converting a typed age

This program should turn typed text into a number and warn only when the text is not a number.

```python
text = "12y"
try:
    age = int(text)
    print("Next year you will be", age + 1)
except:
    print("Please type a whole number")
```

<sub>[Solution](solutions.md#solution-20191--converting-a-typed-age)</sub>

### Exercise 20.19.2 — Dividing a bill among friends

The program should split a bill and report only when the number of people is zero.

```python
bill = 90
people = 0
try:
    share = bill / people
    print("Each pays", share)
except:
    print("There must be at least one person")
```

<sub>[Solution](solutions.md#solution-20192--dividing-a-bill-among-friends)</sub>

### Exercise 20.19.3 — Looking up a price

This program should read a price from a dictionary and warn only when the item is missing.

```python
prices = {"apple": 0.5, "banana": 0.3}
item = "cherry"
try:
    print("Price:", prices[item])
except:
    print("That item is not on the price list")
```

<sub>[Solution](solutions.md#solution-20193--looking-up-a-price)</sub>

### Exercise 20.19.4 — Parsing a temperature

The program should convert typed text to a float and warn only on bad number text.

```python
reading = "hot"
try:
    celsius = float(reading)
    print("Fahrenheit:", celsius * 9 / 5 + 32)
except:
    print("That is not a valid temperature")
```

<sub>[Solution](solutions.md#solution-20194--parsing-a-temperature)</sub>

### Exercise 20.19.5 — Reading a list position

This program should print the third score and warn only when the position is out of range.

```python
scores = [88, 92]
try:
    print("Third score:", scores[2])
except:
    print("There is no score at that position")
```

<sub>[Solution](solutions.md#solution-20195--reading-a-list-position)</sub>

## 20.20 Comparing text without thinking about case

### Exercise 20.20.1 — Accepting a yes answer

This program should accept the answer "yes" no matter how it is capitalized.

```python
answer = "YES"
if answer == "yes":
    print("Confirmed")
else:
    print("Not confirmed")
```

<sub>[Solution](solutions.md#solution-20201--accepting-a-yes-answer)</sub>

### Exercise 20.20.2 — Matching a chosen color

The program should detect the favorite color "blue" regardless of case.

```python
favorite = "Blue"
if favorite.upper() == "blue":
    print("You picked blue")
```

<sub>[Solution](solutions.md#solution-20202--matching-a-chosen-color)</sub>

### Exercise 20.20.3 — Checking a chemical symbol

This program should recognize the element symbol "Na" however the user types it.

```python
symbol = "NA"
if symbol == "Na":
    print("That is sodium")
```

<sub>[Solution](solutions.md#solution-20203--checking-a-chemical-symbol)</sub>

### Exercise 20.20.4 — Looking up a city name

The program should find "Paris" in the list even if typed in lowercase.

```python
cities = ["Paris", "London", "Tokyo"]
search = "paris"
if search in cities:
    print("City found")
else:
    print("City not found")
```

<sub>[Solution](solutions.md#solution-20204--looking-up-a-city-name)</sub>

### Exercise 20.20.5 — Confirming a unit

This program should accept the unit "kg" whether typed as "KG", "Kg", or "kg".

```python
unit = "KG"
if unit.upper() == "kg":
    print("Kilograms")
```

<sub>[Solution](solutions.md#solution-20205--confirming-a-unit)</sub>

## 20.21 Using `range(len(...))` when iterating over items directly is simpler

### Exercise 20.21.1 — Printing each planet

This program should print every planet name on its own line.

```python
planets = ["Mercury", "Venus", "Earth", "Mars"]
for i in range(len(planets)):
    print(planet)
```

<sub>[Solution](solutions.md#solution-20211--printing-each-planet)</sub>

### Exercise 20.21.2 — Summing daily sales

The program should add up every day's sales and print the total.

```python
sales = [120, 85, 200, 95]
total = 0
for i in range(len(sales)):
    total = total + sales
print("Total sales:", total)
```

<sub>[Solution](solutions.md#solution-20212--summing-daily-sales)</sub>

### Exercise 20.21.3 — Greeting each guest

This program should print a greeting for every guest.

```python
guests = ["Ana", "Ben", "Cara"]
for guest in range(len(guests)):
    print("Welcome,", guest)
```

<sub>[Solution](solutions.md#solution-20213--greeting-each-guest)</sub>

### Exercise 20.21.4 — Doubling each measurement

The program should print double each measurement in the list.

```python
measurements = [3, 5, 8]
for m in range(len(measurements)):
    print(m * 2)
```

<sub>[Solution](solutions.md#solution-20214--doubling-each-measurement)</sub>

### Exercise 20.21.5 — Listing the ingredients

This program should print each ingredient.

```python
ingredients = ["flour", "sugar", "butter"]
for item in range(len(ingredients)):
    print(item)
```

<sub>[Solution](solutions.md#solution-20215--listing-the-ingredients)</sub>

## 20.22 Shadowing built-in names like `list`, `str`, or `sum`

### Exercise 20.22.1 — Counting items in a basket

This program should count the letters in a fruit name after storing some numbers.

```python
len = [4, 8, 15]
fruit = "banana"
print("Letters in banana:", len(fruit))
```

<sub>[Solution](solutions.md#solution-20221--counting-items-in-a-basket)</sub>

### Exercise 20.22.2 — Totaling a receipt

The program should add up the prices on a receipt.

```python
sum = 0
prices = [2.50, 3.00, 1.25]
print("Receipt total:", sum(prices))
```

<sub>[Solution](solutions.md#solution-20222--totaling-a-receipt)</sub>

### Exercise 20.22.3 — Turning a word into letters

This program should turn the word into a list of its letters.

```python
list = "abc"
letters = list("hello")
print(letters)
```

<sub>[Solution](solutions.md#solution-20223--turning-a-word-into-letters)</sub>

### Exercise 20.22.4 — Labeling a measurement

The program should print a number alongside its unit as text.

```python
str = "kilograms"
weight = 70
print(str(weight) + " " + str)
```

<sub>[Solution](solutions.md#solution-20224--labeling-a-measurement)</sub>

### Exercise 20.22.5 — Finding the largest reading

This program should print the largest of three sensor readings.

```python
max = 9999
readings = [33.1, 36.5, 31.0]
print("Highest reading:", max(readings))
```

<sub>[Solution](solutions.md#solution-20225--finding-the-largest-reading)</sub>

## 20.23 Expecting floating-point math to be exact

### Exercise 20.23.1 — Splitting a bill exactly

This program should confirm that three shares of $0.10 add up to $0.30.

```python
share = 0.10
total = share + share + share
if total == 0.30:
    print("The shares add up exactly")
else:
    print("The shares do not add up exactly")
```

<sub>[Solution](solutions.md#solution-20231--splitting-a-bill-exactly)</sub>

### Exercise 20.23.2 — Adding two distances

The program should confirm that 0.1 km plus 0.2 km equals 0.3 km.

```python
leg_one = 0.1
leg_two = 0.2
if leg_one + leg_two == 0.3:
    print("Distances match")
else:
    print("Distances do not match")
```

<sub>[Solution](solutions.md#solution-20232--adding-two-distances)</sub>

### Exercise 20.23.3 — Checking a measured volume

This program should confirm that three 0.1 L pours fill a 0.3 L cup.

```python
pour = 0.1
filled = pour * 3
if filled == 0.3:
    print("Cup is exactly full")
else:
    print("Cup is not exactly full")
```

<sub>[Solution](solutions.md#solution-20233--checking-a-measured-volume)</sub>

### Exercise 20.23.4 — Verifying a percentage

The program should check that 0.7 plus 0.1 equals 0.8.

```python
part_one = 0.7
part_two = 0.1
if part_one + part_two == 0.8:
    print("Percentages add correctly")
else:
    print("Percentages do not add correctly")
```

<sub>[Solution](solutions.md#solution-20234--verifying-a-percentage)</sub>

### Exercise 20.23.5 — Comparing a savings target

This program should confirm that saving $1.10 three times reaches $3.30.

```python
weekly = 1.10
saved = weekly * 3
if saved == 3.30:
    print("You reached the target")
else:
    print("You did not reach the target")
```

<sub>[Solution](solutions.md#solution-20235--comparing-a-savings-target)</sub>

## 20.24 Writing long code without testing small pieces

### Exercise 20.24.1 — Average speed of a trip

This program should compute average speed (distance over time) for a 150 km trip in 3 hours and print 50.0.

```python
def average_speed(distance, time):
    return time / distance

print("Average speed:", average_speed(150, 3))  # Average speed: 50.0
```

<sub>[Solution](solutions.md#solution-20241--average-speed-of-a-trip)</sub>

### Exercise 20.24.2 — Final price after discount

The program should subtract a 20 percent discount from a $50 item and print 40.0.

```python
def final_price(price, percent_off):
    discount = price * percent_off
    return price - discount

print("Final price:", final_price(50, 20))  # Final price: 40.0
```

<sub>[Solution](solutions.md#solution-20242--final-price-after-discount)</sub>

### Exercise 20.24.3 — Kinetic energy of a moving cart

This program should compute kinetic energy (one-half m v squared) for m=2, v=3 and print 9.0.

```python
def kinetic_energy(mass, speed):
    return 0.5 * mass * speed * 2

print("Kinetic energy:", kinetic_energy(2, 3))  # Kinetic energy: 9.0
```

<sub>[Solution](solutions.md#solution-20243--kinetic-energy-of-a-moving-cart)</sub>

### Exercise 20.24.4 — Celsius to Fahrenheit

The program should convert 100 degrees Celsius to Fahrenheit and print 212.0.

```python
def to_fahrenheit(celsius):
    return celsius * 9 / 5 - 32

print("Fahrenheit:", to_fahrenheit(100))  # Fahrenheit: 212.0
```

<sub>[Solution](solutions.md#solution-20244--celsius-to-fahrenheit)</sub>

### Exercise 20.24.5 — Average of a list of grades

This program should print the average of four grades and print 85.0.

```python
def average(grades):
    return sum(grades) / len(grades) - 1

print("Average:", average([80, 90, 80, 90]))  # Average: 85.0
```

<sub>[Solution](solutions.md#solution-20245--average-of-a-list-of-grades)</sub>

## 20.25 Shallow vs deep copy

### Exercise 20.25.1 — Copying a seating chart

This program should copy a seating chart so editing the copy leaves the original unchanged.

```python
import copy

original = [["Ana", "Ben"], ["Cara", "Dan"]]
backup = original.copy()
backup[0].append("Eve")
print("Original:", original)  # Original: [['Ana', 'Ben'], ['Cara', 'Dan']]
```

<sub>[Solution](solutions.md#solution-20251--copying-a-seating-chart)</sub>

### Exercise 20.25.2 — Backing up monthly budgets

The program should make an independent copy of a nested budget so changes do not leak back.

```python
import copy

budgets = [[100, 200], [300, 400]]
saved = budgets[:]
saved[1][0] = 999
print("Budgets:", budgets)  # Budgets: [[100, 200], [300, 400]]
```

<sub>[Solution](solutions.md#solution-20252--backing-up-monthly-budgets)</sub>

### Exercise 20.25.3 — Duplicating a tic-tac-toe board

This program should duplicate a game board so the duplicate can be edited safely.

```python
import copy

board = [["X", "O"], ["O", "X"]]
trial = list(board)
trial[0][1] = "X"
print("Board:", board)  # Board: [['X', 'O'], ['O', 'X']]
```

<sub>[Solution](solutions.md#solution-20253--duplicating-a-tic-tac-toe-board)</sub>

### Exercise 20.25.4 — Snapshotting weekly readings

The program should take a snapshot of nested sensor readings that stays fixed.

```python
import copy

readings = [[1.0, 2.0], [3.0, 4.0]]
snapshot = readings.copy()
snapshot[0][0] = 99.0
print("Readings:", readings)  # Readings: [[1.0, 2.0], [3.0, 4.0]]
```

<sub>[Solution](solutions.md#solution-20254--snapshotting-weekly-readings)</sub>

### Exercise 20.25.5 — Cloning a recipe with sub-steps

This program should clone a recipe (with nested steps) so editing the clone is safe.

```python
import copy

recipe = [["mix", "stir"], ["bake", "cool"]]
clone = recipe[:]
clone[1].append("serve")
print("Recipe:", recipe)  # Recipe: [['mix', 'stir'], ['bake', 'cool']]
```

<sub>[Solution](solutions.md#solution-20255--cloning-a-recipe-with-sub-steps)</sub>

## 20.26 Mutable default arguments

### Exercise 20.26.1 — Collecting quiz answers

Each call should start with an empty answer sheet and add one answer.

```python
def record_answer(answer, sheet=[]):
    sheet.append(answer)
    return sheet

print(record_answer("A"))  # ['A']
print(record_answer("B"))  # ['B']
```

<sub>[Solution](solutions.md#solution-20261--collecting-quiz-answers)</sub>

### Exercise 20.26.2 — Building a grocery list

Each call should begin with a fresh, empty cart and add one item.

```python
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("milk"))   # ['milk']
print(add_item("eggs"))   # ['eggs']
```

<sub>[Solution](solutions.md#solution-20262--building-a-grocery-list)</sub>

### Exercise 20.26.3 — Logging a single temperature

Each call should return a new log holding only the reading passed in.

```python
def log_reading(reading, log=[]):
    log.append(reading)
    return log

print(log_reading(21.5))  # expected [21.5]
print(log_reading(19.0))  # expected [19.0]
```

<sub>[Solution](solutions.md#solution-20263--logging-a-single-temperature)</sub>

### Exercise 20.26.4 — Tracking a player's scores

Each call should start a brand-new scoreboard with just the given score.

```python
def new_scoreboard(score, board=[]):
    board.append(score)
    return board

print(new_scoreboard(10))  # expected [10]
print(new_scoreboard(20))  # expected [20]
```

<sub>[Solution](solutions.md#solution-20264--tracking-a-players-scores)</sub>

### Exercise 20.26.5 — Noting one ingredient

Each call should produce a fresh list containing only the ingredient given.

```python
def note_ingredient(name, items=[]):
    items.append(name)
    return items

print(note_ingredient("flour"))  # ['flour']
print(note_ingredient("sugar"))  # ['sugar']
```

<sub>[Solution](solutions.md#solution-20265--noting-one-ingredient)</sub>
