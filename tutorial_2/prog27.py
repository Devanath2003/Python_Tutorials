
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]
bubble_sort(nums)
print("Sorted list:", nums)
    