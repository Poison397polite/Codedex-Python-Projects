"""Area Calculator"""

import math
import time

print("-------------------------------------------------------")
print("                 Shape Area Calculator")
print("-------------------------------------------------------\n")

selectedShape = 0

while selectedShape != 5:

    print("Enter the shape you want to calculate the area for!")
    print("1) Square")
    print("2) Rectangle")
    print("3) Triangle")
    print("4) Circle")
    print("5) Quit\n")

    selectedShape = int(input("Which shape: "))

    if selectedShape == 1:
        squareSide = float(input("\nEnter the length: "))
        print(f"The area is {squareSide ** 2}")
    elif selectedShape == 2:
        rectangleLength = float(input("\nEnter the length: "))
        rectangleWidth = float(input("Enter the width: "))
        print(f"The area is {rectangleLength * rectangleWidth}")
    elif selectedShape == 3:
        triangleHeight = float(input("Enter the height: "))
        triangleBase = float(input("Enter the base: "))
        print(f"The area is {(triangleHeight * triangleBase) / 2}")
    elif selectedShape == 4:
        circleRadius = float(input("Enter the radius: "))
        print(f"The area is {math.pi * circleRadius ** 2}")
    elif selectedShape == 5:
        print("Thanks for using my program!\n")
    else:
        print("Invalid input!\n")
        time.sleep(0.5)
