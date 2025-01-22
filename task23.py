import math
sides = int(input())
length = int(input())
area = (1/4) * sides * length**2 / math.tan(math.pi / sides)
print (round(area, 0))