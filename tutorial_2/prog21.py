
s = input("Enter string: ")
word = input("Enter word to remove: ")
print("Modified string:", " ".join(w for w in s.split() if w != word))
    