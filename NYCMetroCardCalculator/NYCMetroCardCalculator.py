"""Program the tells the user how much to add to get a whole number of rides on the NYC Metro"""

import math
from Clear import clear

def printTitle():
    """Prints the title to the console"""
    print("----------------------------------------------------")
    print("              NYC MetroCard Calculator              ")
    print(" Calculates the amount on money you need to add to  ")
    print(" get an whole number of rides without any left over ")
    print("      Reduced fare is for elderly and disabled      ")
    print("           Current regular fare is $2.90            ")
    print("           Current reduced fare is $1.45            ")
    print("     Current express bus regular fare is $7.00      ")
    print("     Current express bus reduced fare is $3.50      ")
    print("  You can only add amounts that are multiples of 5  ")
    print("       cents and only a max of $80 at a time        ")
    print("----------------------------------------------------")

def printAllInfo(fareCost : float) -> None:
    """Takes in the fare price and prints all the info needed"""
    # Keeps track of total rides
    rides = int(startingMoney // fareCost)
    # Keeps track of remaining money after fare taken out of the starting money floor rounded to the nearest $0.05
    remainingMoney = math.floor(round(startingMoney % fareCost, 2) * 20) / 20
    # Keeps track of remaining cents above the floor rounding e.x. 0.01
    leftOver = round((startingMoney % fareCost) - float(remainingMoney), 2)
    # Keeps track of total fare cost
    total = 0

    while True:
        # If there is remaining money under the fare cost calculate the first cost after that
        if remainingMoney > 0:
            total += fareCost - remainingMoney
            remainingMoney -= remainingMoney
            rides += 1
            if leftOver > 0:
                print(f"\nAdd ${total:.2f} to ${startingMoney:.2f} for a total of ${startingMoney + total:.2f} ({rides} rides)  (with an extra ${leftOver} resulting).")
            else:
                print(f"\nAdd ${total:.2f} to ${startingMoney:.2f} for a total of ${startingMoney + total:.2f} ({rides} rides).")
        else:
            if (total + fareCost) > 80:
                break

            total += fareCost
            rides += 1

            if leftOver > 0:
                print(f"\nAdd ${total:.2f} to ${startingMoney:.2f} for a total of ${startingMoney + total:.2f} ({rides} rides)  (with an extra ${leftOver} resulting).")
            else:
                print(f"\nAdd ${total:.2f} to ${startingMoney:.2f} for a total of ${startingMoney + total:.2f} ({rides} rides).")

clear()
printTitle()

# Loops and asks if the user wants to run the program again until the user doesn't want to anymore
while True:
    print("\nWhat fare do you choose?")
    print("(a) Regular")
    print("(b) Reduced")
    print("(c) Regular express bus")
    print("(d) Reduced express bus")

    while True:
        fare = input("\nChoice: ").lower()
        if fare not in ["a", "b", "c", "d"]:
            print("\nInvalid input. Input a, b, c, or d")
        else:
            break

    while True:
        try:
            startingMoney = float(input("\nWhat is your starting balance: $"))
            break
        except ValueError:
            print("\nInvalid input. Enter a number.")

    if fare == "a":
        printAllInfo(2.90)
    elif fare == "b":
        printAllInfo(1.45)
    elif fare == "c":
        printAllInfo(7.00)
    else:
        printAllInfo(3.50)

    if input("\nRun again? (y/n): ").lower() == "y":
        clear()
        printTitle()
    else:
        break

print("\nThanks for using!")
