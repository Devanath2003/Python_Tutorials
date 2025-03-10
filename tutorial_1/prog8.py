# Program 8
number = int(input("Enter a number: "))
sum_digits = 0

while number > 0:
    sum_digits += number % 10
    number //= 10

print(f"Sum of digits: {sum_digits}")