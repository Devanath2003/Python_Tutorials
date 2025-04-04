class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary:,.2f}")

# Example Usage
person1 = Person("Charlie", 30, 60000)
person2 = Person("Diana", 25, 75000)

print("Details for person 1:")
person1.display()

print("\nDetails for person 2:")
person2.display()