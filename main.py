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
    num = 1.333
    pi = 3.142
    radius = float(input("Enter the radius of the circle: "))
    volume_of_a_cylinder = num * radius * radius* pi
    print(volume_of_a_cylinder)

def area_of_a_parrallelogram():
    num = 1.33
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))
    h = int(input("Enter the value for h: "))
    area_of_a_parrallelogram = num *(a + b)*h
    print(area_of_a_parrallelogram)

def perimeter_of_a_square():
    length = int(input("Enter a value for length: "))
    perimeter_of_a_square = 4 * length
    print("The answer is " , perimeter_of_a_square)
    

area_of_circle()
area_of_rectangle()
area_of_square()
volume_of_a_cylinder()
area_of_a_parrallelogram()
perimeter_of_a_square()