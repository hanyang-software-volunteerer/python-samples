import random

def get_number() :
	return random.randint(1, 45)

print("numbers : ")
for i in range(6) :
	print(get_number())