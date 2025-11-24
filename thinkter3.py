def fun1(g):
    return g*(g+1)/2
print(fun1(4))
#
def fun2(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
print(fun2(5))
#
def fun3(k):
    s=0
    for i in range(1,k+1):
        for j in range(1,i+1):
            s+=1
    return s
print(fun3(6))