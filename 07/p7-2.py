import random

name = input("Hello! What's your name? ")
print("Welcome!", name, "I'm thinking of a number between 1 and 20")
print("Guess the number! (You have an opportunity)")

answer = random.randint(1, 20)
success = False

for i in range(6) :
	guessed_num = int(input("Enter number you guess : "))

	if (guessed_num == answer) :
		print("Right! Good Job!")
		success = True
		break
	else :
		print("Try again.")

if (success) :
	print("Congraturation!")
else :
	print("Fail... That's too bad")