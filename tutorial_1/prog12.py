# Program 12
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(4)]
positive_sum = sum(num for num in numbers if num > 0)
negative_sum = sum(num for num in numbers if num < 0)
positive_count = sum(1 for num in numbers if num > 0)
negative_count = sum(1 for num in numbers if num < 0)

positive_avg = positive_sum / positive_count if positive_count > 0 else 0
negative_avg = negative_sum / negative_count if negative_count > 0 else 0

print(f"Sum of positive numbers: {positive_sum}, Average: {positive_avg:.2f}")
print(f"Sum of negative numbers: {negative_sum}, Average: {negative_avg:.2f}")