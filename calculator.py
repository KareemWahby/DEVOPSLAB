# calculator.py

class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""

    def add(self, x, y):
        """Adds two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtracts the second number from the first."""
        return x - y

    def multiply(self, x, y):
        """Multiplies two numbers."""
        return x * y

    def divide(self, x, y):
        """Divides the first number by the second. Returns a float."""
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

if __name__ == '__main__':
    calc = Calculator()
    
    # Example usage:
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

    # Example of an error
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")
