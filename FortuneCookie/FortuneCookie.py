"""Program that simulates opening a fortune cookie and getting a fortune as well as lucky numbers"""

import random

# Opens a file full of 50 different fortunes
with open("Fortunes.txt", "r", encoding = "utf8") as file:
    content = file.readlines() # Reads the whole file and converts every line to a list item

    content = [line.strip() for line in content] # Removes the trailing newline from every entry

openMore = True

while openMore:
    randomFortune = content[random.randint(0, 49)] # Gets a random fortune
    numbers = []
    for i in range(7): # Fills numbers list with the random numbers for lucky numbers
        if i == 6:
            numbers.append(random.randint(1, 26))
        else:
            numbers.append(random.randint(1, 69))

    print(randomFortune) # Prints fortune

    for num in numbers: # Prints lucky numbers with a space after
        print(num ,end=" ")

    keepOpening = input("\nWant to open another? y for yes anything else for no: ")
    if keepOpening.lower() == "y":
        openMore = True
    else:
        openMore = False
