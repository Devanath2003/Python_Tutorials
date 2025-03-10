
s = input("Enter a string: ")
n = len(s)
pal = True
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        pal = False
        break
if pal:
    print("Palindrome")
else:
    print("Not a palindrome")
    