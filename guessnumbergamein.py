# progect 2 : guess the number game in computer.
# 1 to 100 numbers.

import random
def guess_the_number():
    """project 2: guess_the_number game by computer."""
    number=random.randint(1,100)
    guesses_left = 7
    #welcome message
    print("welcome to the number guessing game")
    print("I am thinking a number between 1 to 100")

    #loop generated
    while guesses_left > 0:
        print(f"\nyou have {guesses_left} guesses left. ")
        try:
            guess = int(input("Take a guess of another number."))
        except ValueError:
            print("Invalid input:please enter a number. ")
            continue

        #guess the secret number.
        if guess < number:
            print("Too low number . Tell another!")
        elif guess > number:
            print("Too high number . Tell another!")
        else:
            print(f"congratulations! you got the correct number in {7 - guesses_left + 1} tries. ")
            return # Exit the game

        guesses_left -= 1
        #jab sub guesses finish ho jayengy
    print(f"\nyou ran out of guess. the number was {number}. ")

guess_the_number()         
