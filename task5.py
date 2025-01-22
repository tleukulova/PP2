from itertools import permutations
def  per():
    s = input()
    return [''.join(perm) for perm in permutations(s)]
print(per())



