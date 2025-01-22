import re
txt = input()
pattern = r'^a(bb|bbb)$'
match = re.match(pattern, txt)
if match:
    print("yes")
else:
    print("no")