# 📅 100 Days of Python – Day 3: Control Flow (if, elif, else)

Welcome to **Day 3** of the *100 Days of Code: The Complete Python Pro Bootcamp* by Angela Yu.  
Today’s focus: **Control flow** in Python using `if`, `elif`, and `else` statements, as well as logical operators and basic programming logic.

---

## 🧠 Topics Covered

- **Conditional Statements**  
  - `if`, `elif`, and `else` blocks (`if-else.py`, `Nested if.py`, `nested elif.py`)  
  - Comparison operators (`<`, `<=`, `>`, `>=`, `==`, `!=`)

- **Logical Operators**  
  - Combining conditions with `and`, `or`, `not` (`logical operators.py`)

- **Modulo Operator**  
  - Checking divisibility and remainders (`Modulo.py`)

- **BMI Classification**  
  - Using `if-elif-else` to categorize BMI values (`bmi calc.py`)

- **Practical Example: Pizza Ordering**  
  - Building a program that calculates price depending on choices (`pizza delivery program.py`)

---

## 📁 File Overview

| Filename                   | Description                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------------------|
| `if-else.py`               | Basic `if-else` to check height eligibility                                                      |
| `Nested if.py`             | Simple nested `if` to check height and age for ticket pricing                                     |
| `nested elif.py`           | Nested `if-elif-else` structure to calculate bill based on height and age, with optional photo    |
| `logical operators.py`     | Example combining logical conditions to set ticket pricing and extras                              |
| `Modulo.py`                | Demonstrates `%` operator for remainder and checks if a number is odd or even                     |
| `bmi calc.py`              | Calculates BMI and classifies weight status                                                        |
| `pizza delivery program.py`| Interactive program that calculates pizza bill based on size, pepperoni, and extra cheese choices |

---

## 🧪 Code Examples

### Basic `if-else` (`if-else.py`)
```python
h = int(input("What is your height in CM? "))
if h < 120:
    print("Sorry you are not allowed")
else:
    print("Hope on")