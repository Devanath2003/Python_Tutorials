class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0.0

    def get_details(self):
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Author Name: ")
        try:
            self.cost = float(input("Enter Cost: "))
        except ValueError:
            print("Invalid cost. Setting cost to 0.")
            self.cost = 0.0

    def print_details(self):
        print("\n--- Book Details ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Cost: ${self.cost:,.2f}")

# Example Usage
book1 = Book()

book1.get_details()
book1.print_details()