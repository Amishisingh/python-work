def power4(num):
    count=0
    if ((num &(~(num-1)))==num):
        while(num>1):
            num>>=1
            count+=1
    if count%2==0:
        return True
    else:
        return False
num=int(input("enter a num"))
if(power4(num)):
    print("\nThe number is of power 4")
else:
    print("\nThe number is not a power of 4")

