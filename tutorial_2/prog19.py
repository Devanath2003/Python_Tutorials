
n = int(input("Enter number of names: "))
names = [input("Enter name: ") for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if names[i] > names[j]:
            names[i], names[j] = names[j], names[i]
print("Sorted names:", names)
    