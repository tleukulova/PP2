string = input("Enter string: ")
count_lowercase = 0
count_uppercase = 0
for i in string:
    if i.islower():
        count_lowercase += 1
    elif i.isupper():
        count_uppercase += 1
print("The number of lower case letters in the string:", count_lowercase)
print("The number of upper case letters in the string:", count_uppercase)