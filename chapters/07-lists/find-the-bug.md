# Chapter 7 — Lists: Find the Bug

Part III · Data — *Everyday Programming*

These exercises cover objects in Python — classes, instance versus class data, duck typing, lists, and copying lists — and each program below contains exactly one bug for you to find and fix.

Read each program, decide what it is supposed to print, and find the one line that stops it. Then check yourself against [the solutions](solutions.md). The corrected programs are also available as runnable files under [`code/find_the_bug/`](code/find_the_bug).

**25 exercises in 5 sections.**

## 7.1 Lists

### Exercise 7.1.1 — A list is mutable

This program corrects a typo in a list of daily temperatures.

```python
tokyo_temps = [33.0, 36.5, 31.0]
tokyo_temps[3] = 33.5
print(tokyo_temps)   # [33.5, 36.5, 31.0]
```

<sub>[Solution](solutions.md#solution-711--a-list-is-mutable)</sub>

### Exercise 7.1.2 — Aliasing a list

The two names are meant to refer to the same list, so a change through one is seen through the other. This should print the list with the new reading.

```python
readings = [12, 15, 9]
same_readings = list(readings)
same_readings.append(20)
print(readings)   # [12, 15, 9, 20]
```

<sub>[Solution](solutions.md#solution-712--aliasing-a-list)</sub>

### Exercise 7.1.3 — Appending to a list

This program builds a list of square numbers from 1 to 5.

```python
squares = []
for n in range(1, 6):
    squares.append(n + n)
print(squares)   # [1, 4, 9, 16, 25]
```

<sub>[Solution](solutions.md#solution-713--appending-to-a-list)</sub>

### Exercise 7.1.4 — Indexing the last item

This program prints the most recent score in the list.

```python
scores = [91, 87, 95, 78]
latest = scores[len(scores)]
print(latest)   # 78
```

<sub>[Solution](solutions.md#solution-714--indexing-the-last-item)</sub>

### Exercise 7.1.5 — A list method

This program removes a finished task from the to-do list.

```python
tasks = ["email", "report", "lunch"]
tasks.remove(1)
print(tasks)   # ['email', 'lunch']
```

<sub>[Solution](solutions.md#solution-715--a-list-method)</sub>

## 7.2 Copying a List

### Exercise 7.2.1 — Assignment is not a copy

The backup should stay unchanged after we add a new reading to the original.

```python
temps = [33.0, 36.5, 31.0]
backup = temps
temps.append(34.0)
print(backup)   # [33.0, 36.5, 31.0]
```

<sub>[Solution](solutions.md#solution-721--assignment-is-not-a-copy)</sub>

### Exercise 7.2.2 — Making a shallow copy

This should make an independent copy of a flat list of prices.

```python
prices = [1.99, 2.49, 0.99]
copy_of_prices = prices.copy
copy_of_prices.append(5.00)
print(prices)            # [1.99, 2.49, 0.99]
print(copy_of_prices)    # [1.99, 2.49, 0.99, 5.0]
```

<sub>[Solution](solutions.md#solution-722--making-a-shallow-copy)</sub>

### Exercise 7.2.3 — Copying with a slice

A slice copy of a flat list should leave the original alone.

```python
grades = [85, 90, 78]
working = grades[0:2]
working.append(100)
print(grades)    # [85, 90, 78]
print(working)   # [85, 90, 78, 100]
```

<sub>[Solution](solutions.md#solution-723--copying-with-a-slice)</sub>

### Exercise 7.2.4 — Deep copy for nested lists

The grid holds rows of numbers. We want an independent copy whose rows can change without touching the original.

```python
import copy

grid = [[1, 2], [3, 4]]
independent = copy.copy(grid)
independent[0].append(99)
print(grid)         # [[1, 2], [3, 4]]
print(independent)  # [[1, 2, 99], [3, 4]]
```

<sub>[Solution](solutions.md#solution-724--deep-copy-for-nested-lists)</sub>

### Exercise 7.2.5 — Shallow copy shares inner lists

The seating chart is a list of rows. We copy it, then add a seat to one row of the copy; the original chart should be unchanged.

```python
import copy

seats = [["A1", "A2"], ["B1", "B2"]]
new_seats = seats.copy()
new_seats[0].append("A3")
print(seats)       # [['A1', 'A2'], ['B1', 'B2']]
print(new_seats)   # [['A1', 'A2', 'A3'], ['B1', 'B2']]
```

<sub>[Solution](solutions.md#solution-725--shallow-copy-shares-inner-lists)</sub>
