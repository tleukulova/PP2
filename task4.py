import re
pattern = r'^[A-Z]+[a-z]*.*'
txt = input()
x = re.findall(pattern, txt)
print(x)