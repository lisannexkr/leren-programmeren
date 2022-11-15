from random import randint

play = True
ronde = 1
bomb = randint(1,10)
score = 0

while play == True:
    guess = input("Ronde {}: Op welk getal denkt u dat de bom niet ligt?" .format(ronde))
  
    if int(guess) == bomb:
        play = False
        print("BOEM! Game over!")
    else:
        score = score + (ronde*ronde)
        ronde = ronde + 1
        nextRound = input("Wilt u naar ronde "+str(ronde)+" (Y/N?)").lower
        
        if nextRound == 'n':
            play = False

if play == False:
    print("Je bent tot ronde {} gekomen! ".format(ronde))

print("Je score is {}".format(score))