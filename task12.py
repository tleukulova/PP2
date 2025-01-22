file1 = "/Users/aruzhantleukul/tsis6/file_for_12task1.py"
file2 = "/Users/aruzhantleukul/tsis6/file_for_12task2.py"
#/Users/aruzhantleukul/tsis6/file_for_12task1.py
with open (file1, 'r') as src:
    with open (file2, 'w') as copy:
        for i in src:
            copy.write(i)