import math
list = []
size = int(input())
for i in range(size):
    element = int(input())
    list.append(element)
product = math.prod(list)
print(product)