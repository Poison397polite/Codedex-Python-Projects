"""Program to convert different metrics between each other"""

import os

def clear():
    """Function to clear the screen"""
    os.system("cls")

def printTitleAndUnits():
    """Function to print the title and the convertible units"""
    print("----------------------------------------------------")
    print("               Metric conversion tool               ")
    print("                     Length(l):                     ")
    print("                  Millimeters(mm)                   ")
    print("                  Centimeters(cm)                   ")
    print("                     Inches(in)                     ")
    print("                   Decimeters(dm)                   ")
    print("                      Feet(ft)                      ")
    print("                     Yards(yd)                      ")
    print("                     Meters(m)                      ")
    print("                   Kilometers(km)                   ")
    print("                     Miles(mi)                      ")
    print("                                                    ")
    print("                  Temperature(t):                   ")
    print("                     Celsius(c)                     ")
    print("                   Fahrenheit(f)                    ")
    print("                     Kelvin(k)                      ")
    print("                                                    ")
    print("                     Weight(w):                     ")
    print("                   Milligrams(mg)                   ")
    print("                      Grams(g)                      ")
    print("                     Ounces(oz)                     ")
    print("                     Pounds(lb)                     ")
    print("                   Kilograms(kg)                    ")
    print("                                                    ")
    print("                     Speed(s):                      ")
    print("              Kilometers per hour(kph)              ")
    print("                Miles per hour(mph)                 ")
    print("                                                    ")
    print("                     Time(ti):                      ")
    print("                     Seconds(s)                     ")
    print("                     Minutes(m)                     ")
    print("                      Hours(h)                      ")
    print("                      Days(d)                       ")
    print("                      Years(y)                      ")
    print("----------------------------------------------------")

def getUnit(listOfUnits, unitNumber):
    """Function to get a unit with the input of the available units"""
    if unitNumber == 1:
        while True:
            unit = input("\nEnter the abbreviation of the unit you want to convert: ").lower()
            if unit not in listOfUnits:
                print("\nInvalid unit. Try again.")
            else:
                listOfUnits.remove(unit)
                break
    else:
        while True:
            unit = input("\nEnter the abbreviation of the unit you want to convert to: ").lower()
            if unit not in listOfUnits:
                print("\nInvalid unit. Try again.")
            else:
                listOfUnits.remove(unit)
                break

    return unit

def getAmount():
    """Function to get the amount of the unit to convert"""
    while True:
        try:
            amount = int(input("Enter the amount of the unit you want to convert: "))
            break
        except ValueError:
            print("Invalid input. Input a number.")

    return amount

printTitleAndUnits()

while True:
    # List for all the abbreviations for all the units
    listOfLengths = ["mm", "cm", "in", "dm", "ft", "yd", "m", "km", "mi"]
    listOfTemps = ["c", "f", "k"]
    listOfWeights = ["mg", "g", "oz", "lb", "kg"]
    listOfSpeeds = ["kph", "mph"]
    listOfTimes = ["s", "m", "h", "d", "y"]

    category = input("\nEnter the first letter of the category you want to convert: ").lower()

    # If category chosen is length
    if category == "l":
        # Get unit to convert and amount
        unit1 = getUnit(listOfLengths, 1)
        unitAmount = getAmount()

        # Get unit to convert to
        unit2 = getUnit(listOfLengths, 2)

        if unit1 == "mm" and unit2 == "cm":
            print(f"{unitAmount:,} millimeters is {unitAmount / 10:,} centimeters")

        elif unit1 == "mm" and unit2 == "in":
            print(f"{unitAmount:,} millimeters is {unitAmount / 25.4:,} inches")

        elif unit1 == "mm" and unit2 == "dm":
            print(f"{unitAmount:,} millimeters is {unitAmount / 100:,} decimeters")

        elif unit1 == "mm" and unit2 == "ft":
            print(f"{unitAmount:,} millimeters is {unitAmount / 304.79999025:,} feet")

        elif unit1 == "mm" and unit2 == "yd":
            print(f"{unitAmount:,} millimeters is {unitAmount / 914.40275784:,} yards")

        elif unit1 == "mm" and unit2 == "m":
            print(f"{unitAmount:,} millimeters is {unitAmount / 1000:,} meters")

        elif unit1 == "mm" and unit2 == "km":
            print(f"{unitAmount:,} millimeters is {unitAmount / 1000000:,} kilometers")

        elif unit1 == "mm" and unit2 == "mi":
            print(f"{unitAmount:,} millimeters is {unitAmount / 1612903.2258065:,} miles")

        elif unit1 == "cm" and unit2 == "mm":
            print(f"{unitAmount:,} centimeters is {unitAmount * 10:,} millimeters")

        elif unit1 == "cm" and unit2 == "in":
            print(f"{unitAmount:,} centimeters is {unitAmount / 2.54:,} inches")

        elif unit1 == "cm" and unit2 == "dm":
            print(f"{unitAmount:,} centimeters is {unitAmount / 10:,} decimeters")

        elif unit1 == "cm" and unit2 == "ft":
            print(f"{unitAmount:,} centimeters is {unitAmount / 30.47999902:,} feet")

        elif unit1 == "cm" and unit2 == "yd":
            print(f"{unitAmount:,} centimeters is {unitAmount / 91.44027578:,} yards")

        elif unit1 == "cm" and unit2 == "m":
            print(f"{unitAmount:,} centimeters is {unitAmount / 100:,} meters")

        elif unit1 == "cm" and unit2 == "km":
            print(f"{unitAmount:,} centimeters is {unitAmount / 100000:,} kilometers")

        elif unit1 == "cm" and unit2 == "mi":
            print(f"{unitAmount:,} centimeters is {unitAmount / 161030.59581321:,} miles")

        elif unit1 == "in" and unit2 == "mm":
            print(f"{unitAmount:,} inches is {unitAmount * 25.4:,} millimeters")

        elif unit1 == "in" and unit2 == "cm":
            print(f"{unitAmount:,} inches is {unitAmount * 2.54:,} centimeters")

        elif unit1 == "in" and unit2 == "dm":
            print(f"{unitAmount:,} inches is {unitAmount / 3.93701004:,} decimeters")

        elif unit1 == "in" and unit2 == "ft":
            print(f"{unitAmount:,} inches is {unitAmount / 12:,} feet")

        elif unit1 == "in" and unit2 == "yd":
            print(f"{unitAmount:,} inches is {unitAmount / 36:,} yards")

        elif unit1 == "in" and unit2 == "m":
            print(f"{unitAmount:,} inches is {unitAmount / 39.37009424:,} meters")

        elif unit1 == "in" and unit2 == "km":
            print(f"{unitAmount:,} inches is {unitAmount / 39370.07874016:,} kilometers")

        elif unit1 == "in" and unit2 == "mi":
            print(f"{unitAmount:,} inches is {unitAmount / 63360:,} miles")

        elif unit1 == "dm" and unit2 == "mm":
            print(f"{unitAmount:,} decimeters is {unitAmount * 100:,} millimeters")

        elif unit1 == "dm" and unit2 == "cm":
            print(f"{unitAmount:,} decimeters is {unitAmount * 10:,} centimeters")

        elif unit1 == "dm" and unit2 == "in":
            print(f"{unitAmount:,} decimeters is {unitAmount * 3.93701:,} inches")

        elif unit1 == "dm" and unit2 == "ft":
            print(f"{unitAmount:,} decimeters is {unitAmount / 3.0479999:,} feet")

        elif unit1 == "dm" and unit2 == "yd":
            print(f"{unitAmount:,} decimeters is {unitAmount / 9.14402758:,} yards")

        elif unit1 == "dm" and unit2 == "m":
            print(f"{unitAmount:,} decimeters is {unitAmount / 10:,} meters")

        elif unit1 == "dm" and unit2 == "km":
            print(f"{unitAmount:,} decimeters is {unitAmount / 10000:,} kilometers")

        elif unit1 == "dm" and unit2 == "mi":
            print(f"{unitAmount:,} decimeters is {unitAmount / 16092.69391696:,} miles")

        elif unit1 == "ft" and unit2 == "mm":
            print(f"{unitAmount:,} feet is {unitAmount * 304.79999025:,} millimeters")

        elif unit1 == "ft" and unit2 == "cm":
            print(f"{unitAmount:,} feet is {unitAmount * 30.47999902:,} centimeters")

        elif unit1 == "ft" and unit2 == "in":
            print(f"{unitAmount:,} feet is {unitAmount * 12:,} inches")

        elif unit1 == "ft" and unit2 == "dm":
            print(f"{unitAmount:,} feet is {unitAmount * 3.0479999:,} decimeters")

        elif unit1 == "ft" and unit2 == "yd":
            print(f"{unitAmount:,} feet is {unitAmount / 3:,} yards")

        elif unit1 == "ft" and unit2 == "m":
            print(f"{unitAmount:,} feet is {unitAmount / 3.28084:,} meters")

        elif unit1 == "ft" and unit2 == "km":
            print(f"{unitAmount:,} feet is {unitAmount / 3280.83989501:,} kilometers")

        elif unit1 == "ft" and unit2 == "mi":
            print(f"{unitAmount:,} feet is {unitAmount / 5280:,} miles")

        elif unit1 == "yd" and unit2 == "mm":
            print(f"{unitAmount:,} yards is {unitAmount * 914.40275784:,} millimeters")

        elif unit1 == "yd" and unit2 == "cm":
            print(f"{unitAmount:,} yards is {unitAmount * 91.44027578:,} centimeters")

        elif unit1 == "yd" and unit2 == "in":
            print(f"{unitAmount:,} yards is {unitAmount * 36:,} inches")

        elif unit1 == "yd" and unit2 == "dm":
            print(f"{unitAmount:,} yards is {unitAmount * 9.14402758:,} decimeters")

        elif unit1 == "yd" and unit2 == "ft":
            print(f"{unitAmount:,} yards is {unitAmount * 3:,} feet")

        elif unit1 == "yd" and unit2 == "m":
            print(f"{unitAmount:,} yards is {unitAmount / 1.09361:,} meters")

        elif unit1 == "yd" and unit2 == "km":
            print(f"{unitAmount:,} yards is {unitAmount / 1093.61329834:,} kilometers")

        elif unit1 == "yd" and unit2 == "mi":
            print(f"{unitAmount:,} yards is {unitAmount / 1760:,} miles")

        elif unit1 == "m" and unit2 == "mm":
            print(f"{unitAmount:,} meters is {unitAmount * 1000:,} millimeters")

        elif unit1 == "m" and unit2 == "cm":
            print(f"{unitAmount:,} meters is {unitAmount * 100:,} centimeters")

        elif unit1 == "m" and unit2 == "in":
            print(f"{unitAmount:,} meters is {unitAmount * 39.3701:,} inches")

        elif unit1 == "m" and unit2 == "dm":
            print(f"{unitAmount:,} meters is {unitAmount * 10:,} decimeters")

        elif unit1 == "m" and unit2 == "ft":
            print(f"{unitAmount:,} meters is {unitAmount * 3.28084:,} feet")

        elif unit1 == "m" and unit2 == "yd":
            print(f"{unitAmount:,} meters is {unitAmount * 1.09361:,} yards")

        elif unit1 == "m" and unit2 == "km":
            print(f"{unitAmount:,} meters is {unitAmount / 1000:,} kilometers")

        elif unit1 == "m" and unit2 == "mi":
            print(f"{unitAmount:,} meters is {unitAmount / 1609.34708789:,} miles")

        elif unit1 == "km" and unit2 == "mm":
            print(f"{unitAmount:,} kilometers is {unitAmount * 1000000:,} millimeters")

        elif unit1 == "km" and unit2 == "cm":
            print(f"{unitAmount:,} kilometers is {unitAmount * 100000:,} centimeters")

        elif unit1 == "km" and unit2 == "in":
            print(f"{unitAmount:,} kilometers is {unitAmount * 39370.1:,} inches")

        elif unit1 == "km" and unit2 == "dm":
            print(f"{unitAmount:,} kilometers is {unitAmount * 10000:,} decimeters")

        elif unit1 == "km" and unit2 == "ft":
            print(f"{unitAmount:,} kilometers is {unitAmount * 3280.84:,} feet")

        elif unit1 == "km" and unit2 == "yd":
            print(f"{unitAmount:,} kilometers is {unitAmount * 1093.61:,} yards")

        elif unit1 == "km" and unit2 == "m":
            print(f"{unitAmount:,} kilometers is {unitAmount * 1000:,} meters")

        elif unit1 == "km" and unit2 == "mi":
            print(f"{unitAmount:,} kilometers is {unitAmount / 1.6093445:,} miles")

        elif unit1 == "mi" and unit2 == "mm":
            print(f"{unitAmount:,} miles is {unitAmount * 1609344.4978926:,} millimeters")

        elif unit1 == "mi" and unit2 == "cm":
            print(f"{unitAmount:,} miles is {unitAmount * 160934.44978926:,} centimeters")

        elif unit1 == "mi" and unit2 == "in":
            print(f"{unitAmount:,} miles is {unitAmount * 63360:,} inches")

        elif unit1 == "mi" and unit2 == "dm":
            print(f"{unitAmount:,} miles is {unitAmount * 16093.44497893:,} decimeters")

        elif unit1 == "mi" and unit2 == "ft":
            print(f"{unitAmount:,} miles is {unitAmount * 5280:,} feet")

        elif unit1 == "mi" and unit2 == "yd":
            print(f"{unitAmount:,} miles is {unitAmount * 1760:,} yards")

        elif unit1 == "mi" and unit2 == "m":
            print(f"{unitAmount:,} miles is {unitAmount * 1609.34449789:,} meters")

        elif unit1 == "mi" and unit2 == "km":
            print(f"{unitAmount:,} miles is {unitAmount * 1.6093445:,} kilometers")

    # If category chosen is temperature
    elif category == "t":
        # Get unit to convert and amount
        unit1 = getUnit(listOfTemps, 1)
        unitAmount = getAmount()

        # Get unit to convert to
        unit2 = getUnit(listOfTemps, 2)

        if unit1 == "c" and unit2 == "f":
            print(f"{unitAmount:,} celsius is {(unitAmount * 1.8) + 32:,} fahrenheit")

        elif unit1 == "c" and unit2 == "k":
            print(f"{unitAmount:,} celsius is {unitAmount + 273.15:,} kelvin")

        elif unit1 == "f" and unit2 == "c":
            print(f"{unitAmount:,} fahrenheit is {(unitAmount - 32) / 1.8:,} celsius")

        elif unit1 == "f" and unit2 == "k":
            print(f"{unitAmount:,} fahrenheit is {((unitAmount - 32) / 1.8) + 273.15:,} kelvin")

        elif unit1 == "k" and unit2 == "c":
            print(f"{unitAmount:,} kelvin is {unitAmount - 273.15:,} celsius")

        elif unit1 == "k" and unit2 == "f":
            print(f"{unitAmount:,} kelvin is {((unitAmount - 273.15) * 1.8) + 32:,} fahrenheit")

    # If category chosen is weight
    elif category == "w":
        # Get unit to convert and amount
        unit1 = getUnit(listOfWeights, 1)
        unitAmount = getAmount()

        # Get unit to convert to
        unit2 = getUnit(listOfWeights, 2)

        if unit1 == "mg" and unit2 == "g":
            print(f"{unitAmount:,} milligrams is {unitAmount / 1000:,} grams")

        elif unit1 == "mg" and unit2 == "oz":
            print(f"{unitAmount:,} milligrams is {unitAmount / 28352.70768358:,} ounces")

        elif unit1 == "mg" and unit2 == "lb":
            print(f"{unitAmount:,} milligrams is {unitAmount / 454545.45454546:,} pounds")

        elif unit1 == "mg" and unit2 == "kg":
            print(f"{unitAmount:,} milligrams is {unitAmount / 1000000:,} kilograms")

        elif unit1 == "g" and unit2 == "mg":
            print(f"{unitAmount:,} grams is {unitAmount * 1000:,} milligrams")

        elif unit1 == "g" and unit2 == "oz":
            print(f"{unitAmount:,} grams is {unitAmount / 28.34949254:,} ounces")

        elif unit1 == "g" and unit2 == "lb":
            print(f"{unitAmount:,} grams is {unitAmount / 453.59290944:,} pounds")

        elif unit1 == "g" and unit2 == "kg":
            print(f"{unitAmount:,} grams is {unitAmount / 1000:,} kilograms")

        elif unit1 == "oz" and unit2 == "mg":
            print(f"{unitAmount:,} ounces is {unitAmount * 28349.49254408:,} milligrams")

        elif unit1 == "oz" and unit2 == "g":
            print(f"{unitAmount:,} ounces is {unitAmount * 28.34949254:,} grams")

        elif unit1 == "oz" and unit2 == "lb":
            print(f"{unitAmount:,} ounces is {unitAmount / 16:,} pounds")

        elif unit1 == "oz" and unit2 == "kg":
            print(f"{unitAmount:,} ounces is {unitAmount / 35.27400317:,} kilograms")

        elif unit1 == "lb" and unit2 == "mg":
            print(f"{unitAmount:,} pounds is {unitAmount * 453592.90943564:,} milligrams")

        elif unit1 == "lb" and unit2 == "g":
            print(f"{unitAmount:,} pounds is {unitAmount * 453.59290944:,} grams")

        elif unit1 == "lb" and unit2 == "oz":
            print(f"{unitAmount:,} pounds is {unitAmount * 16:,} ounces")

        elif unit1 == "lb" and unit2 == "kg":
            print(f"{unitAmount:,} pounds is {unitAmount / 2.20462:,} kilograms")

        elif unit1 == "kg" and unit2 == "mg":
            print(f"{unitAmount:,} kilograms is {unitAmount * 1000000:,} milligrams")

        elif unit1 == "kg" and unit2 == "g":
            print(f"{unitAmount:,} kilograms is {unitAmount * 1000:,} grams")

        elif unit1 == "kg" and unit2 == "oz":
            print(f"{unitAmount:,} kilograms is {unitAmount * 35.274:,} ounces")

        elif unit1 == "kg" and unit2 == "lb":
            print(f"{unitAmount:,} kilograms is {unitAmount * 2.20462:,} pounds")

    # If category chosen is speed
    elif category == "s":
        # Get unit to convert and amount
        unit1 = getUnit(listOfSpeeds, 1)
        unitAmount = getAmount()

        # Get unit to convert to
        unit2 = getUnit(listOfSpeeds, 2)

        if unit1 == "kph" and unit2 == "mph":
            print(f"{unitAmount:,} kph is {unitAmount / 1.60934134:,} mph")

        elif unit1 == "mph" and unit2 == "kph":
            print(f"{unitAmount:,} mph is {unitAmount * 1.60934133:,} kph")

    # If category chosen is time
    elif category == "ti":
        # Get unit to convert and amount
        unit1 = getUnit(listOfTimes, 1)
        unitAmount = getAmount()

        # Get unit to convert to
        unit2 = getUnit(listOfTimes, 2)

        if unit1 == "s" and unit2 == "m":
            print(f"{unitAmount:,} seconds is {unitAmount / 59.99988000024:,} minutes")

        elif unit1 == "s" and unit2 == "h":
            print(f"{unitAmount:,} seconds is {unitAmount / 3599.9971200023:,} hours")

        elif unit1 == "s" and unit2 == "d":
            print(f"{unitAmount:,} seconds is {unitAmount / 86399.806464434:,} days")

        elif unit1 == "s" and unit2 == "y":
            print(f"{unitAmount:,} seconds is {unitAmount / 31540000:,} years")

        elif unit1 == "m" and unit2 == "s":
            print(f"{unitAmount:,} minutes is {unitAmount * 59.99988000024:,} seconds")

        elif unit1 == "m" and unit2 == "h":
            print(f"{unitAmount:,} minutes is {unitAmount / 60.000071999942:,} hours")

        elif unit1 == "m" and unit2 == "d":
            print(f"{unitAmount:,} minutes is {unitAmount / 1439.9996544008:,} days")

        elif unit1 == "m" and unit2 == "y":
            print(f"{unitAmount:,} minutes is {unitAmount / 525600:,} years")

        elif unit1 == "h" and unit2 == "s":
            print(f"{unitAmount:,} hours is {unitAmount * 3599.9971200023:,} seconds")

        elif unit1 == "h" and unit2 == "m":
            print(f"{unitAmount:,} hours is {unitAmount * 60.000071999942:,} minutes")

        elif unit1 == "h" and unit2 == "d":
            print(f"{unitAmount:,} hours is {unitAmount / 23.999965440077:,} days")

        elif unit1 == "h" and unit2 == "y":
            print(f"{unitAmount:,} hours is {unitAmount / 8760:,} years")

        elif unit1 == "d" and unit2 == "s":
            print(f"{unitAmount:,} days is {unitAmount * 86399.806464434:,} seconds")

        elif unit1 == "d" and unit2 == "m":
            print(f"{unitAmount:,} days is {unitAmount * 1439.9996544008:,} minutes")

        elif unit1 == "d" and unit2 == "h":
            print(f"{unitAmount:,} days is {unitAmount * 23.999965440077:,} hours")

        elif unit1 == "d" and unit2 == "y":
            print(f"{unitAmount:,} days is {unitAmount / 365:,} years")

        elif unit1 == "y" and unit2 == "s":
            print(f"{unitAmount:,} years is {unitAmount * 31540000:,} seconds")

        elif unit1 == "y" and unit2 == "m":
            print(f"{unitAmount:,} years is {unitAmount * 525600:,} minutes")

        elif unit1 == "y" and unit2 == "h":
            print(f"{unitAmount:,} years is {unitAmount * 8760:,} hours")

        elif unit1 == "y" and unit2 == "d":
            print(f"{unitAmount:,} years is {unitAmount * 365:,} days")

    else:
        print("Invalid input, Try again.")

    if input("Convert another? y for yes anything else for no: ").lower() != "y":
        break

    clear()
    printTitleAndUnits()
