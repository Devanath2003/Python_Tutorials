# Program 24
num = int(input("Enter a number: "))
print("Prime factors:", end=" ")

for i in range(2, num + 1):
    while num % i == 0:
        print(i, end=" ")
        num //= i