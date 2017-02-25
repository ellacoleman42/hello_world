import random
import time

number = random.randint(1,100)
guess = 0
count = 0
while number != guess:
    while guess != number:
        guess = int(input("I'm thinking of a number between one and one hundred. Can you guess what it is?"))
        if guess > number:
            print("That is too big. Please guess again.")
            count += 1
        if guess < number:
            print("That is too small. Please try again.")
        if count >= 10:
            print("You have guessed 10 times. Please wait 5 seconds before guessing again.")
            time.sleep(5)
            count = 0
print("That is correct. Well done.")