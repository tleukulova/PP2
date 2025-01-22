def solve(numheads, numlegs):
    #number of legs of a chicken
    a = 2
    #number of legs of a rabbit
    b = 4
    #let's create a mathematical system of equations to solve
    """
    chicken - y; rabbit - x
    x + y = 35
    4x + 2y = 94
    """
    y = numheads - (((b * numheads) - numlegs) / (b - a))
    x = numheads - y
    return int(x), int(y)
numheads = 35
numlegs = 94
rabbit, chicken = solve(numheads, numlegs)
print ("rabbit:" , rabbit)
print ("chicken:" , chicken)