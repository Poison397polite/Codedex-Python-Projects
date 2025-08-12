"""Program to play Rock Paper Scissors Lizard Spock"""

import random

rpslsArt = { # Dictionary of the art for the choices
    1: r"""
______           _     
| ___ \         | |    
| |_/ /___   ___| | __ 
|    // _ \ / __| |/ / 
| |\ \ (_) | (__|   <  
\_| \_\___/ \___|_|\_\   
""",

    2: r"""
______                     
| ___ \                    
| |_/ /_ _ _ __   ___ _ __ 
|  __/ _` | '_ \ / _ \ '__|
| | | (_| | |_) |  __/ |   
\_|  \__,_| .__/ \___|_|   
          | |              
          |_|              
""",

    3: r"""
 _____      _                        
/  ___|    (_)                       
\ `--.  ___ _ ___ ___  ___  _ __ ___ 
 `--. \/ __| / __/ __|/ _ \| '__/ __|
/\__/ / (__| \__ \__ \ (_) | |  \__ \\
\____/ \___|_|___/___/\___/|_|  |___/
                                     
""",

    4: r"""
 _     _                      _ 
| |   (_)                    | |
| |    _ __________ _ _ __ __| |
| |   | |_  /_  / _` | '__/ _` |
| |___| |/ / / / (_| | | | (_| |
\_____/_/___/___\__,_|_|  \__,_|
                                
                                
""",

    5: r"""
 _____                  _    
/  ___|                | |   
\ `--. _ __   ___   ___| | __
 `--. \ '_ \ / _ \ / __| |/ /
/\__/ / |_) | (_) | (__|   < 
\____/| .__/ \___/ \___|_|\_\\
      | |                    
      |_|                    
""",
}

# Prints the title and the rules
print("----------------------------------------------------")
print("          Rock Paper Scissors Lizard Spock          ")
print("                      Rules:                        ")
print("                Scissors cuts Paper                 ")
print("                 Paper covers Rock                  ")
print("                Rock crushes Lizard                 ")
print("                Lizard poisons Spock                ")
print("               Spock smashes Scissors               ")
print("            Scissors decapitates Lizard             ")
print("                 Lizard eats Paper                  ")
print("               Paper disproves Spock                ")
print("                Spock vaporizes Rock                ")
print("               Rock crushes Scissors                ")
print("----------------------------------------------------")

# Game loop to keep playing until you no longer want to
while True:
    print("\nWhat do you choose?")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("4 - Lizard")
    print("5 - Spock")

    # Gets users choice and verifies that it is valid input
    choice = int(input("Your choice: "))
    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("Invalid Input")
        continue

    computerChoice = random.randint(1, 5) # Gets CPU choice

    # Checks every case to find out if it was a tie or find the winner
    if choice == computerChoice:
        print(f"You chose {rpslsArt[choice]}\n")
        print(f"The CPU chose {rpslsArt[computerChoice]}\n")
        print("It is a tie try again")
        continue
    elif choice == 1 and computerChoice == 3 or choice == 1 and computerChoice == 4:
        print(f"You chose {rpslsArt[choice]}\n")
        print(f"The CPU chose {rpslsArt[computerChoice]}\n")
        print("You win!")
    elif choice == 2 and computerChoice == 1 or choice == 2 and computerChoice == 5:
        print(f"You chose {rpslsArt[choice]}\n")
        print(f"The CPU chose {rpslsArt[computerChoice]}\n")
        print("You win!")
    elif choice == 3 and computerChoice == 2 or choice == 3 and computerChoice == 4:
        print(f"You chose {rpslsArt[choice]}\n")
        print(f"The CPU chose {rpslsArt[computerChoice]}\n")
        print("You win!")
    elif choice == 4 and computerChoice == 5 or choice == 4 and computerChoice == 2:
        print(f"You chose {rpslsArt[choice]}\n")
        print(f"The CPU chose {rpslsArt[computerChoice]}\n")
        print("You win!")
    elif choice == 5 and computerChoice == 3 or choice == 5 and computerChoice == 1:
        print(f"You chose {rpslsArt[choice]}\n")
        print(f"The CPU chose {rpslsArt[computerChoice]}\n")
        print("You win!")
    else:
        print(f"You chose {rpslsArt[choice]}\n")
        print(f"The CPU chose {rpslsArt[computerChoice]}\n")
        print("You lose!")

    # Asks to keep playing for game loop
    if input("Do you want to play again? y for yes anything else for no: ").lower() != "y":
        break

print("Thanks for playing!")
