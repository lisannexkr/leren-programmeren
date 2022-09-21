import random

name = input('Hoe heet jij? ')
print("Hallo {}".format(name))

favoriteSeason = input('Wat is jouw favorite seizoen {}? A) Lente, B) Zomer, C) Herfst of D) Winter '.format(name)).lower()
answer = favoriteSeason

if answer == 'a':
    print("De lente is geweldig, lekkere temperatuur!")
if answer == 'b':
    print("De zomer is tegenwoordig veel te warm geworden.")
if answer == 'c':
    print("Blaadjes! De herfst bomen zijn prachtig.")
if answer == 'd':
    print("Ik hou van sneeuw.")
else:
    print("Dit seizoen bestaat niet")

favoriteColor = input('Wat is je favoriete kleur? ') 
trueOrFalse = str(random.randint(0,1))
if 0:
    print('Ik vind dat ook een mooie kleur!')
if 1:
    print("Ik hou niet zoveel van {}".format(favoriteColor))

num1 = random.randint(1,10)
num2 = random.randint(5,15)

try:
    number = input("En weet jij wat {}+{} is?".format(num1,num2))
    number = int(number)
    if number == num1+num2:
        print("Dat klopt!")
    else: 
        print("Nee dat klopt niet.")
except:
    print("Dat is geen nummer!")