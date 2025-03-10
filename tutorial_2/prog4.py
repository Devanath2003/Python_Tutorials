
s = input("Enter a string: ")
if " " in s:
    n_str = s.replace(" ", "*")
else:
    n_str = "$" + s + "$"
print("Modified string:", n_str)
    