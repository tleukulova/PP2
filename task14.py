#first solving way
def function(a,b):
    squares = (i**2 for i in range(a,b+1))
    for i in squares:
        print(i)

a = int(input())
b = int(input())
function(a,b)


#second solving way
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a = int(input())
b = int(input())
for j in squares(a,b):
    print(j)