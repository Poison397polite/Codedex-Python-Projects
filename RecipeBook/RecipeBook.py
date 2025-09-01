"""Program to create and edit a recipe book"""

import os
import json
from Clear import clear

class Recipe:
    """Class to store and edit a recipe"""
    def __init__(self, name : str, ingredients : list, steps : list):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def getNumber(self, listType : str, prompt : str, addOrRemove = "remove") -> int:
        """Gets a number for indexing with validation"""
        while True:
            try:
                if listType == "ingredient":
                    if not self.ingredients:
                        print("\nNo ingredients. Add some.")
                        return None

                    number = int(input(f"\n{prompt}"))

                    if number < 1 or number > len(self.ingredients):
                        print("\nIngredient number doesn't exist. Try again.")
                        continue
                else:
                    if not self.steps:
                        print("\nNo steps. Add some.")
                        return None

                    number = int(input(f"\n{prompt}"))

                    if addOrRemove == "add":
                        if number < 1 or number - 1 > len(self.steps):
                            print("\nStep number doesn't exist. Try again.")
                            continue

                    if number < 1 or number > len(self.steps):
                        print("\nStep number doesn't exist. Try again.")
                        continue
                break
            except ValueError:
                print("\nInvalid input. Enter a number.")

        return number

    def changeName(self, newName : str):
        """Changes the name to the new name input"""
        self.name = newName
        print(f"\nChanged name to {newName}.")

    def changeIngredient(self):
        """Changes a specific ingredient"""
        ingredientNumber = self.getNumber("ingredient", "Enter the ingredient number: ")
        if ingredientNumber is None:
            return

        newIngredient = input("\nEnter the new ingredient: ")

        self.ingredients[ingredientNumber - 1] = newIngredient
        print(f"\nChanged ingredient {ingredientNumber} to {newIngredient}")

    def addIngredient(self):
        """Adds an ingredient"""
        ingredient = input("\nEnter the ingredient to add: ")
        self.ingredients.append(ingredient)
        print(f"\nAdded ingredient {ingredient}.")

    def removeIngredient(self):
        """Removes an ingredient"""
        ingredientNumber = self.getNumber("ingredient", "Enter the ingredient number: ")
        if ingredientNumber is None:
            return

        self.ingredients.pop(ingredientNumber - 1)
        print(f"Removed ingredient {ingredientNumber}.")

    def changeStep(self):
        """Changes a specific step"""
        stepNumber = self.getNumber("steps", "Enter the step number: ")
        if stepNumber is None:
            return

        newStep = input("\nEnter the new step: ")

        self.steps[stepNumber - 1] = newStep
        print(f"\nChanged step {stepNumber} to {newStep}.")

    def addStep(self):
        """Adds a step to the recipe"""
        stepNumber = self.getNumber("steps", "Enter the step number: ", addOrRemove = "add")

        step = input("\nEnter the step: ")

        if stepNumber is None:
            self.steps.append(step)
            print(f"\nAdded step 1: {step}.")
        else:
            self.steps.insert(stepNumber - 1, step)
            print(f"\nAdded step {stepNumber}: {step}.")

    def removeStep(self):
        """Removes a step from the recipe"""
        stepNumber = self.getNumber("steps", "Enter the step number: ")
        if stepNumber is None:
            return

        self.steps.pop(stepNumber - 1)
        print(f"\nRemoved step {stepNumber}.")

    def swap2Steps(self):
        """Swaps 2 steps"""
        step1 = self.getNumber("steps", "Enter the first step to swap: ")
        step2 = self.getNumber("steps", "Enter the second step to swap: ")
        if step1 is None or step2 is None:
            return

        self.steps[step1 - 1], self.steps[step2 - 1] = self.steps[step2 - 1], self.steps[step1 - 1]
        print(f"\nSwapped steps {step1} and {step2}.")

    def moveStep(self):
        """Moves a step to a new position"""
        stepNumber = self.getNumber("steps", "Enter the step to move: ")
        stepPosition = self.getNumber("steps", "Enter the step's new step number: ")
        if stepNumber is None or stepPosition is None:
            return

        step = self.steps.pop(stepNumber - 1)
        self.steps.insert(stepPosition - 1, step)
        print(f"\nMoved step {stepNumber} to step {stepPosition}.")

    def displayRecipe(self):
        """Displays the whole recipe in the console"""
        print(f"\n===== {self.name} =====")

        if not self.ingredients and not self.steps:
            print("No ingredients or steps. Add some.")

        elif not self.ingredients:
            print("No ingredients. Add some.")

            print("\nSteps:")
            for i, step in enumerate(self.steps, start = 1):
                print(f"Step {i}: {step}")

        elif not self.steps:
            print("Ingredients:")
            for i, ingredient in enumerate(self.ingredients, start = 1):
                print(f"Ingredient {i}: {ingredient}")

            print("\nNo steps. Add some.")

        else:
            print("Ingredients:")
            for i, ingredient in enumerate(self.ingredients, start = 1):
                print(f"Ingredient {i}: {ingredient}")

            print("\nSteps:")
            for i, step in enumerate(self.steps, start = 1):
                print(f"Step {i}: {step}")

    def toDict(self) -> dict:
        """Converts the recipe to a dictionary for storing"""
        return {"name" : self.name, "ingredients" : self.ingredients, "steps" : self.steps}

class RecipeBook:
    """Class to create and store recipes into a recipe book"""
    def __init__(self, fileName = "recipeBook.json"):
        self.fileName = fileName
        self.recipes = self.loadRecipes()

    def loadRecipes(self) -> dict:
        """Loads all saved recipes for the recipe book"""
        if os.path.exists(self.fileName):
            try:
                with open(self.fileName, "r", encoding = "utf8") as f:
                    data = json.load(f)
                    return {
                        name : Recipe(recipe["name"], recipe["ingredients"], recipe["steps"])
                        for name, recipe in data.items()
                    }
            except json.JSONDecodeError:
                print("\nWarning: recipeBook.json is corrupted. Starting fresh.")
                return{}
        return {}

    def saveRecipes(self):
        """Saves all recipes in the recipe book"""
        with open(self.fileName, "w", encoding = "utf8") as f:
            data = {name : recipe.toDict() for name, recipe in self.recipes.items()}
            json.dump(data, f, indent = 4)

    def createRecipe(self):
        """Creates a new recipe and saves it to the recipe book"""
        name = input("\nEnter the name of the recipe: ")
        if name in self.recipes:
            print("\nName already exists.")
            return

        ingredients = []
        ingredientNumber = 1
        while True:
            ingredient = input(f"\nEnter ingredient {ingredientNumber} (enter q when all ingredients entered to quit): ")
            if ingredient.lower() == "q":
                break
            ingredients.append(ingredient)
            ingredientNumber += 1

        steps = []
        stepNumber = 1
        while True:
            step = input(f"\nEnter step {stepNumber} (enter q when all steps entered to quit): ")
            if step.lower() == "q":
                break
            steps.append(step)
            stepNumber += 1

        self.recipes[name] = Recipe(name, ingredients, steps)
        self.saveRecipes()
        print(f"\nCreated recipe {name}.")

    def openRecipe(self):
        """Opens a saved recipe"""
        name = input("\nEnter the name of the recipe: ")
        recipe = self.recipes.get(name)

        if recipe:
            print(f"\nOpening recipe {name}...")
            self.recipeMenu(recipe)
        else:
            print("\nRecipe doesn't exist.")

    def deleteRecipe(self):
        """Deletes a recipe from the recipe book"""
        name = input("\nEnter the name of the recipe: ")

        if name in self.recipes:
            print(f"\nDeleting recipe {name}...")
            self.recipes.pop(name)
            self.saveRecipes()
        else:
            print("\nRecipe doesn't exist.")

    def displayRecipeBook(self):
        """Displays the whole recipe book"""
        if not self.recipes:
            print("\nNo recipes in the recipe book. Add some.")
            return

        print("\n===== Recipes =====")
        for name in self.recipes:
            print(f"- {name}")
        print("\nOpen a recipe for more details!")

    def recipeMenu(self, recipe : Recipe):
        """Menu for interacting with and editing a given recipe"""
        while True:
            print(f"\n===== Recipe menu: {recipe.name} =====")
            print("1. Change name")
            print("2. Change a certain ingredient")
            print("3. Add an ingredient")
            print("4. Remove an ingredient")
            print("5. Change a certain step")
            print("6. Add a step")
            print("7. Remove a step")
            print("8. Swap the place of 2 steps")
            print("9. Move a step to a new position")
            print("10. Display the recipe")
            print("11. Return to Recipe Book Menu")

            choice = input("\nEnter your choice (1 - 11): ")

            match choice:
                case "1":
                    newName = input("\nEnter the new name for the recipe: ")
                    if newName in self.recipes:
                        print("\nThat name already exists. Try again.")
                        continue

                    self.recipes[newName] = self.recipes.pop(recipe.name)
                    recipe.changeName(newName)
                    self.saveRecipes()

                case "2":
                    recipe.changeIngredient()
                    self.saveRecipes()

                case "3":
                    recipe.addIngredient()
                    self.saveRecipes()

                case "4":
                    recipe.removeIngredient()
                    self.saveRecipes()

                case "5":
                    recipe.changeStep()
                    self.saveRecipes()

                case "6":
                    recipe.addStep()
                    self.saveRecipes()

                case "7":
                    recipe.removeStep()
                    self.saveRecipes()

                case "8":
                    recipe.swap2Steps()
                    self.saveRecipes()

                case "9":
                    recipe.moveStep()
                    self.saveRecipes()

                case "10":
                    recipe.displayRecipe()

                case "11":
                    break

                case _:
                    print("\nInvalid input. Enter a number between 1 and 11")

    def run(self):
        """Main loop for working with the recipe book"""
        while True:
            print("\n===== Recipe Book Menu =====")
            print("1. Create a new recipe")
            print("2. Open a saved recipe")
            print("3. Delete a recipe")
            print("4. Display all of the recipe names in the recipe book")
            print("5. Exit")

            choice = input("\nEnter your choice (1 - 5): ")

            match choice:
                case "1":
                    self.createRecipe()

                case "2":
                    self.openRecipe()

                case "3":
                    self.deleteRecipe()

                case "4":
                    self.displayRecipeBook()

                case "5":
                    print("\nGoodbye!")
                    self.saveRecipes()
                    break

                case _:
                    print("\nInvalid input. Enter a number from 1 - 5.")

clear()
recipeBook = RecipeBook()
recipeBook.run()

print("\nThanks for using!")
