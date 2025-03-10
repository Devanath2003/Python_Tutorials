
A = set(map(int, input("Enter elements of set A: ").split()))
B = set(map(int, input("Enter elements of set B: ").split()))
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Symmetric Difference:", A ^ B)
    