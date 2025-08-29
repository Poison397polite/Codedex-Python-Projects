"""Program that stores info about all the zodiac signs and displays the info about the given sign"""

import json
import os

class Horoscope:
    """Class for displaying info about a specific horoscope"""
    def __init__(self, **kwargs):
        self.data = kwargs # Keep all attributes in one dictionary

    def display(self, key):
        """Function to display a specific attribute in a specific horoscope"""
        value = self.data.get(key)

        if value:
            print(f"\n{value}")
        else:
            print(f"\nNo data available for {key}.")

    def displayAll(self):
        """Function to display everything about the horoscope"""
        for key, value in self.data.items():
            print(f"\n{key.capitalize()}: {value}")

class Horoscopes:
    """Class for loading all saved horoscopes and get a chosen horoscope"""
    def __init__(self, filename = "horoscopes.json"):
        self.filename = filename
        self.horoscopes = self.loadHoroscopes()

    def loadHoroscopes(self):
        """Function to load all the saved horoscopes"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding = "utf8") as f:
                data = json.load(f)
                return{sign : Horoscope(**details) for sign, details in data.items()}
        return{}

    def horoscopeMenu(self, horoscope : Horoscope):
        """Function to handle interacting with horoscope class"""
        while True:
            print("\n===== Horoscope menu =====")
            actions = {
                "1" : "dates",
                "2" : "luckyNumbers",
                "3" : "strengths",
                "4" : "weaknesses",
                "5" : "likes",
                "6" : "dislikes",
                "7" : "description",
            }

            for key, value in actions.items():
                print(f"{key}. Display {value}")
            print("8. Display all")
            print("9. Back to horoscope selection.")

            choice = input("\nEnter your choice (1 - 9): ")

            if choice in actions:
                horoscope.display(actions[choice])
            elif choice == "8":
                horoscope.displayAll()
            elif choice == "9":
                break
            else:
                print("Enter a number between 1 and 9.")

    def run(self):
        """Function to handle picking the zodiac sign"""
        while True:
            choices = {str(i) : key for i, key in enumerate(self.horoscopes.keys(), start = 1)}

            print("\n===== Horoscopes =====")
            for i, key in choices.items():
                print(f"{i}. {key}")
            exitChoice = str(len(choices) + 1)
            print(f"{exitChoice}. Exit")

            choice = input(f"\nEnter your choice (1 - {len(choices) + 1}): ")

            if choice in choices:
                self.horoscopeMenu(self.horoscopes[choices[choice]])
            elif choice == exitChoice:
                print("\nGoodbye.")
                break
            else:
                print("\nInvalid input. Please try again.")

h = Horoscopes()
h.run()

print("\nThanks for using!")
