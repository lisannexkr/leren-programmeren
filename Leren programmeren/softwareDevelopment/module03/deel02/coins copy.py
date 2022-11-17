# name of student: Lisanne
# number of student: 99072683
# purpose of program: Wisselgeld uitrekenen
# function of program: Wisselgeld uitrekenen
# structure of program: While loops, for loops en variabele

vijfEuro = 0
tweeEuro = 0
eenEuro = 0
vijftigCent = 0
twintigCent = 0
tienCent = 0
vijfCent = 0
tweeCent = 0
eenCent = 0

toPay = int(float(input('Amount to pay: '))* 100) # Er word gevraagd hoeveel je moet betalen, Dit word omgezet naar een int of float en dit word x 100 gedaan.
paid = int(float(input('Paid amount: ')) * 100) # Er word gevraagd hoeveel je al betaald hebt, Dit word omgezet naar een int of float en dit word x 100 gedaan.
change = paid - toPay # Wisselgeld = Wat je nog moet betalen - wat je al betaald hebt

if change > 0: # Als change hoger is dan 0:
  coinValue = 500 # Is de coinValue 50
  
  while change > 0 and coinValue > 0: # Terwijl change hoger dan 0 is én coinvalue hoger dan 0 is
    nrCoins = change // coinValue # nrCoins is change gedeeld door coinvalue

    if nrCoins > 0: # Als nrCoins hoger dan 0 is:
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # dan print de code "return maximal "nrCoins" coins of "coinValue" cents!"
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # nrCoinsReturned is de vraag "hoeveel munten van 'coinValue' heb je teruggegeven?"
      change -= nrCoinsReturned * coinValue # change is nrCoinsReturned x coinValue
    
  
  # Print na de while loop ook een overzicht van alle teruggegeven muntstukken: per soort muntstuk hoeveel zijn er teruggeven.

# comment on code below: Het gaat elke keer de munt die lager is dan de vorige, behalve als coinValue 0 is
    if coinValue == 500:
      vijfEuro = nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      tweeEuro = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      eenEuro = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      vijftigCent = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      twintigCent = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      tienCent = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      vijfCent = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      tweeCent = nrCoinsReturned
      coinValue = 1
    elif coinValue == 1:
      eenCent = nrCoinsReturned
    else:
      coinValue = 0

if change > 0: # Als change over 0 is print de code "change not returned: 'change' cents"" anders print de code "done"
  print('Change not returned: ', str(change) + ' cents') 
else:
  print('done')

print("-----------------------------")
print("You returned {} 5 euro bills".format(vijfEuro))
print("You returned {} 2 euro coins".format(tweeEuro))
print("You returned {} 1 euro coins".format(eenEuro))
print("You returned {} 50 cent coins".format(vijftigCent))
print("You returned {} 20 cent coins".format(twintigCent))
print("You returned {} 10 cent coins".format(tienCent))
print("You returned {} 5 cent coins".format(vijfCent))
print("You returned {} 2 cent coins".format(tweeCent))
print("You returned {} 1 cent coins".format(eenCent))
print("-----------------------------")