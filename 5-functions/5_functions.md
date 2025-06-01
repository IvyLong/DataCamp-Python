# Python Workshop: Functions

## Learning Objectives

By the end of this section, you will be able to:
- Define and call functions in Python
- Use parameters and arguments to make functions flexible
- Understand default and keyword arguments
- Recognize variable scope and namespaces
- Return values from functions
- Create simple anonymous (lambda) functions
- Write docstrings to document your functions
- Add and understand function annotations

---

## 1. Defining and Calling Functions

Functions are blocks of code designed to do one job, and help you organize and reuse code.

### Defining a Function

```python
def greet():
    print("Hello, world!")
```

### Calling a Function

```python
greet()  # Output: Hello, world!
```

---

## 2. Parameters and Arguments

Functions can accept input values, known as parameters.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!
```
- `name` is a parameter in the function definition.  
- `"Alice"` and `"Bob"` are arguments passed to the function when calling it.

---

## 3. Default Arguments and Keyword Arguments

You can provide default values for parameters.

```python
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()             # Hello, friend!
greet("Charlie")    # Hello, Charlie!
```

You can also use **keyword arguments** to specify parameters by name, making calls more readable.

```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce(age=25, name="Dina")  # Dina is 25 years old.
```

---

## 4. Variable Scope and Namespaces

Variables created inside a function are **local** to that function.

```python
def show_number():
    number = 5
    print(number)

show_number()    # Output: 5
# print(number)  # This would cause an error! 'number' only exists inside the function.
```

#### Global Variables

Variables defined outside functions are **global** and can be read inside a function, but need a special keyword to be modified.

```python
count = 10

def increment():
    global count
    count += 1

increment()
print(count)   # Output: 11
```

---

## 5. Return Values

Functions can send back (return) results using the `return` statement.

```python
def add(a, b):
    return a + b

sum_result = add(3, 4)
print(sum_result)  # Output: 7
```

You can even return multiple values as a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([7, 4, 10])
print(low, high)  # Output: 4 10
```

---

## 6. Lambda Functions

Lambda functions are small anonymous functions, useful for short, simple operations.

```python
# Regular function
def square(x):
    return x * x

# Lambda equivalent
square = lambda x: x * x
print(square(5))   # Output: 25

# Using with built-in functions (e.g., sorted)
nums = [2, 4, 1, 3]
print(sorted(nums, key=lambda x: -x))  # [4, 3, 2, 1]
```

---

## 7. Documentation Strings (Docstrings)

Docstrings are special strings at the start of a function to describe what it does.

```python
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.

    Parameters:
    a (int or float): First number.
    b (int or float): Second number.

    Returns:
    int or float: Product of a and b.
    """
    return a * b

help(multiply)  # Displays the docstring
```

---

## 8. Function Annotations

Annotations let you specify the expected types of a function’s parameters and return value. They are for hinting; Python won’t enforce them.

```python
def subtract(a: int, b: int) -> int:
    return a - b

result = subtract(10, 3)
print(result)  # 7

# You can access annotations with:
print(subtract.__annotations__)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

---

## Exercises

### 1. Define and Call Functions
- Write a function called `say_hello()` that prints "Hello, learner!"
- Call the function.

### 2. Parameters & Arguments
- Write a function called `goodbye(name)` that prints "Goodbye, [name]".
- Call it with your name and a friend’s name.

### 3. Default and Keyword Arguments
- Modify `goodbye` so that if no name is given, it says "Goodbye, friend".
- Call it without an argument and with an argument.

### 4. Variable Scope
- Write a function that sets a variable `x` inside itself and prints it.  
- Try printing `x` outside the function (should cause an error).

### 5. Return Values
- Make a function `double(n)` that returns its argument times two.  
- Print its return value for `n = 5`.

### 6. Lambda Functions
- Write a lambda that returns the cube of a number (x³) and call it with 3.

### 7. Docstrings
- Add a docstring to `double(n)` that explains what it does.

### 8. Function Annotations
- Annotate `double(n)` to show that `n` and its return value are both integers.

---

## Key Takeaways

- Functions let you organize and reuse code.
- Parameters and arguments make your functions flexible.
- Scope helps you avoid variable name conflicts.
- Lambda functions are great for short, simple operations.
- Docstrings and annotations help document and clarify your code.

