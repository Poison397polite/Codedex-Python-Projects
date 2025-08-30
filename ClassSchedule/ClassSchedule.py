"""Program to create class schedules"""

import os
import json
from Clear import clear

class ClassSchedule:
    """Class for controlling a class schedule"""
    def __init__(self, name : str, **kwargs):
        self.name = name
        self.data = kwargs

    def addClass(self, className : str):
        """Adds a class to the class schedule"""
        self.data.update({str(len(self.data) + 1) : className})
        print(f"\nAdded class {className}.")

    def removeClass(self, classPeriod : str):
        """Removes a class from the class schedule"""
        try:
            print(f"Removing class {self.data[classPeriod]}")
            self.data.pop(classPeriod)
        except KeyError:
            print("\nClass period doesn't exist.")

        self.data = {str(i + 1) : value for i, value in enumerate(self.data.values())}

    def printClassSchedule(self):
        """Prints the whole class schedule to the console"""
        print()
        for key, value in self.data.items():
            print(f"Period {key}: {value}")

    def toDict(self):
        """Converts the class schedule to a dictionary for storing"""
        return {**dict(self.data.items())}

class ClassSchedules:
    """Class for making and deleting class schedules"""
    def __init__(self, fileName = "classSchedules.json"):
        self.fileName = fileName
        self.classSchedules = self.loadClassSchedules()

    def loadClassSchedules(self) -> dict:
        """Loads all saved class schedules"""
        if os.path.exists(self.fileName):
            with open(self.fileName, "r", encoding = "utf8") as f:
                data = json.load(f)
                return {name : ClassSchedule(name, **details) for name, details in data.items()}
        return {}

    def saveClassSchedules(self):
        """Saves all class schedules"""
        with open(self.fileName, "w", encoding = "utf8") as f:
            data = {name : classSchedule.toDict() for name, classSchedule in self.classSchedules.items()}
            json.dump(data, f, indent = 4)

    def createNewClassSchedule(self):
        """Create a new class schedule"""
        name = input("\nEnter student's name: ")
        if name in self.classSchedules:
            print(f"\nClass schedule already exists for {name}.")

        periodNumber = 1
        classes = {}
        while True:
            myClass = input(f"\nEnter period {periodNumber} class name (q to quit): ")
            if myClass.lower() == "q":
                break

            classes.update({str(periodNumber) : myClass})
            periodNumber += 1

        self.classSchedules[name] = ClassSchedule(name, **classes)
        self.saveClassSchedules()
        print(f"\nCreated a new class schedule for {name}.")

    def deleteClassSchedule(self):
        """Deletes a class schedule"""
        name = input("\nEnter student's name: ")
        if name in self.classSchedules:
            print(f"\nDeleting class schedule for {name}...")
            self.classSchedules.pop(name)
            self.saveClassSchedules()
        else:
            print(f"\nClass schedule for {name} doesn't exist.")

    def openClassSchedule(self):
        """Opens an existing class schedule"""
        name = input("\nEnter student's name: ")
        classSchedule = self.classSchedules.get(name)

        if classSchedule:
            print(f"\nOpening class schedule for {name}...")
            self.classScheduleMenu(classSchedule, name)
        else:
            print(f"\nClass schedule for {name} doesn't exist.")

    def classScheduleMenu(self, classSchedule : ClassSchedule, name : str):
        """Loop for displaying and editing the selected class schedule"""
        while True:
            print(f"\n===== {name}'s class schedule =====")
            print("1. Add a class")
            print("2. Remove a class")
            print("3. Display whole class schedule")
            print("4. Back to class schedule select")

            choice = input("\nEnter your choice (1 - 4): ")

            if choice == "1":
                className = input("\nEnter the class name: ")
                classSchedule.addClass(className)
                self.saveClassSchedules()
            elif choice == "2":
                classPeriod = input("\nEnter the class' period number: ")
                classSchedule.removeClass(classPeriod)
                self.saveClassSchedules()
            elif choice == "3":
                classSchedule.printClassSchedule()
            elif choice == "4":
                break
            else:
                print("\nInvalid input. Enter a number from 1 - 4.")

    def run(self):
        """Main loop for creating deleting or opening class schedules"""
        while True:
            print("\n===== Class Schedules =====")
            print("1. Create a new class schedule")
            print("2. Open existing class schedule")
            print("3. Delete class schedule")
            print("4. Exit")

            choice = input("\nEnter your choice (1 - 4): ")

            if choice == "1":
                self.createNewClassSchedule()
            elif choice == "2":
                self.openClassSchedule()
            elif choice == "3":
                self.deleteClassSchedule()
            elif choice == "4":
                print("\nGoodbye!")
                self.saveClassSchedules()
                break
            else:
                print("\nInvalid input. Enter a number from 1 - 4")

clear()
c = ClassSchedules()
c.run()

print("\nThanks for using!")
