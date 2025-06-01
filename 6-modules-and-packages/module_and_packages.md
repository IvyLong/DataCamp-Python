# Python Workshop: Modules and Packages

## Learning Objectives

By the end of this section, you will be able to:
- Import and use Python modules to organize and reuse code
- Create your own modules and understand how imports work
- Explore Python’s standard library for useful tools
- Manage packages using pip (Python’s package installer)
- Understand and set up virtual environments for project isolation
- Install and use third-party libraries

---

## 1. Importing Modules

Modules are files containing Python code (functions, variables, classes) that you can reuse in your programs.

### Importing a Whole Module

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### Importing Specific Functions or Classes

```python
from math import pi, sqrt
print(pi)         # Output: 3.141592653589793
print(sqrt(25))   # Output: 5.0
```

### Assigning an Alias

This helps shorten long module names.

```python
import statistics as stats
data = [1, 2, 3, 4, 5]
print(stats.mean(data))  # Output: 3
```

---

## 2. Creating Your Own Modules

Any `.py` file can be a module! This helps you organize and reuse your code.

### Step 1: Write a Module

Create a file named `greetings.py`:

```python
# greetings.py
def say_hello(name):
    print(f"Hello, {name}!")
```

### Step 2: Import and Use It

In another file (or interactive session):

```python
import greetings
greetings.say_hello("Alice")  # Output: Hello, Alice!
```

Or import only what you need:

```python
from greetings import say_hello
say_hello("Bob")
```

**Note:** Make sure both files are in the same folder, or your module is in the Python path.

---

## 3. Standard Library Exploration

Python comes with dozens of built-in modules called the "standard library". These are well-tested and save you time!

- `math`: Advanced math functions
- `random`: Random numbers and selections
- `os`: Interact with the operating system
- `datetime`: Work with dates and times
- `json`: Read and write JSON data
- `collections`: Useful container datatypes
- `itertools`: Advanced iterator and combinatorics tools

### Example

```python
import random

for _ in range(3):
    print(random.randint(1, 6))  # Simulate dice rolls
```

---

## 4. Package Management with pip

**pip** is Python’s package installer. Use it to install and manage third-party libraries.

### Installing a Package

Open your terminal or command prompt and type:

```
pip install requests
```

### Upgrading or Uninstalling

```
pip install --upgrade requests
pip uninstall requests
```

### Listing Installed Packages

```
pip list
```

---

## 5. Virtual Environments

A **virtual environment** is a self-contained directory with its own Python and package versions. This prevents conflicts between projects.

### Creating a Virtual Environment

```bash
python -m venv myenv
```

### Activating the Virtual Environment

- **Windows:**
  ```
  myenv\Scripts\activate
  ```
- **Mac/Linux:**
  ```
  source myenv/bin/activate
  ```

Once activated, install packages as usual with `pip`. To leave:

```
deactivate
```

---

## 6. Using Third-Party Libraries

Python has a huge ecosystem of community-built libraries!

### Example: Using `requests` to Fetch a Web Page

First, install it:  
```bash
pip install requests
```

Then, use it in your code:

```python
import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to fetch data.")
```

---

## Advanced Topic: Creating a Package

If you want to share your code as a package, organize multiple modules in a directory with an `__init__.py` file. Look up Python packaging guides for more info!

---

## Exercises

1. **Importing Modules**
    - Use the `random` module to pick a random name from a list of five.

2. **Creating Your Own Module**
    - Write a file `math_utils.py` with a function `add(a, b)` that returns the sum.
    - Import and use this function from another script.

3. **Standard Library Exploration**
    - Use the `datetime` module to print today’s date in `YYYY-MM-DD` format.
    - Use the `collections.Counter` class to count letters in a word.

4. **Package Management**
    - Create a virtual environment and activate it.
    - Use pip to install the `pandas` library.
    - Write code to import pandas and print its version.

5. **Using Third-Party Libraries**
    - Use the `requests` library to fetch contents of https://www.python.org and print the first 100 characters.

---

## Key Takeaways

- Modules and packages help you organize code and use code written by others.
- Python’s standard library covers most programming needs.
- Virtual environments and pip make it easy to manage project dependencies.
- Third-party libraries dramatically expand what Python can do!

