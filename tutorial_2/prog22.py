
n = int(input("Enter number of elements: "))
nums = sorted([int(input("Enter number: ")) for _ in range(n)])
m = n // 2
print("Median:", (nums[m] if n % 2 == 1 else (nums[m - 1] + nums[m]) / 2))
    