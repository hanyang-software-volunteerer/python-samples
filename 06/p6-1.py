
grade = int(input("Enter your grade : "))

if grade >= 95 and grade <= 100 :
	print("Your grade is A+.")
elif grade >= 90 and grade < 95 :
	print("Your grade is A0.")
elif grade >= 85 and grade < 90 :
	print("Your grade is B+.")
elif grade >= 80 and grade < 90 :
	print("Your grade is B0.")
else :
	print("Your grade is C+.")