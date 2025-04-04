class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    # Overload the + operator
    def __add__(self, other):
        # Check if the other operand is also a Complex number
        if not isinstance(other, Complex):
            # Optionally, handle addition with real numbers
            if isinstance(other, (int, float)):
                return Complex(self.real + other, self.imag)
            else:
                return NotImplemented # Indicate operation is not supported
        
        # Perform addition
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        
        # Return a new Complex object with the result
        return Complex(new_real, new_imag)
    
    # Overload the string representation for printing
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}j"
        else:
            return f"{self.real} - {-self.imag}j" # Show minus sign correctly

# Example Usage
c1 = Complex(3, 4)  # Represents 3 + 4j
c2 = Complex(1, -2) # Represents 1 - 2j

print(f"Complex number 1: {c1}")
print(f"Complex number 2: {c2}")

# Use the overloaded + operator
c3 = c1 + c2

print(f"Sum (c1 + c2): {c3}")

# Example of adding a real number (optional based on __add__ implementation)
c4 = c1 + 5
print(f"Sum (c1 + 5): {c4}")