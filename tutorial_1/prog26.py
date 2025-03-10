# Program 27
x1, y1 = map(int, input("Enter first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter second point (x2 y2): ").split())

dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Distance: {dist:.2f}")