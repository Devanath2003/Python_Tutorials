class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"The price of the {self.year} {self.model} is: ${self.price:,.2f}")

# Example Usage
car1 = Car("Toyota Camry", 2021, 25000)
car2 = Car("Honda Civic", 2022, 23000)

print("Details for car 1:")
car1.cost()

print("\nDetails for car 2:")
car2.cost()