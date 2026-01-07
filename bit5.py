#find power set
import math
def printPowerSet(set,setwise):
    outer=0
    inner=0
    for outer in range(0,2):
        for inner in range(0,2):
        #check if the inner bit in the outer is set if set then print innner element fron the set
            if((outer & (1 << inner))>0):
                print(set[inner],end="")
    print("")
size=int(input("enter any array size : "))
set=[]
for i in range(0,size):
    n=int(input("enter element"))
    set.append(n)
printPowerSet(2,1)
