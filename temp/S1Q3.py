from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2*math.pi*self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_perimeter(self):
        return 2*(self.length+self.breadth)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4*self.side


def main():
    choice = int(input())

    if choice == 1:
        radius = int(input())
        circle = Circle(radius)
        p = circle.calculate_perimeter()
        print(f"The perimeter is {p:.2f}")
    elif choice == 2:
        l = int(input())
        b = int(input())
        rectangle = Rectangle(l,b)
        p = rectangle.calculate_perimeter()
        print(f"The perimeter is {p:.2f}")
    elif choice == 3:
        side = int(input())
        obj = Square(side)
        p = obj.calculate_perimeter()
        print(f"The perimeter is {p:.2f}")
    else:
        print("Invalid Choice")
    


if __name__ == "__main__":
    main()