student_name =input("Enter your name: ")
print("Enter your marks obtained in the following subjects:")
math =input("Maths")
math_in_tot =input("Total marks")
ca =input("CA")
ca_in_tot =input("Total marks")
science =input("Science")
science_in_tot =input("Total marks")
ssc =input("SSC")
ssc_in_tot =input("Total marks")
total_marks_obtained = math+ca+science+ssc
total_marks = ca_in_tot+math_in_tot+science_in_tot+ssc_in_tot
print(f".........{student_name}........")
print("Total marks obtained : ",total_marks_obtained,"/",total_marks)
percent = (total_marks_obtained/total_marks)*100
print("Percentage : ",percent,"%")
if percent >= 90 and percent <= 100:
  print("GRADE : A1")
elif percent >= 80 and percent < 90:
  print("GRADE : A2")
elif percent >= 70 and percent <= 80:
  print("GRADE : B1")
elif percent >= 60 and percent <= 70:
  print("GRADE : B2")
elif percent >= 50 and percent <= 60:
  print("GRADE : C1")
elif percent >= 40 and percent <= 50:
  print("GRADE : C2")
else:
  print(student_name,"have failed , try again!")

