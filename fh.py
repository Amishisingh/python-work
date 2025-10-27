file1 = open('python\df.txt','r')#to open file df
r= file1.read()#to read the file df
print(r)#to print the content of file df
file1.close()#to close the file

file2=open('python\df.txt','a')#to open file df to append
file2.write("\nfile is changed")#to write content from a new line
file2.close()#to close the file

ef= open('python\ek.txt','w')#to write in it deleting previous data
ef.write('this is to remove and add content')#to add in file
ef.close()#to close the file



