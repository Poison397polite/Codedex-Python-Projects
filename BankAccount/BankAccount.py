"""Program that functions as a simple bank account"""

import json
import os
from argon2 import PasswordHasher, exceptions

# Uses argon2 to hash the pin
ph = PasswordHasher(
    time_cost = 3, # Number of iterations
    memory_cost = 64_000, # in KiB (64 MB)
    parallelism = 2
)

def hashPin(pin: str) -> str:
    """Function to return a secure hash or the PIN"""
    return ph.hash(pin)

def verifyPin(hashStr: str, candidate: str) -> bool:
    """Checks if the pin entered is correct"""
    try:
        return ph.verify(hashStr, candidate)
    except exceptions.VerifyMismatchError:
        return False

class BankAccount:
    """Class to handle the functions of the current bank account"""
    def  __init__(self, owner : str, pinHash : str, balance = 0):
        self.owner = owner
        self.pinHash = pinHash
        self.balance = balance

    def deposit(self, amount : int) -> None:
        """Function to deposit a positive number into the balance of the bank account"""
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited ${amount:,}. New balance: ${self.balance:,}")
        else:
            print("\nDeposit amount must be positive.")

    def withdraw(self, amount : int) -> None:
        """Function to withdraw money from the bank account if its not higher then the balance"""
        if amount > self.balance:
            print("\nInsufficient funds!")
        elif amount <= 0:
            print("\nWithdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"\nWithdrew ${amount:,}. New balance: ${self.balance:,}")

    def getBalance(self) -> int:
        """Function to check the account in the bank account"""
        return self.balance

    def checkPin(self, enteredPin):
        """Checks if the pin entered is correct for the bank account"""
        return verifyPin(self.pinHash, enteredPin)

    def toDict(self):
        """Function to convert the account to a dictionary for storing"""
        return {"owner" : self.owner, "pinHash" : self.pinHash, "balance" : self.balance}

class BankSystem:
    """Class to handle getting into a specific bank account"""
    def __init__(self, filename = "accounts.json"):
        self.filename = filename
        self.accounts = self.loadAccounts()

    def loadAccounts(self):
        """Function to load all saved accounts"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding = "utf8") as f:
                data = json.load(f)
                return{
                    name: BankAccount(acc["owner"], acc["pinHash"], acc["balance"])
                    for name, acc in data.items()
                }
        return {}

    def saveAccounts(self):
        """Function to save all accounts"""
        with open(self.filename, "w", encoding = "utf8") as f:
            data = {name: acc.toDict() for name, acc in self.accounts.items()}
            json.dump(data, f, indent = 4)

    def createAccount(self):
        """Function to create a new account at the bank"""
        name = input("\nEnter your name: ")
        pin = input("\nSet a 4-digit PIN: ")

        if name in self.accounts:
            print("\nAccount already exists!")
            return

        pinHash = hashPin(pin)
        self.accounts[name] = BankAccount(name, pinHash)
        self.saveAccounts()
        print(f"\nAccount created for {name}.")

    def login(self):
        """Function to log into an existing account at the bank"""
        name = input("\nEnter your name: ")
        pin = input("\nEnter your 4-digit PIN: ")
        account = self.accounts.get(name)

        if account and account.checkPin(pin):
            print(f"\nWelcome back, {name}!")
            self.accountMenu(account)

        else:
            print("\nInvalid name or PIN.")

    def accountMenu(self, account : BankAccount):
        """Function that handles the interaction with the current bank account"""
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Logout")

            choice = input("\nChoose an option (1 - 4): ")

            if choice == "1":
                while True:
                    try:
                        depositAmount = float(input("\nEnter amount to deposit: "))
                        break
                    except ValueError:
                        print("\nEnter a number.")
                account.deposit(depositAmount)
                self.saveAccounts()

            elif choice == "2":
                while True:
                    try:
                        withdrawAmount = float(input("\nEnter amount to withdraw: "))
                        break
                    except ValueError:
                        print("\nEnter a number.")
                account.withdraw(withdrawAmount)
                self.saveAccounts()

            elif choice == "3":
                print(f"\nCurrent balance: ${account.getBalance():,}")

            elif choice == "4":
                print("\nLogging out...")
                break

            else:
                print("\nInvalid option. Please try again.")

    def run(self):
        """Function that runs the login / create account part for the bank"""
        while True:
            print("\n===== Welcome to Bank Of Python =====")
            print("1. Create account")
            print("2. Login")
            print("3. Exit")

            choice = input("\nEnter your option (1 - 3): ")

            if choice == "1":
                self.createAccount()

            elif choice == "2":
                self.login()

            elif choice == "3":
                print("\nGoodbye!")
                self.saveAccounts()
                break

            else:
                print("\nInvalid option. Please try again.")

bank = BankSystem()
bank.run()

print("\nThanks for using!")
