# Program 7
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("Point is in Quadrant 1")
elif x < 0 and y > 0:
    print("Point is in Quadrant 2")
elif x < 0 and y < 0:
    print("Point is in Quadrant 3")
elif x > 0 and y < 0:
    print("Point is in Quadrant 4")
else:
    print("Point is on the axis")