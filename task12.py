n = int(input())
generator_expression = (i for i in range(1,n+1) if i%2 == 0)
for i in generator_expression:
    print(i)