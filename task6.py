import re
pattern = r'[ , .]'
txt = input()
x = re.sub(pattern, ":", txt)
print(x)
