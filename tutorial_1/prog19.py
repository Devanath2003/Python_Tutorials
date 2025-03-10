# Program 20
n = int(input("Enter the count of numbers: "))
evens = odds = 0

for _ in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"Evens: {evens}, Odds: {odds}")