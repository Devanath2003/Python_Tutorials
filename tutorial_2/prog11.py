
def dec_to_bin(n):
    b_num = ""
    while n > 0:
        b_num = str(n % 2) + b_num
        n //= 2
    return b_num

n = int(input("Enter decimal number: "))
print("Binary:", dec_to_bin(n))
    