"""Program used to play truth or dare with others"""

import random

# Reads the file Truths.txt and makes every line an entry in a list without trailing \n
with open("Truths.txt", "r", encoding = "utf8") as file:
    truths = file.readlines()

    truths = [line.strip() for line in truths]

# Reads the file Dares.txt and makes every line an entry in a list without trailing \n
with open("Dares.txt", "r", encoding = "utf8") as file:
    dares = file.readlines()

    dares = [line.strip() for line in dares]

# Prints the title
print("----------------------------------------------------")
print("                   Truth or Dare                    ")
print("                 Pick Truth or Dare                 ")
print("    and you will be given a random Truth or Dare    ")
print("                based on your input!                ")
print("----------------------------------------------------")

# Main loop that will keep giving you Truths or Dares based on input as long as the user wants
while True:
    # Gets input
    answer = input("\nChoose Truth or Dare: ")

    # Checks if user chose truth or dare or if they entered invalid input
    if "truth" in answer.lower():
        truth = truths[random.randint(0, len(truths))]
        print(truth)
    elif "dare" in answer.lower():
        dare = dares[random.randint(0, len(dares))]
        print(dare)
    else:
        print("Invalid Input!")

    # Asks if the user wants to continue playing if no breaks out of the loop
    if input("\nDo you want to keep playing? y for yes anything else for no: ").lower() != "y":
        break

print("\nThanks for playing!")
