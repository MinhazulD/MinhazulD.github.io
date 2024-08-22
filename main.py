import tkinter as tk

# Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Fibonacci Function
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Calculator GUI
def show_calculator():
    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            if choice.get() == '1':
                result.set(f"The result is: {add(num1, num2)}")
            elif choice.get() == '2':
                result.set(f"The result is: {subtract(num1, num2)}")
            elif choice.get() == '3':
                result.set(f"The result is: {multiply(num1, num2)}")
            elif choice.get() == '4':
                result.set(f"The result is: {divide(num1, num2)}")
            else:
                result.set("Invalid choice")
        except ValueError:
            result.set("Invalid input")

    calculator_window = tk.Toplevel(root)
    calculator_window.title("Simple Calculator")

    tk.Label(calculator_window, text="Enter first number:").pack()
    entry1 = tk.Entry(calculator_window)
    entry1.pack()

    tk.Label(calculator_window, text="Enter second number:").pack()
    entry2 = tk.Entry(calculator_window)
    entry2.pack()

    tk.Label(calculator_window, text="Select operation:").pack()
    choice = tk.StringVar()
    tk.Radiobutton(calculator_window, text="Add", variable=choice, value='1').pack()
    tk.Radiobutton(calculator_window, text="Subtract", variable=choice, value='2').pack()
    tk.Radiobutton(calculator_window, text="Multiply", variable=choice, value='3').pack()
    tk.Radiobutton(calculator_window, text="Divide", variable=choice, value='4').pack()

    tk.Button(calculator_window, text="Calculate", command=calculate).pack()

    result = tk.StringVar()
    tk.Label(calculator_window, textvariable=result).pack()

# Fibonacci GUI
def show_fibonacci():
    def display_fibonacci():
        try:
            n = int(entry.get())
            if n < 1:
                result.set("Enter a positive integer")
            else:
                sequence = fibonacci(n)
                result.set(", ".join(map(str, sequence)))
        except ValueError:
            result.set("Enter a valid integer")

    fibonacci_window = tk.Toplevel(root)
    fibonacci_window.title("Fibonacci Sequence Generator")

    tk.Label(fibonacci_window, text="Enter a number:").pack()
    entry = tk.Entry(fibonacci_window)
    entry.pack()

    tk.Button(fibonacci_window, text="Generate Fibonacci", command=display_fibonacci).pack()

    result = tk.StringVar()
    tk.Label(fibonacci_window, textvariable=result).pack()

# Main GUI
root = tk.Tk()
root.title("Main Menu")

tk.Button(root, text="Open Calculator", command=show_calculator).pack()
tk.Button(root, text="Open Fibonacci Generator", command=show_fibonacci).pack()

root.mainloop()
