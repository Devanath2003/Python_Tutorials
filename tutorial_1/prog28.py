# Program 29
low, high = map(int, input("Enter lower and upper limit: ").split())
sum_odd = sum(num for num in range(low, high + 1) if num % 2 != 0)

print(f"Sum of odd numbers: {sum_odd}")