Here's the revised section on Exception Handling:

# Python Workshop: Exception Handling

## Learning Objectives

By the end of this section, you will be able to:
- Use try, except, else, and finally blocks to manage exceptions
- Raise exceptions intentionally within your code
- Create and utilize custom exceptions tailored to your application
- Implement debugging techniques to identify and fix issues
- Handle multiple exceptions in a single try-except block

---

## 1. Using Try, Except, Else, and Finally Blocks

Python's exception handling uses `try`, `except`, `else`, and `finally` to manage errors and ensure clean execution.

### Basic Try-Except Block

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer.")
```

### Using Else and Finally

- **`else`**: Runs if no exceptions were raised.
- **`finally`**: Executes no matter what, often used for cleanup.

```python
try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print("The file was not found.")
else:
    content = file.read()
    print(content)
finally:
    if 'file' in locals():
        file.close()
    print("Executed whether exception occurred or not")
```

---

## 2. Raising Exceptions

Raising exceptions can help signal unexpected conditions in your code logic.

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age is: {age}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```

---

## 3. Custom Exceptions

Custom exceptions are created by defining a new class derived from `Exception`.

```python
class InvalidAgeError(Exception):
    pass

def register_voter(age):
    if age < 18:
        raise InvalidAgeError("Voter must be at least 18 years old.")
    print("Voter registered successfully.")

try:
    register_voter(16)
except InvalidAgeError as e:
    print(e)
```

---

## 4. Debugging Techniques

### Using Print Statements

Strategically place `print` statements to track variable values and control flow.

### Using a Debugger

Use Python debuggers like `pdb` to step through code.

```bash
python -m pdb myscript.py
```

### Logging

Use the `logging` module for more organized tracking.

```python
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logging.info('This message provides insight into execution')
```

---

## 5. Handling Multiple Exceptions

You can capture multiple exceptions in one block using parentheses.

```python
try:
    index = int(input("Enter index: "))
    lst = [10, 20, 30]
    print(lst[index])
except (IndexError, ValueError) as e:
    print(f"An error occurred: {e}")
```

---

## Exercises

1. **Try, Except, Else, Finally**
    - Write a function that opens a file specified by the user. Use try-except to handle file not found errors, and finally to ensure the file is closed.

2. **Raising Exceptions**
    - Create a function to check temperature input. Raise an exception if the temperature is below absolute zero.

3. **Custom Exceptions**
    - Develop a custom exception for invalid user input in a form with specific conditions.

4. **Debugging Techniques**
    - Use the `logging` module to insert debug-level logs in a simple script performing mathematical calculations.

5. **Handling Multiple Exceptions**
    - Modify a list index and division program to handle out-of-bounds and division by zero errors in one block.

---

## Key Takeaways

- Exception handling with try-except blocks is crucial for managing errors.
- Raising and customizing exceptions helps address application-specific conditions.
- Debugging through print statements, logging, and debuggers provides insights into program behavior.
- Handling multiple exceptions allows for more robust error management in complex code.