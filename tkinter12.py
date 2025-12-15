compri=int(input("enter a number"))
if compri<=1:
        print(compri," is neither prime nor composite number")
else: 
    a=0
    for i in range(2,compri):
        if compri%i==0:
            a+= 1
        else:
            a+= 0
    if a==0:
        print("This no. is a prime number")
    else:
        print("This no. is a composite number")