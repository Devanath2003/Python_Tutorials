
s = input("Enter a string: ")
v = "aeiouAEIOU"
n_str = "".join([ch for ch in s if ch not in v])
print("String after removing vowels:", n_str)
    