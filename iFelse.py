#Date Time Module
datetime_object= datetime.datetime.now()


#If Else statment
number = int(input("ENTER NO."))
if number%2==0:
   print("This is a EVEN number")
else:
   print("This is a OOD number")


   skyIsBlack = True

if(skyIsBlack):
    print("it is night")
else:
  print("it is not night")

   
 #If Else Elif Statment  
numbe = int(input("ENTER no."))
if numbe>0:
   print("This is a natural number")
elif numbe>=0:
   print("This is a whole number")
else :
   print("This is a -ve integer")

#Nested IF Statment
num = float(input("Enter Your Age"))
if num>0  and num<140:
  if num>=18:
    print("Adult")
  elif num>0 and num<13:
     print("kid")
  elif num>12 and num<=19:
   print("teenager")
  else:
    print("Underage")
else:
   print("Wrong input")





