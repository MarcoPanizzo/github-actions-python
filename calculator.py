# calculator.py

def add(x, y):
    """Add two numbers."""
    return x + y

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result}")
