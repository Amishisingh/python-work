
#if x==x[::-1]:
#    print(x,"is a palendrome no.")
#else:
#   print(x,"is not a palanderome no.")

n=int(input("enter a number:"))
o=n
r=0
while n>0:
  d=n%10
  r=10*r+d
  n=n//10
if r==o:
  print(o,"palindrome")
else:
  print(o,"not palindrome")