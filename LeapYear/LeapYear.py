"""Program that calculates if a year is a leap year or not"""

while True:
    year = int(input("\nEnter a year: "))

    if year % 4 == 0 and year % 100 != 0:
        print(f"\n{year} is a leap year!")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(f"\n{year} is a leap year!")
    else:
        print(f"\n{year} is not a leap year!")

    if input("\nEnter another year? y for yes anything else for no: ").lower() != "y":
        break

print("Thanks for using my program!")
