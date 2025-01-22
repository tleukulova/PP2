import os
path = input("Enter path for your file: ")
#/Users/aruzhantleukul/tsis6/file_for_task13.py
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File successfully deleted!")
else:
    print("File not found!")