# Square Root of String Length
# A quite useless program to calculate the square root of string length (name for the example)
# As part of personal training outside of Codecademy course
# This program will use:
# 1. Function to accpet 3 parameters
# 2. The function will, for no reason, return the square root of the total length lol (to remember how to 
#    calculate squre root (** 0.5). I am aware of the built-in function sqrt() 
# 3. Use user-inputs for the parameters
# 4. Print the names, full length, and the result of the function (square root)

def sqr(first, middle, last):
	return (len(first + middle + last) ** 0.5)
	
first = input("Your first name: ")
middle = input("Your middle name: ")
last = input("Your last name: ")

print("Hi", first, middle, last + "!")
square = sqr(first, middle, last)
full_length = first + middle + last

print("The square root of your full name" + " (" + str(len(full_length)) + " digits) is " + str(square))
