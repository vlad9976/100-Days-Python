# Day 2 Final Project – Tip Calculator

This is a simple **Tip Calculator** built as the Day 2 final project for the _100 Days of Python_ course by Angela Yu.  
The program calculates how much each person needs to pay when splitting a bill, including a specified tip.

---

## 📝 Project File

- `project2.py` – The Python script implementing the Tip Calculator.

---

## 🚀 How to Run

1. Ensure you have **Python 3** installed.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `project2.py`.
4. Run the script:
   ```bash
   python3 project2.py
   ```
5. Follow the interactive prompts:
   - **Total bill**: Enter the total bill amount (integer).
   - **Tip percentage**: Choose a tip (e.g., 10, 12, or 15).
   - **Number of people**: Enter how many people will split the bill.

---

## 🔧 Example Usage

```
Welcome to Tip calculator :)
What is the total bill? 150
How much tip would you like to give 10,12,15? 12
How many people to split the bill? 3
Each person have to pay: $56.0
```

- In this example:
  - Total bill = $150
  - Tip = 12%
  - Number of people = 3
  - Each person pays = $56.00 (rounded to two decimal places)

---

## 🎯 What I Learned

- Converting user input from `input()` (string) to `int()` for arithmetic.
- Performing percentage calculations and splitting the total among multiple people.
- Formatting output using **f-strings** and **round()** for two decimal places.

---

## 📦 Next Steps

- Add input validation (e.g., ensure numbers are positive).
- Extend functionality to accept decimal bill amounts (use `float`).
- Build a graphical user interface (GUI) version using a library like **Tkinter**.

---

Happy coding! 🐍