a = input("Wat is A?") 
b = input("Wat is B?")
if b > a:
  print("A is het kleinste getal, {}".format(a))
  min = a
elif a < b:
  print("")
else:
  print("A is even groot als B")
