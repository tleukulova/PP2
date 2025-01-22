import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#a method show to display the coordinates of the point
    def show(self):
        print({self.x}, {self.y})

#a method move to change these coordinates
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

#a method dist that computes the distance between 2 points
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

x_point1=float(input())
y_point1=float(input())
x_point2=float(input())
y_point2=float(input())
point1=Point(x_point1,y_point1)
point2=Point(x_point2,y_point2)
point1.show()
x_point3=float(input())
y_point3=float(input())
point1.move(x_point3,y_point3)
print(point1.dist(point2))

