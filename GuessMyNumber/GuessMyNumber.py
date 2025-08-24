"""Little game where the user tries and guesses the number chosen by the CPU"""

import random
import os

def clear():
    """Clears all text from the console"""
    os.system("cls")

def printTitleAndRules():
    """Prints the title and rules for the game"""
    print("----------------------------------------------------")
    print("                  Guess my number                   ")
    print("               You have 6 tries total               ")
    print("          Enter a number between 1 and 100          ")
    print("     You will be told if your guess is too high     ")
    print("            or if your guess is too low             ")
    print("----------------------------------------------------")

tries = 6
num = random.randint(1, 100)
printTitleAndRules()

while True:
    while True:
        try:
            if tries < 1:
                print("\nYou have no more tries.")
                print(f"\nThe number was {num}")
                break

            guess = int(input("\nEnter your guess (between 1 and 100): "))
            if guess < num:
                print("\nToo low!")
                tries -= 1
            elif guess > num:
                print("\nToo high!")
                tries -= 1
            else:
                print("\nYou got it!")
                break
        except ValueError:
            print("\nInvalid input. Enter a number.")

    if input("\nGuess again? (y/n): ").lower() != "y":
        break

    num = random.randint(1, 100)
    tries = 6
    clear()
    printTitleAndRules()

print("\nThanks for playing!")
