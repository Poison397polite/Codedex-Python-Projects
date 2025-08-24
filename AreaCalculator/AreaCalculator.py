"""Program to get the area of many different shapes"""

import math
import os

def clear():
    """Clears all text in the console when called"""
    os.system("cls")

shapeList = [ # List of all the shapes
    "Square", "Rectangle", "Triangle", "Circle", "Semicircle",
    "Sector", "Ellipse", "Trapezoid", "Parallelogram", "Rhombus",
    "Kite", "Pentagon", "Hexagon", "Octagon", "Annulus (ring)",
    "Irregular quadrilateral", "Regular polygon"
]

def printTitleAndShapes():
    """Prints the title and all shapes available when called"""
    print("----------------------------------------------------")
    print("                  Area Calculator                   ")
    print("                    All shapes:                     ")
    for s in shapeList:
        print(f"{s:^50}") # center aligned
    print("----------------------------------------------------")

def getFloat(prompt: str) -> float:
    """Get a float from the user with validation"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")

def formatArea(a: float) -> str:
    """Formats a float to have 2 decimal places and commas"""
    return f"{round(a, 2):,}" # Always 2 decimal places, with commas

def areaSquare():
    """Calculates the area of a square"""
    squareSide = getFloat("Enter the side length: ")
    return squareSide ** 2

def areaRectangle():
    """Calculates the area of a rectangle"""
    a = getFloat("Enter side a length: ")
    b = getFloat("Enter side b length: ")
    return a * b

def areaTriangle():
    """Calculates the area of a triangle"""
    while True:
        triangleSolver = input("Solve with base and height(a), SAS(b), SSS(c), or ASA(d): ").lower()
        if triangleSolver not in ["a", "b", "c", "d"]:
            print("Invalid input. Enter a, b, c, or d")
        else:
            break

    if triangleSolver == "a":
        base = getFloat("Enter the base length: ")
        height = getFloat("Enter the height length: ")
        return base * height / 2

    if triangleSolver == "b":
        a = getFloat("Enter side a length: ")
        b = getFloat("Enter side b length: ")
        angle = getFloat("Enter the angle between the sides (in degrees): ")
        return (0.5 * a * b * math.sin(math.radians(angle)))

    if triangleSolver == "c":
        a = getFloat("Enter side a length: ")
        b = getFloat("Enter side b length: ")
        c = getFloat("Enter side c length: ")
        return 0.25 * math.sqrt((a + b + c) * ((a * -1) + b + c) * (a - b + c) * (a + b - c))

    angleA = getFloat("Enter angle a (in degrees): ")
    angleB = getFloat("Enter angle b (in degrees): ")
    a = getFloat("Enter the side length between the angles: ")
    return a ** 2 * math.sin(math.radians(angleA)) * math.sin(math.radians(angleB)) / (2 * math.sin(math.radians(angleA) + math.radians(angleB)))

def areaCircle():
    """Calculates the area of a circle"""
    while True:
        circleSolver = input("Solve with radius(a), diameter(b), or circumference(c): ").lower()
        if circleSolver not in ["a", "b", "c"]:
            print("Invalid input. Enter a, b, or c")
        else:
            break

    if circleSolver == "a":
        radius = getFloat("Enter the radius length: ")
        return math.pi * radius ** 2

    if circleSolver == "b":
        diameter = getFloat("Enter the diameter length: ")
        return math.pi * (diameter / 2) ** 2

    circumference = getFloat("Enter the circumference length: ")
    return circumference ** 2 / (4 * math.pi)

def areaSemicircle():
    """Calculates the area of a semicircle"""
    while True:
        semiCircleSolver = input("Solve with radius(a), diameter(b), or circumference(c): ").lower()
        if semiCircleSolver not in ["a", "b", "c"]:
            print("Invalid input. Enter a, b, or c")
        else:
            break

    if semiCircleSolver == "a":
        radius = getFloat("Enter the radius length: ")
        return (math.pi * radius ** 2) / 2

    if semiCircleSolver == "b":
        diameter = getFloat("Enter the diameter length: ")
        return (math.pi * (diameter / 2) ** 2) / 2

    circumference = getFloat("Enter the circumference length: ")
    return (math.pi * (circumference / (math.pi + 2)) ** 2) / 2

def areaSector():
    """Calculates the area of a sector"""
    radius = getFloat("Enter the radius length: ")
    angle = getFloat("Enter the angle (in degrees): ")
    return (angle / 360) * (math.pi * radius ** 2)

def areaEllipse():
    """Calculates the area of a ellipse"""
    radiusA = getFloat("Enter radius a length: ")
    radiusB = getFloat("Enter radius b length: ")
    return math.pi * radiusA * radiusB

def areaTrapezoid():
    """Calculates the area of a trapezoid"""
    a = getFloat("Enter side a length: ")
    b = getFloat("Enter side b length: ")
    height = getFloat("Enter height length: ")
    return (a + b) * height / 2

def areaParallelogram():
    """Calculates the area of a parallelogram"""
    while True:
        parallelogramSolver = input("Solve with base and height(a), sides and angle between them(b), or diagonals and angle between them(c)").lower()
        if parallelogramSolver not in ["a", "b", "c"]:
            print("Invalid input. Enter a, b, or c")
        else:
            break

    if parallelogramSolver == "a":
        base = getFloat("Enter the base length: ")
        height = getFloat("Enter the height length: ")
        return base * height

    if parallelogramSolver == "b":
        a = getFloat("Enter side a length: ")
        b = getFloat("Enter side b length: ")
        angle = getFloat("Enter the angle between the sides (in degrees): ")
        return a * b * math.sin(math.radians(angle))

    a = getFloat("Enter diagonal a length: ")
    b = getFloat("Enter diagonal b length: ")
    angle = getFloat("Enter the angle between the diagonals (in degrees): ")
    return a * b * math.sin(math.radians(angle))

def areaRhombus():
    """Calculates the area of a rhombus"""
    while True:
        rhombusSolver = input("Solve with side and height(a), diagonals(b), or side and any angle(c): ").lower()
        if rhombusSolver not in ["a", "b", "c"]:
            print("Invalid input. Enter a, b, or c")
        else:
            break

    if rhombusSolver == "a":
        side = getFloat("Enter the side length: ")
        height = getFloat("Enter the height length: ")
        return side * height

    if rhombusSolver == "b":
        a = getFloat("Enter diagonal a length: ")
        b = getFloat("Enter diagonal b length: ")
        return (a * b) / 2

    side = getFloat("Enter the side length: ")
    angle = getFloat("Enter any angle (in degrees): ")
    return side ** 2 * math.sin(math.radians(angle))

def areaKite():
    """Calculates the area of a kite"""
    while True:
        kiteSolver = input("Solve with diagonals(a) or 2 unequal sides and the angle between them(b): ")
        if kiteSolver not in ["a", "b"]:
            print("Invalid input. Enter a or b")
        else:
            break

    if kiteSolver == "a":
        a = getFloat("Enter diagonal a length: ")
        b = getFloat("Enter diagonal b length: ")
        return (a * b) / 2

    a = getFloat("Enter side a length: ")
    b = getFloat("Enter side b length: ")
    angle = getFloat("Enter the angle between the sides (in degrees): ")
    return a * b * math.sin(math.radians(angle))

def areaPentagon():
    """Calculates the area of a pentagon"""
    side = getFloat("Enter the side length: ")
    return side ** 2 * math.sqrt(25 + 10 * math.sqrt(5)) / 4

def areaHexagon():
    """Calculates the area of a hexagon"""
    side = getFloat("Enter the side length: ")
    return 3 / 2 * math.sqrt(3) * side ** 2

def areaOctagon():
    """Calculates the area of a octagon"""
    side = getFloat("Enter the side length: ")
    return 2 * (1 + math.sqrt(2)) * side ** 2

def areaAnnulus():
    """Calculates the area of a annulus"""
    radiusA = getFloat("Enter the bigger radius (in degrees): ")
    radiusB = getFloat("Enter the smaller radius (in degrees): ")
    return math.pi * (radiusA ** 2 - radiusB ** 2)

def areaIQuadrilateral():
    """Calculates the area of an irregular quadrilateral"""
    a = getFloat("Enter diagonal a length: ")
    b = getFloat("Enter diagonal b length: ")
    angle = getFloat("Enter the angle between the diagonals (in degrees): ")
    return 1 / 2 * a * b * math.sin(math.radians(angle))

def areaRPolygon():
    """Calculates the area of a regular polygon"""
    sides = getFloat("Enter the amount of sides: ")
    side = getFloat("Enter the side length: ")
    return sides * side ** 2 * (1 / math.tan(math.pi / sides)) / 4

shapes = {
    "square" : areaSquare,
    "rectangle" : areaRectangle,
    "triangle" : areaTriangle,
    "circle" : areaCircle,
    "semicircle" : areaSemicircle,
    "sector" : areaSector,
    "ellipse" : areaEllipse,
    "trapezoid" : areaTrapezoid,
    "parallelogram" : areaParallelogram,
    "rhombus" : areaRhombus,
    "kite" : areaKite,
    "pentagon" : areaPentagon,
    "hexagon" : areaHexagon,
    "octagon" : areaOctagon,
    "annulus" : areaAnnulus,
    "irregular quadrilateral" : areaIQuadrilateral,
    "regular polygon" : areaRPolygon
}

printTitleAndShapes()

while True:
    while True:
        shape = input("Enter the name of the shape: ").lower()

        if shape not in shapes:
            print("Invalid input. Try again.")
        else:
            area = shapes[shape]()  # call the correct function
            print(f"The area of the {shape} is {formatArea(area)}")
            break

    if input("Another shape? (y/n): ").lower() != "y":
        break

    clear()
    printTitleAndShapes()

print("Thanks for using!")
