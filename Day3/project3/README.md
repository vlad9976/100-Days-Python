# 🏴‍☠️ Day 3 Project – Treasure Hunt Game

This is the final project for **Day 3** of the [100 Days of Code: Python Bootcamp by Angela Yu](https://www.udemy.com/course/100-days-of-code/).  
It’s a text-based decision-making adventure game built using Python conditionals and user input.

---

## 🗂 Project Files

- `project3.py` – Main script for the Treasure Hunt game.

---

## 🚀 How to Run

```bash
python project3.py
```

Follow the prompts to make decisions and navigate through the game.

---

## 🎮 Game Overview

You start on a mysterious island looking for treasure. At each step, you must make a choice:

1. **Left or Right?**
   - `left` ➝ you reach a lake
   - `right` ➝ you fall into a hole (Game Over)

2. **Wait or Swim?**
   - `wait` ➝ you cross the lake safely
   - `swim` ➝ you're eaten by a sea monster (Game Over)

3. **Choose a Door: red, blue, or green**
   - `green` ➝ you find the treasure (🎉 You Win!)
   - `red` ➝ fire room (Game Over)
   - `blue` ➝ flooded room (Game Over)

Invalid inputs at any stage also result in a Game Over.

---

## 🧠 Concepts Practiced

- `input()` for user interaction
- `if/elif/else` conditionals
- Nested condition handling
- Game logic flow
- ASCII art usage for visual appeal

---

## 📸 Sample Output

```text
Welcome To Treasure hunt game! :)
Type 'start' To start the game

Where Would you like to go? Type left OR right:
You came to a lake. What would you do? wait or swim?
You came to a castle with 3 doors. Type red, green, or blue.
🎉 You found the treasure!
```

---

## 💡 Possible Enhancements

- Allow replay after game over
- Add randomness or bonus paths for variety

---

Happy Coding! 🐍
