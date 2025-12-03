number=int(input("enter a number"))
digits=len(str(number))
result=0
temp=number
while temp>0:
    digit=temp % 10
    result += digit**digits
    temp //= 10
if number==result:
    print("number is a armstrong number")
else:
    print("number is not a armstrong number")