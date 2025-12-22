#retur n if even else odd
def isEvenOod(n):
    #XOR with 1 equals n+1
    if (n^1==n+1):
        return True;
    else:
        return False;
num=int(input("enter a number : "))
if isEvenOod(num):
    print(num,"is EVEN")
else:
    print(num,"is Ood")
