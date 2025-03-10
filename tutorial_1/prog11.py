# Program 11
n = int(input("Enter a positive integer: "))
sum_cubes = sum(i**3 for i in range(2, n+1, 2))

print(f"Sum of cubes of even numbers: {sum_cubes}")