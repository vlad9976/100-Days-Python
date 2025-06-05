# 📅 100 Days of Python – Day 2: Numbers, Math, and Type Conversion

Welcome to **Day 2** of the *100 Days of Code: The Complete Python Pro Bootcamp* by Angela Yu.  
Today’s focus: understanding Python’s basic data types, arithmetic operations, and type conversions.

---

## 🧠 Topics Covered

- **Integers & Floats**  
  - Integer literals, large numbers with underscores (`Integers.py`)  
  - Floating-point numbers and precision (`Floats.py`)  
  - Rounding with `round()` and floor division (`round.py`)

- **Mathematical Operations & PEMDAS**  
  - Addition, subtraction, multiplication, division, exponentiation (`mathematics.py`)  
  - Order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

- **Strings & Subscripting**  
  - Accessing individual characters using indices (`Strings.py`)  
  - Formatted string literals (f-strings) (`f-string.py`)

- **Booleans**  
  - `True` and `False` values (`boolians.py`)

- **Type Checking & Conversion**  
  - Using `type()` to inspect data types (`type.py`)  
  - Converting between strings, integers, and floats (`type casting.py`)

---

## 📁 File Overview

| Filename               | Description                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| `Integers.py`          | Demonstrates integer operations and usage of underscores for readability.                                   |
| `Floats.py`            | Shows basic floating-point numbers and output.                                                              |
| `round.py`             | Examples of rounding a float to an integer or specified decimal places.                                     |
| `mathematics.py`       | Arithmetic expressions, BMI calculation, and order of operations (PEMDAS).                                  |
| `Strings.py`           | String indexing (subscripting) to retrieve characters from a string.                                        |
| `f-string.py`          | Examples of formatted string literals (f-strings) for embedding variables in strings.                       |
| `boolians.py`          | Prints boolean values `True` and `False`.                                                                   |
| `type.py`              | Demonstrates the `type()` function to identify data types (`bool`, `int`, `str`, `float`).                 |
| `type casting.py`      | Shows converting a string to an integer, and converting input for user prompts to strings or integers.     |

---

## 🧪 Code Examples

### Integers (`Integers.py`)
```python
# Whole Numbers
print(123 + 123)

# Large Numbers with underscores
print(123_12)  # 12312
```

---

### Floats (`Floats.py`)
```python
# Floating-point number
print(32.21)
```

---

### Rounding (`round.py`)
```python
height = 1.65
weight = 84
bmi = weight / (height ** 2)

print(round(bmi))      # Rounded to nearest integer
print(round(bmi, 2))   # Rounded to two decimal places
```

---

### Mathematics & PEMDAS (`mathematics.py`)
```python
# Basic arithmetic
print(3 * 3 + 3 / 3 - 3)  # Evaluates with PEMDAS rules

# BMI Calculator
height = 1.65
weight = 84
bmi = weight / (height ** 2)
print(bmi)
```

---

### Strings & Indexing (`Strings.py`)
```python
print("Hello"[0])   # H
print("Hello"[-1])  # o
```

---

### f-Strings (`f-string.py`)
```python
score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}, height is {height}, winning: {is_winning}")
```

---

### Booleans (`boolians.py`)
```python
print(True)
print(False)
```

---

### Type Checking (`type.py`)
```python
print(type(True))     # <class 'bool'>
print(type(123))      # <class 'int'>
print(type("123"))    # <class 'str'>
print(type(12.12))    # <class 'float'>
```

---

### Type Casting (`type casting.py`)
```python
# Convert string to integer
print(int("123") + int("132"))  # 255

# Convert input length to string and print
user_name = str(len(input("Enter your name: ")))
print("Number of letters in your name: " + user_name)
```

---

## ✅ Summary & Next Steps

- **Key Takeaways:**  
  - Understanding Python’s numeric and boolean types  
  - Performing arithmetic operations and respecting operator precedence  
  - Working with strings and f-strings for formatting  
  - Checking types with `type()` and converting types with casting functions  

- **Tomorrow’s Focus (Day 3):**  
  - Control flow: `if` statements, loops (`for`, `while`), and logical operators.

Stay tuned for **Day 3** where we’ll dive into decision-making and loops in Python!