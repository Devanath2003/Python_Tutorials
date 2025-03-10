""" Write $thon program using function to generate a dictionary that contains (7)
(i:'i*i) such that i is a number ranging from 1 to 6'?"""

def gen_dict():
    dict={}
    for i in range (1,7):
        dict[i]=i*i;

    return dict

new_dict = gen_dict()
# print(new_dict)

"""  write a Python program to compute.the sum of the series (l- x^2/2!+x^4/4!-x^6/6!
+..........n terms) """

x=int(input("Enter the value for x: "))
n=int(input("Enter the value for range: "))
sum=1

def fact(a):
    if (a==0):
        return 1
    else:
        return a*fact(a-1)
for i in range (1,n+1):
    if i%2 != 0 :
        sum-=x**(2*i)/fact(2*i)
    elif i%2==0:
        sum+=x**(2*i)/fact(2*i)
    
print("The sum is :",sum)



