class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0.0

    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:,.2f}")

# Example Usage
my_mobile = Mobile()

print("Setting mobile details...")
my_mobile.set_details("Samsung", "Galaxy S23", 999.99)

print("\nDisplaying mobile details:")
my_mobile.display_details()