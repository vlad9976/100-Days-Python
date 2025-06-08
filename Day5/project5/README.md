# Password Generator (v1)

_A mini‑project from **Day 5** of my **100 Days of Python** journey._

This simple **command‑line Password Generator** lets you specify how many **letters**, **symbols**, and **numbers** you want in a password, then builds and shuffles those characters to produce a random result.

---

## 📂 File

| File          | Description                                |
|---------------|--------------------------------------------|
| `project5.py` | Interactive password generator script.     |

---

## 🏁 Quick start

```bash
# Clone or download this repository
git clone https://github.com/<your‑user>/password‑generator.git
cd password‑generator

# Run the script with Python 3
python project5.py
```

You will be prompted for the number of letters, symbols, and numbers:

```text
Welcome to password generator
How many letters would you like in your password? 6
How many symbols would you like in your password? 3
How many numbers would you like in your password? 2
bqK#4$P7!a
```

*(Your output will vary — that’s the point!)*

---

## ⚙️ How it works

1. **Character pools** — three lists: `letters`, `numbers`, and `symbols`.
2. **User input** determines how many characters to select from each pool.
3. `random.choice()` picks characters; the selections are stored in `password`.
4. `random.shuffle()` mixes the order.
5. The list is joined into a single string and printed.

> **Note:** This script is for educational purposes and **not suitable for production‑grade cryptography**. The Python `random` module is not cryptographically secure.

---

## 🚀 Ideas for next iterations

* Wrap logic in a function and add **type hints**.
* Use `secrets.choice()` for cryptographically secure randomness.
* Replace interactive prompts with a **CLI interface** using `argparse`.
* Add unit tests with **pytest**.
* Package and upload to **PyPI**.

---

## 📝 License

Released under the **MIT License** — see the [`LICENSE`](LICENSE) file.

Happy password generating! 🔐
