def area_of_circle():
    pi = 3.14
    radius = float(input("Enter the radius of the circle: "))
    area = pi * radius * radius
    print(f"The area of the circle is: {area}" )

def area_of_square():
    lenght = float(input("Enter the side length of the square: "))
    area = lenght * lenght
    print(area)

def area_of_rectangle():
    lenght = float(input("Enter the lenght of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = lenght * width
    print(area)

area_of_circle()
area_of_rectangle()
area_of_square()