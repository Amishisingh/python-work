def power2(num):
    if (num==0):
        return 0
    if ((num &(~(num-1)))==num):
        return 1
    return 0
num=int(input("ener a num"))
if(power2(num)):
    print("\nThe number is of power 2")
else:
    print("\nThe number is not a power of 2")

#
number=int(input("enter a num"))
for i in range(0,number):
    if 2**i==number :
        print(number," is of power:",i,"raise to 2")
