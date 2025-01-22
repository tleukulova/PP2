import re

def match_str(input_str):
    pattern = re.compile(r'a.*b$')
    if pattern.match(input_str):
        return True
    else:
        return False
    
txt = input()

if match_str(txt):
    print("Yes")
else:
    print("No")