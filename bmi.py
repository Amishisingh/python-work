Height = float(input("Enter height in cm"))
Weight = float(input("Enter weight in kg"))
BMI = Weight/(Height/100)**2
print("Your BMI is:",BMI)
if BMI<=18.4:
   print("Under Weight")
elif BMI<=24.9:
   print("You are Healthy")
elif BMI<=29.9:
   print("Over Weight")
elif BMI<=34.9:
   print("Severly Over Weight")
elif BMI<=39.9:
   print("Obese")
else:
   print("Severly Obese")   