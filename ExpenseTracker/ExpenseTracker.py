"""Program to track user expenses"""

import json
import os
from Clear import clear

class Expense:
    """Class for making and editing the name and price of an expense"""
    def __init__(self, name : str, price : float, frequency = "monthly"):
        self.name = name
        self.price = price
        self.frequency = frequency

    def changeName(self, name : str):
        """Changes the name of the expense"""
        self.name = name

    def changePrice(self, price : float):
        """Changes the price of the expense"""
        self.price = price

    def changeFrequency(self, frequency : str):
        """Changes the frequency the expense is payed"""
        self.frequency = frequency

    def getYearlyPrice(self) -> float:
        """Returns the price converted to a yearly price"""
        if self.frequency == "bi-weekly":
            return round(self.price * 26, 2)

        if self.frequency == "monthly":
            return round(self.price * 12, 2)

        return self.price

    def getMonthlyPrice(self) -> float:
        """Returns the price converted to a monthly price"""
        if self.frequency == "bi-weekly":
            return round(self.price * 2, 2)

        if self.frequency == "monthly":
            return self.price

        return round(self.price / 12, 2)

    def displayExpense(self):
        """Prints the expense to the console"""
        print(f"\n{self.name} is ${self.price}, payed {self.frequency} for a total of ${self.getMonthlyPrice()} monthly.")

    def toDict(self) -> dict:
        """Converts the class to a dictionary for storing"""
        return {"name" : self.name, "price" : self.price, "frequency" : self.frequency}

    def __str__(self) -> str:
        return f"{self.name} cost ${self.price} and is paid {self.frequency}"

class Expenses():
    """Class to store and interact with all expenses"""
    def __init__(self, fileName = "expenses.json"):
        self.fileName = fileName
        self.expenses = self.loadExpenses()

    def loadExpenses(self) -> dict:
        """Loads all saved expenses"""
        if os.path.exists(self.fileName):
            with open(self.fileName, "r", encoding = "utf8") as f:
                data = json.load(f)
                return {
                    name : Expense(expense["name"], expense["price"], expense["frequency"])
                    for name, expense in data.items()
                }
        return {}

    def saveExpenses(self):
        """Saves all expenses"""
        with open(self.fileName, "w", encoding = "utf8") as f:
            data = {name : expense.toDict() for name, expense in self.expenses.items()}
            json.dump(data, f, indent = 4)

    def createExpense(self):
        """Creates a new expense"""
        name = input("\nEnter the name of the expense: ")
        if name in self.expenses:
            print("\nExpense already exists.")
            return

        while True:
            print("\nEnter the frequency that the expense is paid.")
            print("1. bi-weekly")
            print("2. monthly")
            print("3. yearly")

            frequency = input("\nEnter your choice: ")

            if frequency == "1":
                frequency = "bi-weekly"
                break

            if frequency == "2":
                frequency = "monthly"
                break

            if frequency == "3":
                frequency = "yearly"
                break

            print("\nEnter a number between 1 - 3")

        while True:
            try:
                price = float(input("\nEnter the price of the expense: "))
                break
            except ValueError:
                print("\nInvalid input. Enter a number.")

        self.expenses[name] = Expense(name, price, frequency)
        self.saveExpenses()
        print(f"\nExpense created: {name} cost ${price} and is paid {frequency}.")

    def openExpense(self):
        """Opens an existing expense"""
        name = input("\nEnter the name of the expense: ")
        expense = self.expenses.get(name)

        if expense:
            print(f"\nOpening expense {name}...")
            self.expenseMenu(expense)
        else:
            print("\nExpense doesn't exist.")

    def deleteExpense(self):
        """Deletes an expense"""
        name = input("\nEnter the name of the expense: ")
        expense = self.expenses.get(name)

        if expense:
            print(f"\nDeleting expense {name}...")
            self.expenses.pop(name)
            self.saveExpenses()
        else:
            print("Expense doesn't exist.")

    def displayAllExpenses(self):
        """Displays all the expenses"""
        print()
        yearlyTotal = 0
        monthlyTotal = 0

        for expense in self.expenses.values():
            print(expense)
            yearlyTotal += expense.getYearlyPrice()
            monthlyTotal += expense.getMonthlyPrice()

        print(f"\nThe total of all your expenses is ${yearlyTotal:,} yearly, which is ${monthlyTotal:,} per month.")

    def expenseMenu(self, expense : Expense):
        """Menu for editing an expense"""
        print(f"\n===== Menu for expense: {expense.name}")
        print("1. Change name")
        print("2. Change price")
        print("3. Change frequency")
        print("4. Display expense")
        print("5. Back to expense tracker menu")

        choice = input("\nEnter your choice (1 - 5): ")

        if choice == "1":
            name = input("Enter new name: ")
            expense.changeName(name)
            self.saveExpenses()
        elif choice == "2":
            while True:
                try:
                    price = float(input("Enter the new price: "))
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")

            expense.changePrice(price)
            self.saveExpenses()
        elif choice == "3":
            while True:
                print("\nEnter the new frequency that the expense is paid.")
                print("1. bi-weekly")
                print("2. monthly")
                print("3. yearly")

                frequency = input("\nEnter your choice: ")

                if frequency == "1":
                    frequency = "bi-weekly"
                    break

                if frequency == "2":
                    frequency = "monthly"
                    break

                if frequency == "3":
                    frequency = "yearly"
                    break

                print("\nEnter a number between 1 - 3")

            expense.changeFrequency(frequency)
            self.saveExpenses()
        elif choice == "4":
            expense.displayExpense()
        elif choice == "5":
            return
        else:
            print("Enter a number between 1 - 5.")

    def run(self):
        """Main loop for running the program"""
        while True:
            print("\n===== Expense Tracker =====")
            print("1. Create a new expense")
            print("2. Open an existing expense")
            print("3. Delete an expense")
            print("4. Display all expenses")
            print("5. Exit")

            choice = input("\nEnter your choice (1 - 5): ")

            if choice == "1":
                self.createExpense()
            elif choice == "2":
                self.openExpense()
            elif choice == "3":
                self.deleteExpense()
            elif choice == "4":
                self.displayAllExpenses()
            elif choice == "5":
                print("\nGoodbye.")
                self.saveExpenses()
                break
            else:
                print("\nEnter a number between 1 - 5.")

clear()
e = Expenses()
e.run()

print("\nThanks for using!")
