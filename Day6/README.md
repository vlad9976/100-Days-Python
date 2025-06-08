# 100 Days of Python — Day 6

Today’s focus: **Functions** and the **`while` loop**.  
I practised turning repeated code into reusable functions and controlling program flow with `while`, `break`, and `continue`.

---

## 🗂️ Repository contents

| File           | Purpose                                        |
|----------------|------------------------------------------------|
| `functions.py` | Simple demo showing how to define and call a function. |

*(More example scripts will be added as I keep experimenting!)*

---

## 🧑‍💻 Key concepts & examples

### 1️⃣ Defining and calling a function

```python
def myfunc():
    print("Hello")
    print("Bye")

myfunc()  # -> Hello \n Bye
```

### 2️⃣ Functions with parameters & return values

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

total = add(3, 5)      # 8
print(f"The total is {total}")
```

### 3️⃣ `while` loops for repeated actions

```python
# Countdown timer
count = 5
while count > 0:
    print(count)
    count -= 1
print("Lift‑off!")
```

### 4️⃣ Using `break` and `continue`

```python
# Infinite input loop that stops on 'q'
while True:
    cmd = input("Command (q to quit): ")
    if cmd == "q":
        break         # exit the loop entirely
    if cmd.strip() == "":
        continue      # skip empty commands
    print(f"Running {cmd}…")
```

---

## 🤹‍♂️ What I practised today

* Turning repeated code into **named functions**.
* Understanding **scope** and **return values**.
* Controlling loops with **`while`**, **`break`**, and **`continue`**.
* Accepting **user input** inside a loop.

---

## 🚀 Next improvement ideas

* Add parameter validation and **type hints** to functions.
* Build a small console game (e.g., _Number Guessing_) using a `while` loop.
* Write **unit tests** for the helper functions.

---

## 📝 License

This work is licensed under the **MIT License** — see the [LICENSE](LICENSE) file.

Happy coding! ✨
