def area_of_circle():
    pi = 3.14
    radius = float(input("Enter the radius of the circle: "))
    area = pi * radius * radius
    print(f"The area of the circle is: {area}" )

def area_of_square():
    length = float(input("Enter the side length of the square: "))
    area = length * length
    print(area)

def area_of_rectangle():
    length = float(input("Enter the lenght of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(area)

def volume_of_a_cylinder():
    num = 1.333(input("Enter the num of the num: "))
    pi = 3.142
    radius =float(input("Enter the radius of the circle: "))
    volume_of_a_cylinder = num * radius * radius* pi
    print(volume_of_a_cylinder)

def area_of_a_parrallelogram():
    num= 0.5 float(input("Enter the radius of the circle: "))
    a = 23
    b = 15 
    h= 10
    area_of_a_parrallelogram = num *(a + b)*h
    print(area_of_a_parrallelogram)

area_of_circle()
area_of_rectangle()
area_of_square()
volume_of_a_cylinder()
area_of_a_parrallelogram()