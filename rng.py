# testing and trying to learn random.choice()

import random

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_rng(num1, num2):
	return num1 + num2

num1 = random.choice(lst)
num2 = random.choice(lst)

print(num1, "+", num2, "=", my_rng(num1, num2))

print(num1) # num1 - is this the same value, or will num1 every time its called be running random.choice() again?
print(num1) # num1 - yea, so it will just be the same. For good and for bad. 
print(num2)
print(num2)
