
s = input("Enter a string: ")
n_str = "".join([s[i] for i in range(len(s)) if i % 2 == 0])
print("Modified string:", n_str)
    