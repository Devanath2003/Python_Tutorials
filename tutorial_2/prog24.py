
n = int(input("Enter number of elements: "))
nums = []
for _ in range(n):
    num = int(input("Enter number: "))
    if num not in nums:
        nums.append(num)
print("List after removing duplicates:", nums)
    