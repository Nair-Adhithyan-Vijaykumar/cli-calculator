# ============================================
#  CLI CALCULATOR
#  Author  : Adithyan
#  Skills  : input(), functions, if/else, loops
#  Project : Phase 1 — Foundation
# ============================================


# ── FUNCTIONS ──────────────────────────────

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot mod by zero"
    return a % b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  That's not a valid number. Try again.")


def show_menu():
    print("\n┌─────────────────────────────┐")
    print("│      CLI CALCULATOR  v1.0   │")
    print("├─────────────────────────────┤")
    print("│  1.  Addition       ( + )   │")
    print("│  2.  Subtraction    ( - )   │")
    print("│  3.  Multiplication ( × )   │")
    print("│  4.  Division       ( ÷ )   │")
    print("│  5.  Power          ( ^ )   │")
    print("│  6.  Modulus        ( % )   │")
    print("│  7.  History                │")
    print("│  8.  Clear History          │")
    print("│  0.  Exit                   │")
    print("└─────────────────────────────┘")


def show_history(history):
    if len(history) == 0:
        print("\n  No calculations yet.")
        return
    print("\n── Calculation History ──")
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")
    print("─────────────────────────")


def calculate(choice, a, b):
    """Route to the right function based on user choice."""
    if choice == "1":
        result = add(a, b)
        symbol = "+"
    elif choice == "2":
        result = subtract(a, b)
        symbol = "-"
    elif choice == "3":
        result = multiply(a, b)
        symbol = "×"
    elif choice == "4":
        result = divide(a, b)
        symbol = "÷"
    elif choice == "5":
        result = power(a, b)
        symbol = "^"
    elif choice == "6":
        result = modulus(a, b)
        symbol = "%"
    else:
        return None, None

    return result, symbol


# ── MAIN LOOP ──────────────────────────────

def main():
    history = []

    print("\n  Welcome to CLI Calculator!")
    print("  Built with Python — Phase 1 Project")

    while True:
        show_menu()
        choice = input("\n  Enter choice: ").strip()

        # Exit
        if choice == "0":
            print("\n  Goodbye! Keep building. 🚀\n")
            break

        # History
        elif choice == "7":
            show_history(history)
            continue

        # Clear history
        elif choice == "8":
            history.clear()
            print("\n  History cleared.")
            continue

        # Valid operation choices
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            a = get_number("  Enter first number  : ")
            b = get_number("  Enter second number : ")

            result, symbol = calculate(choice, a, b)

            # Format nicely — remove .0 from whole numbers
            def fmt(n):
                return int(n) if isinstance(n, float) and n == int(n) else n

            if isinstance(result, str):
                # It's an error message
                print(f"\n  ⚠  {result}")
            else:
                display = f"{fmt(a)} {symbol} {fmt(b)} = {fmt(result)}"
                print(f"\n  ✓  {display}")
                history.append(display)

        else:
            print("\n  ⚠  Invalid choice. Enter a number from the menu.")


# ── ENTRY POINT ────────────────────────────

if __name__ == "__main__":
    main()
