
from collections import Counter

n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]
count = Counter(nums)
mode = max(count, key=count.get)
print("Mode:", mode)
    