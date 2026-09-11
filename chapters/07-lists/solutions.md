# Chapter 7 — Lists: Find the Bug, Solutions

Each solution names the bug type — **syntax**, **runtime**, or **logical** — explains why the original program misbehaved, and shows the corrected program.

Back to [the exercises](find-the-bug.md).

## 7.1 Lists

### Solution 7.1.1 — A list is mutable

**Bug type:** Runtime

The list has three items at indexes 0, 1, and 2, so `tokyo_temps[3]` is out of range and raises an `IndexError`. The typo is at index 0, so the fix assigns to `tokyo_temps[0]`.

```python
tokyo_temps = [33.0, 36.5, 31.0]
tokyo_temps[0] = 33.5
print(tokyo_temps)   # [33.5, 36.5, 31.0]
```

<sub>[Exercise](find-the-bug.md#exercise-711--a-list-is-mutable) · [Runnable file](code/find_the_bug/ex_06_04_01_a_list_is_mutable.py)</sub>

### Solution 7.1.2 — Aliasing a list

**Bug type:** Logical

`list(readings)` builds a brand-new list, so `same_readings` is a separate object and appending to it does not change `readings`. To make both names refer to the same list, assign directly with `same_readings = readings`.

```python
readings = [12, 15, 9]
same_readings = readings
same_readings.append(20)
print(readings)   # [12, 15, 9, 20]
```

<sub>[Exercise](find-the-bug.md#exercise-712--aliasing-a-list) · [Runnable file](code/find_the_bug/ex_06_04_02_aliasing_a_list.py)</sub>

### Solution 7.1.3 — Appending to a list

**Bug type:** Logical

`n + n` doubles each number instead of squaring it, so the list comes out `[2, 4, 6, 8, 10]`. Squaring with `n * n` (or `n ** 2`) produces the intended `[1, 4, 9, 16, 25]`.

```python
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)   # [1, 4, 9, 16, 25]
```

<sub>[Exercise](find-the-bug.md#exercise-713--appending-to-a-list) · [Runnable file](code/find_the_bug/ex_06_04_03_appending_to_a_list.py)</sub>

### Solution 7.1.4 — Indexing the last item

**Bug type:** Runtime

`len(scores)` is 4, but valid indexes are 0 through 3, so `scores[len(scores)]` raises an `IndexError`. The last item is at `scores[len(scores) - 1]`, or more simply `scores[-1]`.

```python
scores = [91, 87, 95, 78]
latest = scores[-1]
print(latest)   # 78
```

<sub>[Exercise](find-the-bug.md#exercise-714--indexing-the-last-item) · [Runnable file](code/find_the_bug/ex_06_04_04_indexing_the_last_item.py)</sub>

### Solution 7.1.5 — A list method

**Bug type:** Runtime

`list.remove` deletes by *value*, not by index, so `tasks.remove(1)` looks for the value `1` and raises a `ValueError`. To drop the finished task by value, remove `"report"` (or use `del tasks[1]`).

```python
tasks = ["email", "report", "lunch"]
tasks.remove("report")
print(tasks)   # ['email', 'lunch']
```

<sub>[Exercise](find-the-bug.md#exercise-715--a-list-method) · [Runnable file](code/find_the_bug/ex_06_04_05_a_list_method.py)</sub>

## 7.2 Copying a List

### Solution 7.2.1 — Assignment is not a copy

**Bug type:** Logical

`backup = temps` makes both names point at the same list, so appending to `temps` also changes `backup`. Taking a real copy with `temps.copy()` (or `temps[:]`) keeps the backup unchanged.

```python
temps = [33.0, 36.5, 31.0]
backup = temps.copy()
temps.append(34.0)
print(backup)   # [33.0, 36.5, 31.0]
```

<sub>[Exercise](find-the-bug.md#exercise-721--assignment-is-not-a-copy) · [Runnable file](code/find_the_bug/ex_06_05_01_assignment_is_not_a_copy.py)</sub>

### Solution 7.2.2 — Making a shallow copy

**Bug type:** Runtime

`prices.copy` refers to the method without calling it, so `copy_of_prices` becomes a method object and `.append` raises an `AttributeError`. Calling `prices.copy()` makes the independent copy.

```python
prices = [1.99, 2.49, 0.99]
copy_of_prices = prices.copy()
copy_of_prices.append(5.00)
print(prices)            # [1.99, 2.49, 0.99]
print(copy_of_prices)    # [1.99, 2.49, 0.99, 5.0]
```

<sub>[Exercise](find-the-bug.md#exercise-722--making-a-shallow-copy) · [Runnable file](code/find_the_bug/ex_06_05_02_making_a_shallow_copy.py)</sub>

### Solution 7.2.3 — Copying with a slice

**Bug type:** Logical

The slice `grades[0:2]` copies only the first two items, so `working` starts as `[85, 90]` and the result is wrong. A full-list slice `grades[:]` copies every element.

```python
grades = [85, 90, 78]
working = grades[:]
working.append(100)
print(grades)    # [85, 90, 78]
print(working)   # [85, 90, 78, 100]
```

<sub>[Exercise](find-the-bug.md#exercise-723--copying-with-a-slice) · [Runnable file](code/find_the_bug/ex_06_05_03_copying_with_a_slice.py)</sub>

### Solution 7.2.4 — Deep copy for nested lists

**Bug type:** Logical

`copy.copy` makes a shallow copy, so the inner lists are still shared and appending to `independent[0]` also changes `grid`. `copy.deepcopy` copies the nested lists recursively, keeping the original intact.

```python
import copy

grid = [[1, 2], [3, 4]]
independent = copy.deepcopy(grid)
independent[0].append(99)
print(grid)         # [[1, 2], [3, 4]]
print(independent)  # [[1, 2, 99], [3, 4]]
```

<sub>[Exercise](find-the-bug.md#exercise-724--deep-copy-for-nested-lists) · [Runnable file](code/find_the_bug/ex_06_05_04_deep_copy_for_nested_lists.py)</sub>

### Solution 7.2.5 — Shallow copy shares inner lists

**Bug type:** Logical

`seats.copy()` is a shallow copy: the outer list is new, but the row lists are shared, so `new_seats[0].append` also changes `seats`. Using `copy.deepcopy` copies each row, leaving the original chart unchanged.

```python
import copy

seats = [["A1", "A2"], ["B1", "B2"]]
new_seats = copy.deepcopy(seats)
new_seats[0].append("A3")
print(seats)       # [['A1', 'A2'], ['B1', 'B2']]
print(new_seats)   # [['A1', 'A2', 'A3'], ['B1', 'B2']]
```

<sub>[Exercise](find-the-bug.md#exercise-725--shallow-copy-shares-inner-lists) · [Runnable file](code/find_the_bug/ex_06_05_05_shallow_copy_shares_inner_lists.py)</sub>
