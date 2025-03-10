
n = int(input("Enter number of elements: "))
ints, floats, strs = [], [], []
for _ in range(n):
    val = input("Enter value: ")
    if val.isdigit():
        ints.append(int(val))
    elif '.' in val and val.replace('.', '').isdigit():
        floats.append(float(val))
    else:
        strs.append(val)
print("Integers:", ints)
print("Floats:", floats)
print("Strings:", strs)
    