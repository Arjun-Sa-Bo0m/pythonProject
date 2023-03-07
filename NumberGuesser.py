
import random

num = random.randint(2,2)
guess = False
while not guess:
    userNum = int(input("Guess the number between 1 and 1:"))
    if userNum == num:
        print("You guessed it right!")
        break
    elif userNum < num:
        print("Too low!")
    else:
        print("Too high!")