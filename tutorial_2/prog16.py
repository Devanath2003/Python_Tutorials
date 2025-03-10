
import math

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))
s = 0
for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / fact(2 * i + 1)
    s += term
print("sin(x):", s)
    