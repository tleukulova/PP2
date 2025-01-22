def decreasing(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in decreasing(n):
    print (i)
