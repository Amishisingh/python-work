#use xor(a^a) is always 0
def check(num1,num2):
    if ((num1^num2) !=0):
        print("numbers are not equal")
    else:
        print("numbers are equal")
#input
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

check(num1,num2)
