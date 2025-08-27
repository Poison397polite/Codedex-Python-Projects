"""Program to decipher a caesar cipher"""

import string
import enchant
from Clear import clear

def printTitleAndRules():
    """Prints the title and the rules to the console"""
    print("----------------------------------------------------")
    print("               Caesar Cipher decipher               ")
    print(" A caesar cipher is a way to encrypt text by moving ")
    print("every letter by a certain amount forward or backward")
    print("This program has 2 modes the first one asks for the ")
    print("   number the letters are shifted and prints the    ")
    print("decrypted text, the second mode tries to decrypt the")
    print("               text with brute force                ")
    print("----------------------------------------------------")

# Lower case alphabet to find and shift the letters
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]

# Upper case alphabet to find and shift the letters
alphabetCaps = ["A", "B", "C", "D", "E", "F", "G", "H",
                "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X",
                "Y", "Z"]

# list for the punctuation and the special characters to skip if in encrypted text
punctuationAndSpecialChars = ["," , ".", "?", "!", "/", ";", ":", "\\",
                              "<", ">", "'", '"', "[", "]", "{", "}",
                              "|", "-", "_", "=", "+", "(", ")", "*",
                              "&", "^", "%", "$", "#", "@"]

def decryptWithShift(encryptedText : str, shift : int) -> str:
    """Decrypts the caesar cipher with a known shift amount"""
    # Splits the text into a list of all the words
    words = encryptedText.split()
    # Stores the full decrypted text
    decryptedText = []

    # Loops through each word and letter to decrypt the text one letter at a time
    for word in words:
        # Stores the current decrypted word
        decryptedWord = []

        for letter in word:
            # If letter is punctuation or a special character add it to the decryptedWord list
            # and skip to next letter
            if letter in punctuationAndSpecialChars:
                decryptedWord.append(letter)
                continue

            # If the letter is capitalized use the capitalized alphabet list
            if letter.isupper():
                # Get the index of the encrypted letter
                index = alphabetCaps.index(letter)
                # Shift the index to get the index of the decrypted letter
                shiftedIndex = index - shift

                # While the index is out of bounds add the length of the alphabetCaps list
                # to effectively loop to the end of the list
                while shiftedIndex < 0:
                    shiftedIndex += len(alphabetCaps)

                # Adds the decrypted letter to the decryptedWord list
                decryptedWord.append(alphabetCaps[shiftedIndex])

            # Else use the lower case alphabet list
            else:
                # Get the index of the encrypted letter
                index = alphabet.index(letter)
                # Shift the index to get the index of the decrypted letter
                shiftedIndex = index - shift

                # While the index is out of bounds add the length of the alphabet list
                # to effectively loop to the end of the list
                while shiftedIndex < 0:
                    shiftedIndex += len(alphabet)

                # Adds the decrypted letter to the decryptedWord list
                decryptedWord.append(alphabet[shiftedIndex])

        # Adds the decrypted word to the decryptedText list
        decryptedText.append("".join(decryptedWord))

    # Returns the decryptedText list as a single string with a space between each word
    return " ".join(decryptedText)

def decryptWithoutShift(encryptedText : str) -> str:
    """Decrypts the caesar cipher without a known shift amount with brute force"""
    # Creates a dict object that is the us english dictionary for checking if a word is real
    d = enchant.Dict("en_US")
    # Splits the text into a list of all the words
    words = encryptedText.split()
    # Stores the full decrypted text
    decryptedText = []
    # Variable to find the shift of the text
    shift = 1

    while True:
        # Variable to keep track if the word is real if not increment shift and try to decrypt again
        realWord = True

        # Loops through every word and letter before determining if it is a real word to decrypt the text
        for word in words:
            # Stores the current decrypted word
            decryptedWord = []

            for letter in word:
                # If letter is punctuation or a special character add it to the decryptedWord list
                # and skip to next letter
                if letter in punctuationAndSpecialChars:
                    decryptedWord.append(letter)
                    continue

                # If the letter is capitalized use the capitalized alphabet list
                if letter.isupper():
                    # Get the index of the encrypted letter
                    index = alphabetCaps.index(letter)
                    # Shift the index to get the index of the decrypted letter
                    shiftedIndex = index - shift

                    # While the index is out of bounds add the length of the alphabetCaps list
                    # to effectively loop to the end of the list
                    while shiftedIndex < 0:
                        shiftedIndex += len(alphabetCaps)

                    # Adds the decrypted letter to the decryptedWord list
                    decryptedWord.append(alphabet[shiftedIndex])

                # Else use the lower case alphabet list
                else:
                    # Get the index of the encrypted letter
                    index = alphabet.index(letter)
                    # Shift the index to get the index of the decrypted letter
                    shiftedIndex = index - shift

                    # While the index is out of bounds add the length of the alphabet list
                    # to effectively loop to the end of the list
                    while shiftedIndex < 0:
                        shiftedIndex += len(alphabet)

                    # Adds the decrypted letter to the decryptedWord list
                    decryptedWord.append(alphabet[shiftedIndex])

            # If word is real append it to the end of the decryptedText list
            if d.check(("".join(decryptedWord)).strip(string.punctuation)):
                decryptedText.append("".join(decryptedWord))
            # Else clear the list and increment the shift and try again with a new shift
            else:
                decryptedText.clear()
                shift += 1
                realWord = False
                break

        # If the word is real add it to the decryptedText list and go to next word else retry
        # with a different shift
        if realWord:
            return " ".join(decryptedText)

        continue

clear()
printTitleAndRules()

# Main loop to allow using to keep decrypting text until they no longer want to
while True:
    # Loop to ensure user picks one of the 2 options available
    while True:
        mode = input("\nPick the first mode (a) or the second mode (b): ").lower()
        if mode not in ["a", "b"]:
            print("\nInvalid input. Enter a or b")
        else:
            break

    # If user chose choice 1 (decrypt with known shift number)
    if mode == "a":
        # Get encrypted text
        text = input("\nEnter the encrypted text: ")
        # Loop to ensure the user enters a number
        while True:
            try:
                shiftNum = int(input("\nEnter the shift number: "))
                break
            except ValueError:
                print("\nInvalid input. Enter a number.")

        # Prints decrypted text
        print("\n" + decryptWithShift(text, shiftNum))
    # Else user chose choice 2 (decrypt without known shift number)
    else:
        text = input("\nEnter the encrypted text: ")
        print("\n" + decryptWithoutShift(text))

    # Asks if user wants to decrypt another text
    if input("\nRun again? (y/n): ").lower() == "y":
        clear()
        printTitleAndRules()
    else:
        break

print("\nThanks for using!")
