"""Program to convert different metrics between each other"""

import os

def clear():
    """Function to clear the screen"""
    os.system("cls")

def printTitleAndUnits():
    """Function to print the title and the convertible units"""
    print("----------------------------------------------------")
    print("               Metric conversion tool               ")
    print("                                                    ")
    print("    Length(l): mm, cm, in, dm, ft, yd, m, km, mi    ")
    print("              Temperature(t): c, f, k               ")
    print("            Weight(w): mg, g, oz, lb, kg            ")
    print("                 Speed(s): kph, mph                 ")
    print("              Time(ti): s, m, h, d, y               ")
    print("----------------------------------------------------")

lengthFactors = {
    "mm" : 0.001, "cm" : 0.01, "in" : 0.0254, "dm" : 0.1,
    "ft" : 0.3048, "yd" : 0.9144, "m" : 1, "km" : 1000, "mi" : 1609.3445
}

weightFactors = {
    "mg" : 0.001, "g" : 1, "oz" : 28.3495,
    "lb" : 453.592, "kg" : 1000
}

speedFactors = {
    "kph" : 1, "mph": 1.60934
}

timeFactors = {
    "s" : 1, "m" : 60, "h" : 3600,
    "d" : 86400, "y" : 31536000
}

def convertUsingFactors(amount2, fromUnit, toUnit, factors2):
    """Convert between units using a factor dictionary with a base unit"""
    return amount2 * (factors2[fromUnit] / factors[toUnit])

def convertTemperature(amount2, fromUnit, toUnit):
    """Special handling for temperature"""
    if fromUnit == toUnit:
        return amount2
    if fromUnit == "c" and toUnit == "f":
        return (amount2 * 1.8) + 32
    if fromUnit == "f" and toUnit == "c":
        return (amount2 - 32) * 1.8
    if fromUnit == "c" and toUnit == "k":
        return amount2 + 273.15
    if fromUnit == "k" and toUnit == "c":
        return amount2 - 273.15
    if fromUnit == "f" and toUnit == "k":
        return (amount2 - 32) * 1.8 + 273.15
    if fromUnit == "k" and toUnit == "f":
        return (amount2 - 273.15) * 1.8 + 32
    return None

def getUnit(availableUnits, prompt):
    """Ask the user for a unit until valid"""
    while True:
        unit = input(prompt).lower()
        if unit not in availableUnits:
            print("Invalid unit. Try again.")
        else:
            return unit

def getAmount():
    """Ask the user for a numeric amount"""
    while True:
        try:
            return float(input("Enter the amount: "))
        except ValueError:
            print("Invalid input. Enter a number.")

categories = {
    "l" : ("Length", lengthFactors, convertUsingFactors),
    "w" : ("Weight", weightFactors, convertUsingFactors),
    "s" : ("Speed", speedFactors, convertUsingFactors),
    "ti" : ("Time", timeFactors, convertUsingFactors),
    "t" : ("Temperature", None, convertTemperature)
}

printTitleAndUnits()

while True:
    category = input("\nEnter category (l/w/s/t/ti): ").lower()

    if category not in categories:
        print("Invalid category. Try again.")
        continue

    name, factors, converter = categories[category]
    print(f"\nSelected: {name}")

    if category == "t": # Temperature
        unit1 = getUnit(["c", "f", "k"], "From (c/f/k): ")
        amount = getAmount()
        unit2 = getUnit(["c", "f", "k"], "To (c/f/k): ")
        result = converter(amount, unit1, unit2)

    else: # Factor-based
        units = list(factors.keys())
        unit1 = getUnit(units, f"From {units}: ")
        amount = getAmount()
        unit2 = getUnit(units, f"To {units}: ")
        result = converter(amount, unit1, unit2, factors)

    print(f"\n{amount:,} {unit1} = {result:,} {unit2}\n")

    if input("Convert another? (y/n): ").lower() != "y":
        break

    clear()
    printTitleAndUnits()
