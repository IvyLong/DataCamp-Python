# Data Structures in Python

## Learning Objectives

By the end of this section, you will be able to:
- Use Python’s built-in data structures: lists, tuples, dictionaries, and sets
- Perform common operations like indexing, appending, and deleting elements
- Apply tuple unpacking in real-world scenarios
- Create, read, and update dictionaries
- Make use of set operations for unique collection use cases
- Build lists efficiently using list comprehensions
- Work with nested data structures for handling complex data

---

## 1. Lists and List Operations

Lists are ordered, mutable collections to store items.

### Creating a List

```python
colors = ["red", "green", "blue"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hi", 3.14]
```

### Accessing & Modifying

```python
print(colors[0])  # red
colors[2] = "yellow"
print(colors)     # ['red', 'green', 'yellow']
```

### List Methods

```python
colors.append("blue")          # Add to end
colors.insert(1, "purple")     # Insert at index 1
colors.remove("green")         # Remove by value
numbers.pop()                  # Remove last item

print(len(colors))             # List length
print(colors[1:3])             # Slicing
```

### Iterating Through a List

```python
for color in colors:
    print(f"I like {color}")
```

---

## 2. Tuples and Tuple Unpacking

Tuples are ordered, immutable collections—great for fixed data.

### Creating and Using Tuples

```python
dimensions = (20, 40)
person = ("Alice", 30)

# Tuple unpacking
width, height = dimensions
print(f"Width: {width}, Height: {height}")
```

### When to Use Tuples

- Grouping related, fixed data
- Function returns with multiple values

---

## 3. Dictionaries

Dictionaries are collections of key-value pairs for fast lookups.

### Creating and Accessing

```python
student = {"name": "Charlie", "age": 22, "grade": "A"}
print(student["name"])   # Charlie

# Adding or updating
student["age"] = 23
student["major"] = "Math"
```

### Dictionary Methods

```python
print(student.keys())    # dict_keys(['name', 'age', 'grade', 'major'])
print(student.values())  # dict_values(['Charlie', 23, 'A', 'Math'])

for key, value in student.items():
    print(f"{key}: {value}")
```

### Removing Items

```python
del student["grade"]
age = student.pop("age")
```

---

## 4. Sets

Sets store unordered, unique elements—great for membership checks or removing duplicates.

### Creating and Using Sets

```python
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)  # {1, 2, 3}

unique_numbers.add(4)
unique_numbers.discard(2)
```

### Set Operations

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # Union: {1, 2, 3, 4}
print(a & b)  # Intersection: {2, 3}
print(a - b)  # Difference: {1}
```

---

## 5. List Comprehensions

List comprehensions give you a concise way to generate lists.

### Example: Squares

```python
squares = [x**2 for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]
```

### Example: Filtering

```python
even = [x for x in range(10) if x % 2 == 0]
print(even)   # [0, 2, 4, 6, 8]
```

### Example: Nested Loop

```python
pairs = [(x, y) for x in [1,2] for y in [3,4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]
```

---

## 6. Nested Data Structures

You can combine data structures to model complex data.

### List of Dictionaries

```python
people = [
    {"name": "Bob", "age": 28},
    {"name": "Sue", "age": 32}
]
print(people[0]["name"])  # Bob
```

### Dictionary of Lists

```python
grades = {
    "Alice": [85, 90, 92],
    "Bob": [70, 88, 81]
}
print(grades["Alice"][1])  # 90
```

### List of Lists (Matrix)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])  # 6
```

---

## Exercises

### 1. Lists

- Create a list of five cities.
- Replace the third city with a new one.
- Remove the last city and print the resulting list.

### 2. Tuples

- Create a tuple representing a date (year, month, day).
- Use tuple unpacking to assign each part to a variable and print them.

### 3. Dictionaries

- Make a dictionary mapping three people's names to their favorite colors.
- Add a new person, change one color, and remove one entry.
- Loop through the dictionary and print each person's favorite color.

### 4. Sets

- Given the list `[1, 2, 2, 3, 4, 4, 5]`, create a set from it.
- Add the number 6 to the set.
- Check if 3 is in the set.

### 5. List Comprehensions

- Write a list comprehension to create a list of all squares from 1 to 10 that are even.

### 6. Nested Structures

- Create a list of dictionaries, each representing a book with its 'title' and 'author'.
- Print the title of the second book.

---

## Key Takeaways

- Use the right data structure for the task—lists for ordered collections, tuples for immutable groups, dictionaries for key-value data, and sets for unique items.
- List comprehensions provide a powerful way to create and filter lists.
- Combining these structures lets you manage complex data efficiently!

