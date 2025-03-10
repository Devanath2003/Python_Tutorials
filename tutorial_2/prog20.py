
n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]
print("Sum of even numbers:", sum(num for num in nums if num % 2 == 0))
    