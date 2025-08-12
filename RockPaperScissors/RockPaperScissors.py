"""Program to play rock paper scissors againts a very basic AI(random numbers)"""

import random

rpsHands = { # Dictionary of the art for Rock Paper Scissors
    1: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    2: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    3: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Prints title
print("---------------------------------------------------")
print("                Rock Paper Scissors                ")
print("---------------------------------------------------")

while True: # Game loop to keep playing until you no longer want to
    print("\nWhat do you choose?")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    choice = int(input("Your choice: ")) # Gets users choice

    if choice != 1 and choice != 2 and choice != 3: # Makes sure user entered valid input
        print("\nInvalid input")
        continue

    computerChoice = random.randint(1, 3) # Gets CPU choice

    # Checks every possibility to find Tie or the winner
    if choice == computerChoice:
        print(f"You chose:\n{rpsHands[choice]}\n")
        print(f"The CPU chose:\n{rpsHands[computerChoice]}\n")
        print("It is a tie try again!")
        continue
    elif choice == 1 and computerChoice == 2:
        print(f"You chose:\n{rpsHands[choice]}\n")
        print(f"The CPU chose:\n{rpsHands[computerChoice]}\n")
        print("You lose!")
    elif choice == 1 and computerChoice == 3:
        print(f"You chose:\n{rpsHands[choice]}\n")
        print(f"The CPU chose:\n{rpsHands[computerChoice]}\n")
        print("You win!")
    elif choice == 2 and computerChoice == 1:
        print(f"You chose:\n{rpsHands[choice]}\n")
        print(f"The CPU chose:\n{rpsHands[computerChoice]}\n")
        print("You win!")
    elif choice == 2 and computerChoice == 3:
        print(f"You chose:\n{rpsHands[choice]}\n")
        print(f"The CPU chose:\n{rpsHands[computerChoice]}\n")
        print("You lose!")
    elif choice == 3 and computerChoice == 1:
        print(f"You chose:\n{rpsHands[choice]}\n")
        print(f"The CPU chose:\n{rpsHands[computerChoice]}\n")
        print("You lose!")
    elif choice == 3 and computerChoice == 2:
        print(f"You chose:\n{rpsHands[choice]}\n")
        print(f"The CPU chose:\n{rpsHands[computerChoice]}\n")
        print("You win!")
    else:
        print("Unknown Error")

    # Asks to keep playing for game loop
    if input("Do you want to play again? y for yes anything else for no: ").lower() != "y":
        break

print("Thanks for playing!")
