import random

#add word you wnats
list = ["apple", "banana", "kiwi", "pineapple", "orange", "watermelon", "melon"]

print("Start game. Good Luck.")

for i in range(5) :
	word = random.choice(list)
	print(word)
	while True :
		input_word = input("Enter word : ")
		if (word == input_word) :
			print("pass!")
			break
		else :
			print("again!")

print("End! Have a nice day.")

