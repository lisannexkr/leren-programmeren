a = input("Wat is A?") 
b = input("Wat is B?")
if b > a:
  print("A is het kleinste getal, {}".format(a))
elif a < b:
  print("")
else:
  print("A is even groot als B")

a = float(a)
b = float(b)

nums = [a, b]

min ( nums) 
max( nums )

print("Het minimum is {}".format(a))
print("Het maximum is {}".format(b))