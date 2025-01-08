import math

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

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")

    while True:
        choice = input("Enter choice (1-10): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            if choice in ['1', '2', '3', '4', '5']:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                try:
                    num1 = float(input("Enter number: "))
                    print(f"Square root of {num1} = {square_root(num1)}")
                except ValueError:
                    print("Invalid input! Please enter a number.")
            elif choice == '7':
                try:
                    num1 = float(input("Enter number: "))
                    base = float(input("Enter base (default is e): ") or "e")
                    print(f"Logarithm of {num1} base {base} = {logarithm(num1, base)}")
                except ValueError:
                    print("Invalid input! Please enter a number.")
            elif choice == '8':
                num1 = float(input("Enter angle in degrees: "))
                print(f"Sine of {num1} = {sine(num1)}")
            elif choice == '9':
                num1 = float(input("Enter angle in degrees: "))
                print(f"Cosine of {num1} = {cosine(num1)}")
            elif choice == '10':
                num1 = float(input("Enter angle in degrees: "))
                print(f"Tangent of {num1} = {tangent(num1)}")
        else:
            print("Invalid choice! Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()