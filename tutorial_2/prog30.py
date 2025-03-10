
from collections import Counter

n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]
count = Counter(nums)
unique_nums = [num for num in nums if count[num] == 1]
print("List with only unique elements:", unique_nums)
    