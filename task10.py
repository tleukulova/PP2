import os
path = input("Enter path: ")
#/Users/aruzhantleukul/tsis6/file_for_10task.py as example
my_list = ["Divergent", "The Matrix", "The Hunger games"]
with open(path, 'w') as file:
    for element in my_list:
        file.write(str(element) + '\n')
        
print("List has been written to the file successfully.")
    
