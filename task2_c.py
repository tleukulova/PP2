class Shape:
    def __init__(self, length):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

a = int(input())
shape = Shape(a)
print("Area of Shape:", shape.area())  
b = int(input())
square = Square(b)
print("Area of Square:", square.area()) 

