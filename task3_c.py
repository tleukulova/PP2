
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
    
l_rectangle = float(input())
w_rectangle = float(input())
rectangle = Rectangle(l_rectangle, w_rectangle)
print(rectangle.area())

