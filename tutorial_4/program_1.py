class Arith:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def read(self):
        try:
            self.num1 = float(input("Enter first number: "))
            self.num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            self.num1 = 0
            self.num2 = 0

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero"
        else:
            return self.num1 / self.num2

# Example Usage
operation = Arith()
operation.read()

print(f"Number 1: {operation.num1}")
print(f"Number 2: {operation.num2}")
print(f"Sum: {operation.add()}")
print(f"Difference: {operation.subtract()}")
print(f"Product: {operation.multiply()}")
print(f"Quotient: {operation.divide()}")