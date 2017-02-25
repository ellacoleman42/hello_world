import random
import time

number = random.randint(1,10)
guess = 0
count = 0
while number != guess:
    while guess != number:
        guess = int(input("I'm thinking of a number between one and ten. Can you guess what it is?"))
        if guess != number:
            print("That is wrong. Please guess again.")
            count += 1
        if count >= 10:
            print("You have guessed 10 times. Please wait 5 seconds before guessing again.")
            time.sleep(5)
            count = 0
print("That is correct. Well done.")