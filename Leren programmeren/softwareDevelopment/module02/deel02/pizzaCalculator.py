# Lisanne van de Wege opdracht: Pizza calculator

# Een inleiding naar het bestel model
print("--------------------------------------------------------------------")
print("Welkom bij domino's online bestellen.")
print("We hebben drie maten pizza, Small, Medium en Large.")
print("Je kan bij elke maat zeggen hoeveel pizza's je wilt.")
print("Er zal bij elke maat bij staan hoe duur één pizza is.")
print("--------------------------------------------------------------------")

# Afmetingen pizza & hoeveel de klant er wilt
antwoord1=input("Wil je een pizza size small voor €4?").lower()
if antwoord1 == "ja":
    antwoord1=input('Hoeveel wil je er?')
    antwoord1=int(antwoord1)
else:
    print('Oke,')

antwoord2 = input("Wil je een medium pizza voor €7?").lower()
if antwoord2 == 'ja':
    antwoord2=input('Hoeveel wil je er?')
    antwoord2=int(antwoord2)
else:
    print("Oke,")

antwoord3 = input("Wil je een large pizza voor €12?").lower()
if antwoord3 == 'ja':
    antwoord3=input("Hoeveel wil je er?")
    antwoord3=int(antwoord3)
else:
    print("Oke")
print("--------------------------------------------------------------------")

# Prijzen pizza maten
small = 4
medium = 7
large = 12

# Omschrijving aantal bestelde pizza's & prijs
if antwoord1 != 'nee':
    print("Je hebt {} pizza's in size small gekozen, dit word in totaal €{}".format(antwoord1, antwoord1*small))
if antwoord2 != 'nee':
    print("Je hebt {} pizza's in size medium gekozen, dit word in totaal €{}".format(antwoord2, antwoord2*medium))
if antwoord3 != 'nee':
    print("Je hebt {} pizza's in size large gekozen, dit word in totaal €{}".format(antwoord3, antwoord3*large))
print("Als je geen small/medium/large pizza's besteld heb dan komen er uiteraard geen extra kosten bij")
print("--------------------------------------------------------------------")

# Totaalprijs alle pizza's
smalltotaalprijs = 0
mediumtotaalprijs = 0
largetotaalprijs = 0

# Toon op het scherm de totaalprijs van alle pizza's.
if antwoord1 != 'nee':
    smalltotaalprijs = (antwoord1*small)
    print("{} euro voor de size small pizza('s) ".format(smalltotaalprijs))
if antwoord2 != 'nee':
    mediumtotaalprijs = (antwoord2*medium)
    print("{} euro voor de size medium pizza('s) ".format(mediumtotaalprijs))
if antwoord3 != 'nee':
    largetotaalprijs = (antwoord3*large)
    print("{} euro betalen voor de size large pizza('s)".format(largetotaalprijs))
totaalprijs = (smalltotaalprijs+mediumtotaalprijs+largetotaalprijs)
print("Dat is in totaal {} dat je betaald voor al je pizza's!".format(totaalprijs))