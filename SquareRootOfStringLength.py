# Square Root of String Length
# A quite useless program to calculate the square root of string length (name for the example)
# As part of personal training outside of Codecademy course

def sqr(first, middle, last):
	return (len(first + middle + last) ** 0.5)
	
first = input("Your first name: ")
middle = input("Your middle name: ")
last = input("Your last name: ")

print("Hi", first, middle, last + "!")
square = sqr(first, middle, last)
full_length = first + middle + last

print("The square root of your full name" + " (" + str(len(full_length)) + " digits) is " + str(square))
