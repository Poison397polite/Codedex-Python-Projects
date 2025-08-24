"""Program that counts the words in a given text"""

import Clear

def printTitle():
    """Prints the title"""
    print("----------------------------------------------------")
    print("      Enter text you need the word count for.       ")
    print("            Prints the word count after!            ")
    print("----------------------------------------------------")

while True:
    words = input("Enter the text you want the word count for: ").split()

    if len(words) == 1:
        print("There is 1 word in the text!")
    else:
        print(f"There are {len(words)} words in the text!")

    if input("Another text? (y/n): ").lower() == "y":
        Clear.clear() # Clears the console when called
        printTitle()
        continue

    break

print("Thanks for using!")
