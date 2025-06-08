# Reeborg’s World — Universal Hurdle & Maze Solver

This **single script** solves **all hurdle challenges** (_Hurdle 1–4_ & _Hurdle Race_) **and the Maze world** in Reeborg’s World (the Blockly / Python practice site used in **Day 6** of _100 Days of Python_).

---

## 📂 File

| File        | Description                                        |
|-------------|----------------------------------------------------|
| `project6.py` | Right‑hand‑rule algorithm that handles every hurdle course **and** the Maze in one go. |

---

## 🚀 How to run

1. **Open Reeborg’s World** in your browser: <https://reeborg.ca/reeborg.html>.
2. Click **Choose World** and pick any of these:  
   * _Hurdle 1_ • _Hurdle 2_ • _Hurdle 3_ • _Hurdle 4_  
   * _Hurdle Race_  
   * _Maze_
3. Switch the language to **Python** (top‑right drop‑down).
4. Copy–paste the contents of **`project6.py`** into the code editor.
5. Hit **Run** ▶️.

Reeborg will navigate the course and stop on the goal flag without modifying a single line between worlds.

---

## 🧠  How it works

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():        # path ahead?
        move()                  # take the step
        turn_right()            # try to turn right (keep right hand on wall)
    elif wall_in_front():       # dead‑end: wall ahead
        turn_left()             # follow the wall on the left
```

* **Right‑hand rule** — by always attempting a right turn after each move, Reeborg keeps its “right hand” on the wall, which guarantees reaching the goal in simply‑connected mazes.
* **Universal hurdles** — a hurdle is just a one‑cell wall. The same logic that follows the wall lets Reeborg climb up, move over, and descend, no matter how many hurdles appear.

---

## 🎓  Lessons learned

* Encapsulating repeated actions into functions (`turn_right`).
* Using **`while not at_goal()`** to create a loop that adapts to any world.
* Combining **conditional checks** (`front_is_clear()`, `wall_in_front()`) to build a simple but powerful navigation algorithm.

---

## 💡  Possible upgrades

* Detect and handle **taller hurdles** (>1 cell high).
* Add a **step counter** to measure path efficiency.
* Visualize the path taken by logging coordinates.
* Refactor into a class (`ReeborgBot`) for cleaner code reuse.

---

## 📝 License

This code is provided for educational purposes under the **MIT License**.

Happy problem‑solving! 🤖✨
