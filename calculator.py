# calculator.py - simple command-line calculator (beginner-friendly)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a number. Try again.")

def main():
    print("Simple calculator. Type q at any prompt to quit.")
    while True:
        a = input("Enter first number (or q to quit): ")
        if a.lower() == 'q':
            print("Goodbye!")
            break
        try:
            a = float(a)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        op = input("Operator (+, -, *, /): ").strip()
        if op not in ('+', '-', '*', '/'):
            print("Operator must be one of +, -, *, /. Try again.")
            continue

        b = input("Enter second number: ")
        try:
            b = float(b)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Cannot divide by zero. Try again.")
                continue
            result = a / b

        print(f"{a} {op} {b} = {result}\n")

if __name__ == "__main__":
    main()
