import random
import math
from playsound import playsound



#set up number range
smaller = int("1")
larger = int("100")


#generate random number
x = random.randint(smaller, larger)
print("A random number has been generated, please begin guessing. You have 10 tries.")

#store number of guesses player has done
count = 0


#while loop, set max guesses and begin counting, store players guess and math accordingly.
while count < 10:
    count += 1

    guess = int(input("Guess a number from 1-100:-"))

    if x == guess:
        print("Congrats you have guessed the correct number", + x)
        playsound('/home/josh/Desktop/VSCode-Projects/GeneralPy/rngguesser/sounds/ding.mp3')
        break

    elif x > guess:
        print("You guessed too small!")
        playsound('/home/josh/Desktop/VSCode-Projects/GeneralPy/rngguesser/sounds/wrong.mp3')
    elif x < guess:
        print("You Guessed too high!")
        playsound('/home/josh/Desktop/VSCode-Projects/GeneralPy/rngguesser/sounds/wrong.mp3')

    if count == 10:
        print ("You have run out of guesses!")
        playsound('/home/josh/Desktop/VSCode-Projects/GeneralPy/sounds/lost.mp3')
        break


