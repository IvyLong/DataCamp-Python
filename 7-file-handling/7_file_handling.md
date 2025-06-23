Here is the content for a section on file handling in your Python course, designed for beginner to intermediate learners:

# Python Workshop: File Handling

## Learning Objectives

By the end of this section, you will be able to:
- Open and read from files in Python
- Write data to files
- Use context managers to ensure files are properly opened and closed
- Understand different file modes and their use cases
- Handle exceptions related to file operations

---

## 1. Introduction to Files

Python makes it easy to work with files. Files can be text files or binary files and are used for storing data permanently.

### Different Modes for Opening Files

- **'r'**: Read (default)
- **'w'**: Write (overwrites the file if it exists)
- **'a'**: Append (adds to the end without overwriting)
- **'b'**: Binary mode (use with other modes, e.g., 'rb', 'wb')

---

## 2. Reading from Files

### Basic File Reading

To read from a file, you can use the `open` function and read methods:

```python
file = open('example.txt', 'r')
content = file.read()  # Reads the whole file
print(content)
file.close()
```

### Reading Line by Line

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Strip removes leading/trailing whitespace
```

### Using `with` Statement

The `with` statement is preferred because it automatically closes the file:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

---

## 3. Writing to Files

### Writing Data to a File

```python
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Python is great for file handling.\n")
```

This will create or overwrite `output.txt` with the given content.

### Appending Data

```python
with open('output.txt', 'a') as file:
    file.write("This line is appended to the file.\n")
```

This adds to the end of `output.txt`.

---

## 4. Working with Different File Types

### Binary Files

Reading binary files (like images) uses `'b'` mode:

```python
with open('image.jpg', 'rb') as file:
    content = file.read()
    # Do something with the binary data
```

### JSON Files

Reading and writing JSON files often involves Python's `json` module:

```python
import json

# Writing JSON data
data = {'name': 'Bob', 'age': 25}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading JSON data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)
```

---

## 5. Exception Handling in File Operations

Use try-except blocks to handle potential errors in file operations:

```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An I/O error occurred.")
```

---

## Exercises

1. **Reading from a File**
    - Create a text file called `sample.txt` with several lines of text.
    - Write a Python program to read and print each line from the file.

2. **Writing to a File**
    - Write a program that prompts a user for their name and saves it to a file `usernames.txt`.
    - Each new name should be appended to the file, not overwrite existing entries.

3. **Working with JSON**
    - Create a dictionary with some personal information.
    - Write it to a `info.json` file using the `json` module.
    - Read the data back from the `info.json` file and print it.

4. **Binary File Handling**
    - Write a program to read an image file in binary mode and print the size of the read data.

5. **Exception Handling**
    - Create a Python program that tries to read from a file that doesn’t exist and gracefully handles the error, printing a custom message.

---

## Key Takeaways

- Python’s built-in file handling makes it easy to work with files for reading and writing.
- Use context managers (`with` statement) for safer file handling.
- The JSON module helps with reading and writing JSON data.
- Always handle exceptions in file operations to make your programs robust.