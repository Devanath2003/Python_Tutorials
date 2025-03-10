# Program 19
num = int(input("Enter a number: "))
power = len(str(num))
arm_sum = sum(int(digit) ** power for digit in str(num))

if arm_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")