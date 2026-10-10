from colorama import Fore, Style, Back

name = input("Enter your name: ")

objType = input(Fore.YELLOW + "Enter type of shape (circle, square, triangle): " + Fore.RESET)

if objType == "circle":
    radius = int(input("Enter the radius of the circle: "))
    area = 3.142 * radius * radius

    print("The area of the circle is: ", area)

elif objType == "square":
    width = int(input("Enter the width of the square: "))
    length = int(input("Enter the length of the square: "))
    area = width * length

    print("The area of the square is: ", area)

elif objType == "triangle":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = 0.5 * base * height

    print("The area of the triangle is: ", area)    
else:
    print("Invalid shape type/value entered.")