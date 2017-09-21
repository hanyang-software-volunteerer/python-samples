import random

name = input("Hello! What's your name? ")
print("Welcome!", name, "I'm thinking of a number between 1 and 20")
print("Guess the number! (You have an opportunity)")

num = random.randint(1, 20)

guessed_num = int(input("Enter number you guess : "))

if (guessed_num == num) :
	print("Right! Good Job!")
else :
	print("Fail... That's too bad.")