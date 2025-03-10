
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print("nCr:", fact(n) // (fact(r) * fact(n - r)))
    