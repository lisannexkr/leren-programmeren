deTuple = ("appelmoes","aardappel","appelsaus","appel","appelkaas")
for i in range(len(deTuple)):
    print(deTuple[i])

deList = ("appelmoes","aardappel","appelsaus","appel","appelkaas")
for i in range(len(deList)):
    print(deList[i])

deDictionary = {
  "Ford": "Mustang",
  "Audi": "RS6",
  "BMW": "volkwagen",
  "hotel?": "trivago"
}

for i in deDictionary.keys():
    print(i)

for x, y in deDictionary.items():
  print(x, y)


print (dir(deDictionary))

# CTRL + R = alles verplaatsen