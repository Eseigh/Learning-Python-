# Parent Class
class Shape:

    # Parent class constructor
    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass


# Child class of parent class Shape
class Rectangle(Shape):

    # constructor
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


# Child class of parent class Shape
class Circle(Shape):

    # constructor
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(3, 5), Circle(3)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))
