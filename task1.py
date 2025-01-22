#first solving way
import re
txt = input()
pattern = r'ab*'
match = re.search(pattern, txt)
if match:
    print("yes")
else:
    print("no")