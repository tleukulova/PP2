import os
path = input("Enter path: ")
#/Users/aruzhantleukul/tsis6/task6.py as example

with open (path, 'r') as file:
    count_lines = len(file.readlines())
    print("The number of lines in the given file is: ", count_lines)
