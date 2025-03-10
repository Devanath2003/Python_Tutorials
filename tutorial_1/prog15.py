# Program 15
print("Prime numbers less than 1000:")
for num in range(2, 1000):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")