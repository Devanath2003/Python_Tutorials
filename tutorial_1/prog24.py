# Program 25
for num in range(100, 1001):
    if sum(int(digit) for digit in str(num)) % 9 == 0:
        print(num, end=" ")