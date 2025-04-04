class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print(f"Rectangle created with length {self.length} and width {self.width}")

    def area(self):
        return self.length * self.width

# Example Usage
rect1 = Rectangle(10, 5)
area1 = rect1.area()
print(f"The area of rect1 is: {area1}")

rect2 = Rectangle(7.5, 3)
area2 = rect2.area()
print(f"The area of rect2 is: {area2}")