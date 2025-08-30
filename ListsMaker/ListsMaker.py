"""Program to make any list the user wants e.g. Grocery list, Favorites list, To-do list"""

import os
import json
from Clear import clear

class List:
    """Class to make a list"""
    def __init__(self, name : str, **kwargs):
        self.name = name
        self.data = kwargs

    def displayList(self):
        """Displays the list"""
        for key, value in self.data.items():
            print(f"{key}. {value}")

    def add2List(self, value : str):
        """Adds an entry to the list"""
        self.data.update({str(len(self.data) + 1) : value})
        print(f"\nAdded a new entry: {value}")

    def removeFromList(self, key : str):
        """Removes an entry from the list and renumbers the keys"""
        try:
            print(f"\nRemoved entry: {self.data[key]}")
            self.data.pop(key)
        except KeyError:
            print("\nInvalid input. Entered value not in list.")

        self.data = {str(i + 1) : value for i, value in enumerate(self.data.values())}

    def toDict(self):
        """Function to convert the list to a dictionary for storing"""
        return {**dict(self.data.items())}

class Lists:
    """Class to interact and create or delete lists"""
    def __init__(self, filename = "lists.json"):
        self.filename = filename
        self.lists = self.loadLists()

    def loadLists(self):
        """Loads all the saved lists"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding = "utf8") as f:
                data = json.load(f)
                return{name : List(name, **details) for name, details in data.items()}
        return {}

    def saveLists(self):
        """Saves all the lists"""
        with open(self.filename, "w", encoding = "utf8") as f:
            data = {name : myList.toDict() for name, myList in self.lists.items()}
            json.dump(data, f, indent = 4)

    def createNewList(self):
        """Creates a new list"""
        name = input("\nEnter a name for the list: ")
        if name in self.lists:
            print("\nName already exists. Choose a new name.")
            return

        objectives = {}
        count = 1
        while True:
            objective = input(f"\nEnter entry {count} (q to quit and stop adding entry's): ")

            if objective.lower() == "q":
                break

            objectives.update(dict({str(count) : objective}))
            count += 1

        self.lists[name] = List(name, **objectives)
        self.saveLists()
        print(f"\nList created with the name of {name}.")

    def openExistingList(self):
        """Opens an existing list"""
        name = input("\nEnter the name of the list: ")
        myList = self.lists.get(name)

        if myList:
            print(f"\nOpening list: {name}!")
            self.listMenu(myList)
        else:
            print("\nInvalid name.")

    def listMenu(self, myList: List):
        """Function to interact with the List class"""
        while True:
            print("\n===== List Menu =====")
            print("1. Display list")
            print("2. Add an entry")
            print("3. Remove an entry")
            print("4. Return to choice selection")

            choice = input("\nEnter your choice (1 - 4): ")

            if choice == "1":
                myList.displayList()
            elif choice == "2":
                myList.add2List(input("\nEnter the entry: "))
                self.saveLists()
            elif choice == "3":
                myList.removeFromList(input("\nEnter the number of the entry to remove: "))
                self.saveLists()
            elif choice == "4":
                break
            else:
                print("\nEnter a number (1 - 4)")

    def run(self):
        """Main loop to create or load a list"""
        while True:
            print("\n===== Lists =====")
            print("1. Create a new list")
            print("2. Open an existing list")
            print("3. Exit")

            choice = input("\nEnter your choice (1 - 3): ")

            if choice == "1":
                self.createNewList()
            elif choice == "2":
                self.openExistingList()
            elif choice == "3":
                print("\nGoodbye!")
                self.saveLists()
                break
            else:
                print("\nEnter a number (1 - 3)")

clear()
t = Lists()
t.run()

print("\nThanks for using!")
