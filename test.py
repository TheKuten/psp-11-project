

name = input("Enter your name: ")

objType = input("Enter type of shape (circle, square, triangle): ")

if objType == "circle":
    radius = int(input("Enter the radius of the circle: "))
    area = 3.142 * radius * radius

    print("The area of the circle is: ", area)
