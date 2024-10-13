import math


class Shape :

    def __init__(self, name):
       self.name = name

    def area(self):
        return None

class Rectangle(Shape) :

    def __init__(self, width, height, name):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape) :

   def __init__(self, radius, name):
       super().__init__(name)
       self.radius = radius

   def area(self):
       return pow(self.radius,2) * math.pi

def print_area(shape):
    print(f"name: {shape.name}, area: {shape.area()}")

print_area(Rectangle(5,5,'a'))
print_area(Circle(5,'b'))

