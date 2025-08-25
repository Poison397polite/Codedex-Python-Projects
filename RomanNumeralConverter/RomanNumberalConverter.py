"""Converts roman numerals to numbers and vise versa"""

from Clear import clear

# List of roman numerals and their corresponding value
# for converting roman numerals to integers
romanToInt = {
    "I" : 1, "V" : 5, "X" : 10, "L" : 50,
    "C" : 100, "D" : 500, "M" : 1000
}

# List of integers and their corresponding roman numeral symbol
# for converting integers to roman numerals
intToRoman = {
    1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C",
    90 : "XC", 50 : "L", 40 : "XL", 10 : "X", 9 : "IX",
    5 : "V", 4 : "IV", 1 : "I"
}

def printTitleAndNumbers():
    """Prints the title and the roman numerals"""
    print("----------------------------------------------------")
    print("              Roman numeral converter               ")
    print("  Convert any whole number from 1 to 3999 to roman  ")
    print(" numeral and any standard roman numeral to a whole  ")
    print("                       number                       ")
    for key, value in romanToInt.items():
        line = f"{value} = {key}"
        print(f"{line:^52}")
    print("----------------------------------------------------")

def roman2Int(roman : str) -> int:
    """Converts a roman numeral to an integer and returns it as an int"""
    # Keeps track of the last symbol to check if it needs to subtract
    last = 0

    # Keeps track of the total number
    convertedRoman = 0

    # Loop from right to left to subtract correctly
    for letter in reversed(roman):
        value = romanToInt[letter]

        # If symbol after the last one is a smaller value subtract it from the total
        # else add it to the total
        if value < last:
            convertedRoman -= value
        else:
            convertedRoman += value

        last = value

    return convertedRoman

def int2Roman(number : int) -> str:
    """Converts an int to roman numeral and returns it as a string"""
    # Keeps track of the converted symbols in order
    convertedNum = []

    # Loops through all the items in the intToRoman dictionary
    # and saves the key to key and the value to value
    for key, value in intToRoman.items():
        # While the number is >= the key in the intToRoman dictionary
        # append the current value to the convertedNum list
        # and subtract the key from the number
        while number >= key:
            convertedNum.append(value)
            number -= key

    # Joins all the strings in the convertedNum list to make one list
    # of all the symbols to make the correct roman numeral
    return "".join(convertedNum)


printTitleAndNumbers()

# Loop and ask if the user wants convert from roman numeral to integers
# or convert from integers to roman numerals
# break out of the loop if the user wants too
while True:
    romanOrInt = input("\nConvert whole number to roman numeral(a) or vise versa(b): ").lower()

    if romanOrInt == "a":
        while True:
            try:
                while True:
                    numberToConvert = int(input("\nEnter the number to convert: "))
                    if numberToConvert > 3999:
                        print("\nNumber must be 3999 or smaller")
                    else:
                        break
                break
            except ValueError:
                print("\nInvalid input. Enter a number.")

        print(f"\n{numberToConvert:,} = {int2Roman(numberToConvert)}")

    elif romanOrInt == "b":
        romanToConvert = input("\nEnter the roman numeral to convert: ").upper().strip()
        print(f"\n{romanToConvert} = {roman2Int(romanToConvert):,}")

    if input("\nConvert another? (y/n): ").lower() == "y":
        clear()
        printTitleAndNumbers()
        continue

    break

print("\nThanks for using!")
