
def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

while True:
    print("\n1. Check Even/Odd\n2. Check Positive/Negative/Zero\n3. Generate Factors\n4. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        num = int(input("Enter number: "))
        print("Even" if num % 2 == 0 else "Odd")
    elif ch == 2:
        num = int(input("Enter number: "))
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")
    elif ch == 3:
        num = int(input("Enter number: "))
        factors(num)
    elif ch == 4:
        break
    else:
        print("Invalid Choice!")
    