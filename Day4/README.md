# 📅 100 Days of Python – Day 4: Randomization & Python Lists

Welcome to **Day 4** of the *100 Days of Code: The Complete Python Pro Bootcamp* by Angela Yu.  
Today we explore Python lists, randomization using the `random` module, nested data structures, and simple modules.

---

## 🧠 Topics Covered

- **Python Lists**
  - Creating and accessing list elements
  - Updating and manipulating lists (`list.py`)
  - Nesting lists (`nested-list.py`)

- **Randomization**
  - Generating random numbers and selections (`randomization_mod.py`, `heads_or_tails.py`)
  - Using `random.choice()` and `random.randint()`

- **Modules**
  - Understanding and importing Python modules (`module.py`, `my_module.py`)

- **Practical Program: Tip Calculator**
  - Calculate split bills with percentage tip (`bill_pay.py`)

---

## 📁 File Overview

| Filename              | Description                                                                              |
|-----------------------|------------------------------------------------------------------------------------------|
| `list.py`             | Demonstrates basic list creation and manipulation                                        |
| `nested-list.py`      | Shows how to create and navigate nested lists                                            |
| `randomization_mod.py`| Uses `random` module to simulate behavior (e.g., who pays the bill)                      |
| `heads_or_tails.py`   | Simulates a coin flip using `random`                                                    |
| `module.py`           | Demonstrates how to use a custom module                                                  |
| `my_module.py`        | A sample custom module containing constants                                              |
| `bill_pay.py`         | A simple tip calculator that splits the bill among people                               |

---

## 🧪 Code Snippets

### Example: Heads or Tails (`heads_or_tails.py`)
```python
import random
flip = random.randint(0, 1)
if flip == 1:
    print("Heads")
else:
    print("Tails")
```

### Example: Tip Calculator (`bill_pay.py`)
```python
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

split = round((bill + (bill * (tip / 100))) / people, 2)
print(f"Each person should pay: ${split}")
```

---

## 🔁 Summary

Day 4 is about understanding one of the most versatile data structures in Python — the **list**, and using randomization for fun and useful programs. You also learned how to build your own module and apply that knowledge to real-world scenarios like tipping or coin flipping.

---
