
s = input("Enter a string: ")
n_str = "".join([ch.upper() if 'a' <= ch <= 'z' else ch for ch in s])
print("Uppercase string:", n_str)
    