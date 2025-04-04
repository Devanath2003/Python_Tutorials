class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def dataprint(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

# Example Usage
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

print("Details for student 1:")
student1.dataprint()

print("\nDetails for student 2:")
student2.dataprint()