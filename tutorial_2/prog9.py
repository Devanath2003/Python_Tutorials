
s = input("Enter a string: ")
n = len(s)
mid = n // 2
first_half = s[:mid][::-1]
second_half = s[mid:][::-1]
print("Modified string:", first_half + second_half)
    