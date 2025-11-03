file1=open('python\df.txt','r')
with open('python\df.txt','w+') as file1:
    file1.write("first line")
r= file1.read()
print(r,"a")
with open('python\df.txt','w+') as file1:
    file1.write("second input")
r= file1.read()
print(r,"o")

#r+___read and write
#w+___write and read