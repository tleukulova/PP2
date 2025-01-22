import re
pattern = r'[a-z]+_[a-z]+'
txt = input()
x = re.findall(pattern, txt)
print(x)