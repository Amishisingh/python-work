
for i in range(10, 100):
    r=0
    for j in range(2, i):
        if i%j != 0:
           r=r+0
        else:
            r=r+1
    if r==0:
        print(i)