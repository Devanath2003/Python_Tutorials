# Program 28
import math

a, b, c = map(float, input("Enter a, b, c: ").split())

d = b ** 2 - 4 * a * c
if d >= 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Roots: {r1:.2f}, {r2:.2f}")
else:
    print("No real roots")