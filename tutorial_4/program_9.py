import math 

print("""How to instantiate a class:
A class is instantiated by calling the class name followed by parentheses (), 
passing any required arguments defined in the __init__ constructor.
Example: my_object = MyClass(arg1, arg2)
""")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

class RECTANGLE:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner = Point(corner_x, corner_y) # Using the Point class for the corner

    def find_center(self):
        center_x = self.corner.x + self.width / 2
        center_y = self.corner.y + self.height / 2 # Assuming corner_y is the bottom edge
        return Point(center_x, center_y) # Return center as a Point object

    def find_area(self):
        return self.width * self.height

    def find_perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return (f"Rectangle(Width={self.width}, Height={self.height}, "
                f"Bottom-Left Corner={self.corner})")

# Function demonstrating returning an instance
def create_rectangle(h, w, x, y):
    print(f"\nCreating a rectangle with H={h}, W={w}, Corner=({x},{y})")
    instance = RECTANGLE(h, w, x, y)
    return instance # Returning the created instance

# Example Usage
rect_instance = RECTANGLE(height=10, width=20, corner_x=5, corner_y=3)
print(f"\nInstantiated Rectangle: {rect_instance}")

center_point = rect_instance.find_center()
print(f"Center: {center_point}")

area = rect_instance.find_area()
print(f"Area: {area}")

perimeter = rect_instance.find_perimeter()
print(f"Perimeter: {perimeter}")

# Using the function that returns an instance
returned_rect = create_rectangle(7, 15, 0, 0)
print(f"Rectangle returned from function: {returned_rect}")
print(f"Area of returned rectangle: {returned_rect.find_area()}")