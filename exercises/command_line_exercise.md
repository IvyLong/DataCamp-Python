# Command-Line Calculator Exercise

## Overview

Create a command-line calculator that can perform basic mathematical operations using Python's `argparse` module. This exercise will help you understand how to handle command-line arguments effectively.

## Learning Objectives

- Understanding command-line argument parsing
- Working with Python's `argparse` module
- Handling different argument types
- Implementing error handling
- Writing clear help messages

## Basic Requirements

Create a program called `calculator.py` that can:

1. Perform basic math operations (+, -, *, /)
2. Accept numbers as command-line arguments
3. Provide helpful usage messages
4. Handle errors gracefully

## Exercise Tasks

### Task 1: Basic Calculator

Create a calculator that accepts three arguments:

- First number
- Operation (+, -, *, /)
- Second number

Example usage:

```bash
python calculator.py 5 + 3
# Output: 8

python calculator.py 10 * 5
# Output: 50
```

### Task 2: Add Optional Arguments

Add the following optional arguments:

- `--round`: Round the result to N decimal places
- `--verbose`: Show the full equation in the output

Example usage:

```bash
python calculator.py 10 / 3 --round 2
# Output: 3.33

python calculator.py 5 + 3 --verbose
# Output: 5 + 3 = 8
```

### Task 3: Add Multiple Operations

Allow the calculator to perform multiple operations in sequence:

Example usage:

```bash
python calculator.py --sequence 5 + 3 * 2
# Output: 16 (following order of operations)
```

## Starter Code

```python
import argparse

def setup_parser():
    """
    Set up the argument parser with all required and optional arguments.
    """
    # Your code here
    pass

def calculate(args):
    """
    Perform the calculation based on provided arguments.
    """
    # Your code here
    pass

def main():
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

## Testing Cases

Test your program with:

1. Basic operations:

   ```bash
   python calculator.py 5 + 3
   python calculator.py 10 - 5
   python calculator.py 4 * 3
   python calculator.py 15 / 3
   ```

2. Error cases:

   ```bash
   python calculator.py 5 + abc  # Should handle non-numeric input
   python calculator.py 10 / 0   # Should handle division by zero
   python calculator.py          # Should show help message
   ```

3. Optional features:

   ```bash
   python calculator.py 10 / 3 --round 2
   python calculator.py 5 + 3 --verbose
   python calculator.py --sequence 5 + 3 * 2
   ```

## Expected Output Examples

```bash
$ python calculator.py 5 + 3
8

$ python calculator.py 10 / 3 --round 2
3.33

$ python calculator.py 5 + 3 --verbose
Equation: 5 + 3 = 8

$ python calculator.py --help
usage: calculator.py [-h] [--round N] [--verbose] [--sequence] num1 operation num2

A command-line calculator

positional arguments:
  num1          First number
  operation     Operation to perform (+, -, *, /)
  num2          Second number

optional arguments:
  -h, --help    show this help message and exit
  --round N     Round result to N decimal places
  --verbose     Show the full equation
  --sequence    Perform sequence of operations
```

## Bonus Challenges

1. Add support for more operations (power, square root, etc.)
2. Add ability to save calculation history to a file
3. Add support for variables (store results for later use)
4. Implement scientific notation output for large numbers

## Grading Criteria

- Basic functionality (40%)
- Error handling (20%)
- Code organization (20%)
- Documentation (10%)
- Bonus features (10%)

## Tips

1. Use `argparse.ArgumentParser()` to create your parser
2. Add clear help messages for each argument
3. Use appropriate argument types (int, float, str)
4. Handle all possible error cases
5. Follow Python best practices for code organization

## Common Issues to Handle

1. Invalid operations
2. Non-numeric inputs
3. Division by zero
4. Missing arguments
5. Invalid argument combinations

Good luck with your implementation!
