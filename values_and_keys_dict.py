thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
    print(x)
    

for y in thisdict.values():
    print(y)


#Loop through both keys and values, by using the items() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for z in thisdict.items():
    print(z)