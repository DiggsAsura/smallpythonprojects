# Ok this is just made out of no motivation and just trying to do something. Haha, i had a syntax error
# on if rng_1 == number3 for the longest time, figured after a long time i messed up the line above. I knew,
# but still a kind note to self. 
# 

import random

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Guess which number between those two I will pick: "))

rng_1 = random.randint(number1, number2)


if rng_1 == number3:
  print("\n\tWoow, you got it! Correct! " + str(rng_1) + " indeed was the number!")
else:
  print("\n\tBummer... you guess " + str(number3) + ", while the answer really was " + str(rng_1) + ":-(")

print("\n")
print("\t\t Thank you for playing this useless game")
print("\n\n")
