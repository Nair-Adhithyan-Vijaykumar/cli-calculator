# 🧮 CLI Calculator

A command-line calculator built in Python as part of my Python learning journey.

---

## 📚 About

This is a **Phase 1 Foundation Project** — one of the first Python projects I built while learning the language. It covers core beginner concepts like functions, loops, conditionals, and user input handling.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with divide-by-zero protection)
- ^ Power / Exponentiation
- % Modulus (with mod-by-zero protection)
- 📜 Calculation history — view all past results in a session
- 🗑️ Clear history
- ✅ Input validation — handles non-numeric input gracefully

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed — [Download here](https://www.python.org/downloads/)

### Run the calculator

```bash
python calculator.py
```

---

## 🖥️ Usage

When you run the script, you'll see a menu like this:

```
┌─────────────────────────────┐
│      CLI CALCULATOR  v1.0   │
├─────────────────────────────┤
│  1.  Addition       ( + )   │
│  2.  Subtraction    ( - )   │
│  3.  Multiplication ( × )   │
│  4.  Division       ( ÷ )   │
│  5.  Power          ( ^ )   │
│  6.  Modulus        ( % )   │
│  7.  History                │
│  8.  Clear History          │
│  0.  Exit                   │
└─────────────────────────────┘
```

Just enter the number of the operation you want, then input your two numbers. Results are saved to history for the session.

---

## 🧠 Concepts Practiced

| Concept | Where it's used |
|---|---|
| `functions` | Each operation has its own function |
| `if / elif / else` | Menu routing and error handling |
| `while` loops | Main program loop and input validation |
| `try / except` | Catching invalid number input |
| `lists` | Storing calculation history |
| `f-strings` | Formatting output |
| `input()` | Getting user input |

---

## 📁 Project Structure

```
calculator.py   # Main script — all logic lives here
README.md       # You're reading it!
```

---

## 🛣️ What's Next

This is Phase 1. Future phases may include:

- [ ] Square root and logarithm support
- [ ] Save history to a `.txt` file
- [ ] Unit converter
- [ ] GUI version with `tkinter`

---

## 👨‍💻 Author

**Adithyan** — learning Python, one project at a time.
