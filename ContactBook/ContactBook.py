"""Program to make a contact book"""

import json
import os
from Clear import clear

class Contact:
    """Class to store and edit a contact"""
    def __init__(self, name : str, phoneNumber : str):
        self.name = name
        self.phoneNumber = phoneNumber

    def changeName(self, newName : str):
        """Changes the name for the contact"""
        self.name = newName

    def changePhoneNumber(self, newPhoneNumber : str):
        """Changes the phone number for the contact"""
        self.phoneNumber = newPhoneNumber

    def displayContact(self):
        """Displays the contact to the console"""
        print(f"{self.name}: {self.phoneNumber}")

    def toDict(self) -> dict:
        """Converts the contact to a dictionary for storing"""
        return {"name" : self.name, "phoneNumber" : self.phoneNumber}

class ContactBook:
    """Class to create Contact's and main interface"""
    def __init__(self, fileName = "contactBook.json"):
        self.fileName = fileName
        self.contacts = self.loadContactBook()

    def loadContactBook(self) -> dict:
        """Loads all saved contacts into the contact book"""
        if os.path.exists(self.fileName):
            with open(self.fileName, "r", encoding = "utf8") as f:
                data = json.load(f)
                return {name : Contact(contact["name"], contact["phoneNumber"]) for name, contact in data.items()}
        return {}

    def saveContactBook(self):
        """Saves all contacts in the contact book"""
        with open(self.fileName, "w", encoding = "utf8") as f:
            data = {name : contact.toDict() for name, contact in self.contacts.items()}
            json.dump(data, f, indent = 4)

    def createContact(self):
        """Creates a new contact and saves it to the contact book"""
        while True:
            name = input("\nEnter the name for the contact: ")
            if name in self.contacts:
                print("\nContact name already exists. Try again.")
            else:
                break

        while True:
            phoneNumber = input("\nEnter the phone number for the contact (format: 1112223333): ")
            if not phoneNumber.isdigit():
                print("\nEntered something other then a number. Try again.")
            else:
                break

        phoneNumber = f"{phoneNumber[ : 3]}-{phoneNumber[3 : 6]}-{phoneNumber[6 : ]}"

        self.contacts[name] = Contact(name, phoneNumber)
        self.saveContactBook()
        print(f"\nCreated contact for {name}.")

    def openContact(self):
        """Opens an existing contact"""
        name = input("\nEnter the name of the contact: ")
        contact = self.contacts.get(name)

        if contact:
            print(f"\nOpening contact for {name}...")
            self.contactMenu(contact)
            return

        print("\nContact doesn't exist.")

    def deleteContact(self):
        """Deletes a contact from the contact book"""
        name = input("\nEnter the name of the contact to delete: ")
        contact = self.contacts.get(name)

        if contact:
            print(f"\nDeleting the contact for {name}...")
            self.contacts.pop(name)
        else:
            print("\nContact doesn't exist.")

    def displayContactBook(self):
        """Displays the whole contact book"""
        print()
        for contact in self.contacts.values():
            contact.displayContact()

    def contactMenu(self, contact: Contact):
        """Menu for editing a contact"""
        while True:
            print(f"\n===== Contact menu: {contact.name}")
            print("1. Change name")
            print("2. Change phone number")
            print("3. Display contact")
            print("4. Return to contact book menu")

            choice = input("\nEnter your choice (1 - 4): ")

            if choice == "1":
                newName =  input("\nEnter the new name: ")
                contact.changeName(newName)
                self.saveContactBook()
            elif choice == "2":
                newPhoneNumber = input("\nEnter the new phone number (1112223333): ")
                newPhoneNumber = f"{newPhoneNumber[ : 3]}-{newPhoneNumber[3 : 6]}-{newPhoneNumber[6 : ]}"
                contact.changePhoneNumber(newPhoneNumber)
                self.saveContactBook()
            elif choice == "3":
                print()
                contact.displayContact()
            elif choice == "4":
                break
            else:
                print("\nInvalid input. Enter a number (1 - 4).")

    def run(self):
        """Main loop for the program"""
        while True:
            print("\n===== Contact Book Menu =====")
            print("1. Create a new contact")
            print("2. Open an existing contact")
            print("3. Delete a contact")
            print("4. Display the whole contact book")
            print("5. Exit")

            choice = input("\nEnter your choice (1 - 4): ")

            if choice == "1":
                self.createContact()
            elif choice == "2":
                self.openContact()
            elif choice == "3":
                self.deleteContact()
            elif choice == "4":
                self.displayContactBook()
            elif choice == "5":
                print("\nGoodbye!")
                self.saveContactBook()
                break
            else:
                print("\nInvalid input. Enter a number (1 - 4).")

clear()
contactBook = ContactBook()
contactBook.run()

print("\nThanks for using!")
