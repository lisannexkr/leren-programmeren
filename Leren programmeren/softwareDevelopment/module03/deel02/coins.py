# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

if change > 0: # Als change hoger dan 0
  coinValue = 50 #
  
  while change > 0 and coinValue > 0: # Als change over 0 en de coinValue over 0 zijn.
    nrCoins = change // coinValue # Change gedeeld door coinValue.

    if nrCoins > 0: # Als het aantal coins hoger dan 0 is 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print(coinValue)


'''coins.py is een programma dat helpt wisselgeld terug te geven met de juiste hoeveelheid munten van bepaalde soort.

Kopieer het programma naar de map nogmaals.
Breid het uit naar het gebruik van 1, 2 en 5-euro muntstukken.
Print na de while loop ook een overzicht van alle teruggegeven muntstukken: per soort muntstuk hoeveel zijn er teruggeven.
Meldt met een print als niet al het vereiste wisselgeld is teruggegeven met munten.
Voorzie het programma van comments achter alle aangegeven hashes # De comments tonen aan dat je de werking van het programma helemaal hebt begrepen.
 

Doe een commit in de repo.
Lever de aangepaste coins.py verpakt in coins.zip in!'''