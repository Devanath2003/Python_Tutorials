
n = int(input("Enter number of elements: "))
nums = list(set(int(input("Enter number: ")) for _ in range(n)))
print("List after removing duplicates:", nums)
    