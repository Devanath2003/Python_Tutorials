
b = input("Enter binary number: ")
dec_num = 0
for i in range(len(b)):
    dec_num = dec_num * 2 + int(b[i])
print("Decimal:", dec_num)
    