class Shape:
    def __init__(self): print(" ")

    def area(self):
        print("Area of shape")

    def peri(self):
        print("Perimeter of shape")


class Circle(Shape):
    def __init__(self, r):
        Shape.__init__(self)
        self.area = 3.142 * r * r
        self.perimeter =3.142 * 2 * r
        # print("Circle Constructor")

    # def area(self):
    #     print(f"Area of circle is:{3.142 * self.radius * self.radius}")
    #     pass
    #     # return 3.142 * self.radius * self.radius


while True:
    print('Enter a number')

    print('1. Square\t2. Rectangle\n3. Circle\t4. Rhombus\n5.Cylinder\t6. Polygon\n7. Exit')

    choice = int(input('Enter your choice:'))


    def switch(choice):
        def square():
            length = float(input('Length of square: '))
            area = length ** 2
            perimeter = 4 * length

            print(f'Area is {area} and Perimeter is {perimeter}')

        def rectangle():
            length = float(input('Length of Rectangle: '))
            breadth = float(input('breadth of Rectangle: '))

            area = length * breadth
            perimeter = 2 * (length + breadth)

            print(f'Area is {area} and Perimeter is {perimeter}')

        def circle():
            radius = float(input('Radius of circle:'))
            ro = Circle(radius)
            area = ro.area
            perimeter = ro
            print(f'The radius of the circle is {area}')
            # ro.area()

        def Exit():
            quit()

        if choice == 1:
            return switch(square())
        elif choice == 2:
            return switch(rectangle())
        elif choice == 3:
            return switch(circle())
        elif choice == 4:
            return Rhombus()
        elif choice == 5:
            return cylinder()
        elif choice == 6:
            return polygon()
        elif choice == 7:
            print('Closing...')
            return switch(Exit())
        else:
            print('Invalid Argument')


    switch(choice)


class Area():
    def getArea(self, l, b):
        return l * b


class Perimeter():
    def getPerimeter(self, l, b):
        return 2 * (l + b)


class Rectangle(Area, Perimeter):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return super().getArea(self.length, self.breadth)

    def perimeter(self):
        return super().getPerimeter(self.length, self.breadth)


rect = Rectangle(7, 4)

print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


class Shape:
    def __init__(self): print("Shape Constructor")

    def area(self): print("Area of shape")

    def peri(self): print("Perimeter of shape")


# class Circle(Shape):
#     def __init__(self, r):
#         Shape.__init__(self)
#         self.radius = r
#         print("Circle Constructor")
#
#     def area(self):
#         # print(f"Area of circle is:{3.142 * self.radius * self.radius}")
#         return 3.142 * self.radius * self.radius


class Rhombus(Shape):
    def __init__(self, h, b):
        Shape.__init__(self)
        self.height = h
        self.base = b
        print("Rhombus Constructor")

    def area(self):
        print("Area of Rhombus is:", self.height * self.base)


class Cylinder(Shape):
    def __init__(self, r):
        Shape.__init__(self)
        self.radius = r
        print("Cylinder Constructor")

    def area(self):
        print("Area of cylinder is:", 3.142 * self.radius * self.radius)


c = Circle(5)
c.area()  # Circle class area method overrides Shape class area method
