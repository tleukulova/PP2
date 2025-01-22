import os
path = input("Enter path: ")
#/Users/aruzhantleukul/tsis6 as example

if os.path.exists(path):
    print(path)
    print("Filename of the given path: ", os.path.basename(path))
    print("Directory portion of the given path: ", os.path.dirname(path))
else:
    print("The path do not exist")