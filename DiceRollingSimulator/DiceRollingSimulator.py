"""Program where you roll a chosen amount of dice as many times as you want and it will tell you the total of all the dice rolled!"""

import random

diceFaces = { # Dictionary of all 6 of the dice faces
    1: [
        "╔═════════╗",
        "║         ║",
        "║    ●    ║",
        "║         ║",
        "╚═════════╝"
    ],
    2: [
        "╔═════════╗",
        "║ ●       ║",
        "║         ║",
        "║       ● ║",
        "╚═════════╝"
    ],
    3: [
        "╔═════════╗",
        "║ ●       ║",
        "║    ●    ║",
        "║       ● ║",
        "╚═════════╝"
    ],
    4: [
        "╔═════════╗",
        "║ ●     ● ║",
        "║         ║",
        "║ ●     ● ║",
        "╚═════════╝"
    ],
    5: [
        "╔═════════╗",
        "║ ●     ● ║",
        "║    ●    ║",
        "║ ●     ● ║",
        "╚═════════╝"
    ],
    6: [
        "╔═════════╗",
        "║ ●     ● ║",
        "║ ●     ● ║",
        "║ ●     ● ║",
        "╚═════════╝"
    ]
}

def printDice(diceValues):
    """Prints multiple dice side by side."""
    for row in range(5): # Each dice face has 5 lines
        print("  ".join(diceFaces[val][row] for val in diceValues))

totalRolled = 0

while True: # Loop to keep rolling as many dice as you want until you don't want to anymore
    numberOfDice = int(input("How many dice do you want to roll? "))

    randomDice = []
    for dice in range(numberOfDice): # Gets the number for every die
        randomDice.append(random.randint(1, 6))

    printDice(randomDice)
    totalRolled = sum(randomDice) # Gets the total for all dice rolled
    print(f"You rolled a total of: {totalRolled}")

    if input("Do you want to roll again? y for yes anything else for no: ").lower() == "y":
        continue
    else:
        break
