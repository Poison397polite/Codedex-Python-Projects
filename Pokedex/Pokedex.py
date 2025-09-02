"""Program for storing a pokedex"""

import os
import json
import time
from dataclasses import dataclass, field, asdict
from Clear import clear

@dataclass
class PokemonIdentificationDetails:
    """Class the holds info about a pokemon's identification details"""
    species : str = "Unknown"
    npn : str = "Unknown"

@dataclass
class PokemonPhysicalDetails:
    """Class that holds info about a pokemon's physical details"""
    height : str = "Unknown"
    weight : str = "Unknown"
    gender : str = "Unknown"
    category : str = "Unknown"

@dataclass
class PokemonAbilityDetails:
    """Class that holds info about a pokemon's ability details"""
    ability : str = "Unknown"
    abilityInfo : str = "Unknown"

@dataclass
class PokemonTypeDetails:
    """Class that holds info about a pokemon's type details"""
    types : list[str] = field(default_factory = list)
    weaknesses : list[str] = field(default_factory = list)

@dataclass
class PokedexEntry:
    """Class to hold all of the pokemon's info"""
    identificationDetails : PokemonIdentificationDetails = field(default_factory = PokemonIdentificationDetails)
    physicalDetails : PokemonPhysicalDetails = field(default_factory = PokemonPhysicalDetails)
    abilityDetails : PokemonAbilityDetails = field(default_factory = PokemonAbilityDetails)
    typeDetails : PokemonTypeDetails = field(default_factory = PokemonTypeDetails)
    evolutions : list[str] = field(default_factory = list)
    stats : dict[str, str] = field(default_factory = dict)
    description : str = "Unknown"

class Pokedex:
    """Class to create and store pokedex entry's"""
    def __init__(self, fileName = "pokedex.json"):
        self.fileName = fileName
        self.pokedexEntrys = self.loadPokedexEntrys()

    def loadPokedexEntrys(self):
        """Loads all saved pokedex entrys into the pokedex"""
        if os.path.exists(self.fileName):
            try:
                with open(self.fileName, "r", encoding = "utf8") as f:
                    data = json.load(f)
                    return {
                        species : PokedexEntry(**pokemonInfo)
                        for species, pokemonInfo in data.items()
                    }
            except json.JSONDecodeError:
                print("\nWarning: pokedex.json is corrupted. Saving a backup as pokedexCorrupted.json.")
                os.rename(self.fileName, f"pokedexCorrupted{int(time.time())}.json")
                return {}
        return {}

    def savePokedexEntrys(self):
        """Saves all pokedex entrys"""
        with open(self.fileName, "w", encoding = "utf8") as f:
            data = {
                species : asdict(pokedexEntry)
                for species, pokedexEntry in self.pokedexEntrys.items()
            }
            json.dump(data, f, indent = 4)

    def getNumberAsString(self, prompt : str, checkLength = 0) -> str:
        """Gets a number as a string and validates that it is only numbers except for 1 decimal point"""
        while True:
            number = input(f"\n{prompt}")

            if not number.replace(".", "", 1).strip().isdigit():
                print("\nMake sure you input only number.")
                continue

            if checkLength > 0:
                if len(number) != checkLength:
                    print(f"\nMake sure the number entered is {checkLength} digits.")

            break

        return number

    def getListOfStrings(self, prompt : str) -> list[str]:
        """Gets a list of strings until user decides to quit out"""
        myList = []
        iteration = 1

        while True:
            newPrompt = prompt.format(iteration)

            listEntry = input(f"\n{newPrompt}")

            if listEntry.lower() == "q":
                break

            myList.append(listEntry)
            iteration += 1

        return myList

    def getIdentificationDetails(self) -> PokemonIdentificationDetails:
        """Gets the identification details of the pokemon"""
        species = input("\nEnter the species name of the pokemon (e.g. Pikachu): ")

        npn = self.getNumberAsString("Enter the pokemon's National Pokedex Number (e.g. 0025): ", checkLength = 4)

        return PokemonIdentificationDetails(species, npn)

    def getPhysicalDetails(self) -> PokemonPhysicalDetails:
        """Gets the physical details of the pokemon"""
        heightFeet = self.getNumberAsString("Enter the height in feet without inches that the pokemon is (e.g. 1): ")
        heightInches = self.getNumberAsString("Enter the remaining height in inches (e.g. 4): ")
        height = f"{heightFeet} ft {heightInches} in"

        weight = self.getNumberAsString("Enter the weight in lbs of the pokemon (e.g. 13.2): ")
        weight = f"{weight} lbs"

        while True:
            gender = input("\nEnter the gender(s) the pokemon can be (Male, Female, or Male And Female): ").strip().title()

            if gender not in ["Male", "Female", "Male And Female"]:
                print("\nYou must enter Male, Female, or Male And Female. Try again.")
                continue

            break

        category = input("\nEnter the pokemon's category (e.g. Mouse): ")

        return PokemonPhysicalDetails(height, weight, gender, category)

    def getAbilityDetails(self) -> PokemonAbilityDetails:
        """Gets the ability details of the pokemon"""
        ability = input("\nEnter the ability the pokemon has (e.g. Static): ")

        abilityInfo = input("\nEnter the ability info: ")

        return PokemonAbilityDetails(ability, abilityInfo)

    def getTypeDetails(self) -> PokemonTypeDetails:
        """Gets the type details of the pokemon"""
        types = self.getListOfStrings("Enter type {} of the pokemon (e.g. Electric) (enter q when done to quit): ")

        weaknesses = self.getListOfStrings("Enter weakness {} of the pokemon (e.g. Ground) (enter q when done to quit): ")

        return PokemonTypeDetails(types, weaknesses)

    def createPokedexEntry(self):
        """Creates a pokedex entry"""
        pokemonIdentificationDetails = self.getIdentificationDetails()

        if pokemonIdentificationDetails.species in self.pokedexEntrys:
            confirm = input(f"\n{pokemonIdentificationDetails.species} already exists. Overwrite? (y/n): ")
            if confirm.lower() != "y":
                print("\nCanceled.")
                return

        pokemonPhysicalDetails = self.getPhysicalDetails()
        pokemonAbilityDetails = self.getAbilityDetails()
        pokemonTypeDetails = self.getTypeDetails()
        evolutions = self.getListOfStrings("Enter evolution number {} (e.g. Pichu) (enter q when done to quit): ")
        stats = {
            "HP" : "0/15", "Attack" : "0/15", "Defense" : "0/15",
            "Special Attack" : "0/15", "Special Defense" : "0/15", "Speed" : "0/15"
        }
        for key in stats:
            while True:
                stat = input(f"\nEnter the {key} stat out of 15 (e.g. 3): ")

                if not stat.strip().isdigit():
                    print("\nMake sure to enter a number. Please try again.")
                    continue

                if int(stat) > 15 or int(stat) < 0:
                    print("\nMake sure the entered number is between 0 and 15: ")
                    continue

                break

            stats[key] = f"{stat}/15"

        description = input("\nEnter the description of the pokemon: ")

        self.pokedexEntrys[pokemonIdentificationDetails.species] = PokedexEntry(pokemonIdentificationDetails, pokemonPhysicalDetails, pokemonAbilityDetails, pokemonTypeDetails, evolutions, stats, description)
        self.savePokedexEntrys()
        print(f"\nCreated pokedex entry for {pokemonIdentificationDetails.species}.")

    def displayPokedexEntry(self, pokedexEntry : PokedexEntry, indent : int = 0):
        """Displays the pokedex entry for a given pokemon"""
        pokedexEntry = asdict(pokedexEntry)

        keyLabels = {
            "species" : "Species",
            "npn" : "National Pokedex Number",
            "height" : "Height",
            "weight" : "Weight",
            "gender" : "Gender",
            "category" : "Category",
            "ability" : "Ability",
            "abilityInfo" : "Ability Info",
            "types" : "Types",
            "weaknesses" : "Weaknesses",
            "evolutions" : "Evolutions",
            "stats" : "Stats",
            "description" : "Description",
            "hp" : "HP"
        }

        def prettifyKey(key : str) -> str:
            return keyLabels.get(key, key)

        def printDict(d : dict, level : int = 0):
            for key, value in d.items():
                label = prettifyKey(key)

                if isinstance(value, dict):
                    if key == "stats":
                        print("    " * level + f"{label}:")
                        printDict(value, level + 1)
                    else:
                        # Skip container labels (like IdentificationDetails)
                        printDict(value, level)

                elif isinstance(value, list):
                    if value:
                        print("    " * level + f"{label}: {", ".join(value)}")
                    else:
                        print("    " * level + f"{label}: {value}")

                else:
                    # Special case for National Pokedex Number
                    if key == "npn":
                        print("    " * level + f"{label}: #{value}")
                    else:
                        print("    " * level + f"{label}: {value}")

        print()
        printDict(pokedexEntry, indent)

    def displayPokemonInPokedex(self):
        """Displays all the saved pokemon in the pokedex"""
        print("\n===== Pokemon =====")
        for pokemon in self.pokedexEntrys:
            print(f"- {pokemon}")

    def deletePokedexEntry(self):
        """Deletes a pokedex entry"""
        species = input("\nEnter the species name (e.g. Pikachu): ")

        if species in self.pokedexEntrys:
            print(f"\nDeleting pokedex entry {species}...")
            self.pokedexEntrys.pop(species)
            self.savePokedexEntrys()
        else:
            print(f"Pokedex entry for {species} doesn't exist.")

    def run(self):
        """Main loop to use the program"""
        while True:
            print("\n===== Pokedex Menu =====")
            print("1. Create a new pokedex entry")
            print("2. Display a pokedex entry")
            print("3. Display available pokemon in pokedex")
            print("4. Delete a pokedex entry")
            print("5. Exit")

            choice = input("\nEnter your choice (1 - 5): ")

            match choice:
                case "1":
                    self.createPokedexEntry()

                case "2":
                    pokedexEntry = input("\nEnter the species name (e.g. Pikachu): ")

                    if pokedexEntry in self.pokedexEntrys:
                        self.displayPokedexEntry(self.pokedexEntrys[pokedexEntry])
                    else:
                        print(f"\nPokedex entry for {pokedexEntry} doesn't exist.")

                case "3":
                    self.displayPokemonInPokedex()

                case "4":
                    self.deletePokedexEntry()

                case "5":
                    print("\nGoodbye!")
                    self.savePokedexEntrys()
                    break

                case _:
                    print("\nInvalid input. Enter a number between 1 and 5.")

clear()
pokedex = Pokedex()
pokedex.run()

print("\nThanks for using!")
