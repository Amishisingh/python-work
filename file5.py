import os
if os.path.exists('python\ef.txt'):
    #to find the file existing in a folder which is in a folder in a file and so on till u can go to find it
    print("file exists")
else:
    print("file does not exist")
os.remove('python\ef.txt')
#to remove a file
os.rmdir('python\df.txt')
#to remove a folder