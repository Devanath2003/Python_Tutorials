
import re

s = input("Enter password: ")
if (len(s) >= 6 and 
    re.search("[a-z]", s) and 
    re.search("[A-Z]", s) and 
    re.search("[0-9]", s) and 
    re.search("[$#@]", s)):
    print("Valid Password")
else:
    print("Invalid Password")
    