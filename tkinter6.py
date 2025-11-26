def onsquaretime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
            iteration+=1
        print("")
    print("when n is",n,"iteration=",iteration,"\n")
onsquaretime(5)
onsquaretime(4)
onsquaretime(3)

print("\n with every 'n' time taken equals n^2")
print("O(n^2)")