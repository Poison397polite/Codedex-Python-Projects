"""Simple hangman program"""

import random
from Clear import clear

# Stores all the game stages of the hangman game. Don't change position in important
g_hangmanGameStages = [
r"""
   +---+
   |   |
       |
       |
       |
       |
 =========
 """,
 r"""
   +---+
   |   |
   O   |
       |
       |
       |
 =========
 """,
 r"""
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========
 """,
 r"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========
 """,
 r"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========
 """,
 r"""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========
 """,
 r"""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========
 """
]

# Stores the alphabet for checking that the user only enters letters in the english alphabet
g_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

class GameLoop:
    """Class for handling the main game loop"""
    def __init__(self):
        # Fills self.mediumWords with all the words in 5-8LetterWords.txt
        with open("5-8LetterWords.txt", "r", encoding = "utf8") as f:
            self.mediumWords = [line.strip() for line in f]

        # Fills self.longWords with all the words in 9+LetterWords.txt
        with open("9+LetterWords.txt", "r", encoding = "utf8") as f:
            self.longWords = [line.strip() for line in f]

    def showRules(self):
        """Prints the rules when called"""
        clear()
        print("===== Rules =====")
        print("1. A certain amount of underscores will be displayed for how many letters are in the word")
        print("2. You will enter a letter to guess")
        print("3. If the letter is in the word, the letter will be put into the word replacing the underscores")
        print("4. If the letter is not in the word an additional body part will be added to the person on the gallows")
        print("5. Once the person is complete (6 incorrect letters guesses) you lose")
        print("6. If you fill in the word you win")
        input("Press enter to go back to the main menu.")

    def displayScreen(self, word : str, solvedLetters : list[str], incorrectLetters : list[str], gameStage : int):
        """Displays the game screen"""
        print(g_hangmanGameStages[gameStage])

        if incorrectLetters:
            print(f"Incorrect letters: {", ".join(incorrectLetters)}")

        for letter in word:
            if letter in solvedLetters:
                print(letter, end = "")
            else:
                print("_", end = "")

        print()

    def enterLetter(self, solvedLetters : list[str], incorrectLetters : list[str]) -> str:
        """Asks the user to input a guess and validate it"""
        while True:
            guess = input("\nEnter a letter to guess: ").lower()

            if len(guess) > 1:
                print("\nPlease enter only one letter.")
                continue

            if guess not in g_alphabet:
                print("\nPlease enter a letter in the alphabet.")
                continue

            if guess in solvedLetters or guess in incorrectLetters:
                print("\nYou already guessed that letter.")
                continue

            break

        return guess

    def playGame(self, wordLength : str) -> bool:
        """Play a round of hangman with the given word length"""
        clear()
        # Gets a random word from the chosen word length list
        if wordLength == "medium":
            word = random.choice(self.mediumWords)
        else:
            word = random.choice(self.longWords)

        # Holds the letters that are solved
        solvedLetters = set()
        # Holds the letters that have been guessed but are incorrect
        incorrectLetters = set()
        # Holds the game stage to print the correct hangman stage
        # Also used for life checking
        gameStage = 0
        # Holds if the user won or not
        won = False

        # Main loop display screen get a guess until the user wins or guesses 6 wrong letters
        while True:
            clear()
            self.displayScreen(word, solvedLetters, incorrectLetters, gameStage)

            guessedLetter = self.enterLetter(solvedLetters, incorrectLetters)

            if guessedLetter in word:
                solvedLetters.add(guessedLetter)
            else:
                incorrectLetters.add(guessedLetter)
                gameStage += 1

            if gameStage == len(g_hangmanGameStages) - 1:
                clear()
                self.displayScreen(word, solvedLetters, incorrectLetters, gameStage)
                break

            if set(word).issubset(solvedLetters):
                clear()
                self.displayScreen(word, solvedLetters, incorrectLetters, gameStage)
                won = True
                break

        if won:
            print("\nGood job! You won!!!")
        else:
            print(f"\nYou lost. The word was {word}. Better luck next time.")

        playAgain = input("\nDo you want to play again? (y/n): ").lower()

        if playAgain == "y":
            return True

        return False

    def mainMenu(self):
        """Prints the main menu of the game"""
        while True:
            clear()
            print("===== Hangman =====")
            print("1. Play with a 5 - 8 letter word")
            print("2. Play with a 9+ letter word")
            print("3. See the rules")
            print("4. Quit")

            choice = input("\nEnter your choice: ")

            match choice:
                case "1":
                    playAgain = self.playGame("medium")
                case "2":
                    playAgain = self.playGame("long")
                case "3":
                    self.showRules()
                case "4":
                    break
                case _:
                    print("\nInvalid input. Please enter a number between 1 and 4.")

            if not playAgain:
                break

game = GameLoop()
game.mainMenu()

clear()
print("Thanks for playing!")
