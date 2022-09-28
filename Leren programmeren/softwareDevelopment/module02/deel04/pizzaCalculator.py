# Lisanne van de Wege opdracht: Pizza calculator

# Een inleiding naar het bestel model
print("--------------------------------------------------------------------")
print("Welkom bij domino's online bestellen.")
print("We hebben drie maten pizza, Small, Medium en Large.")
print("Je kan bij elke maat zeggen hoeveel pizza's je wilt.")
print("Er zal bij elke maat bij staan hoe duur één pizza is.")
print("--------------------------------------------------------------------")

# Afmetingen pizza & hoeveel de klant er wilt
antwoord1 = input("Wil je een size small pizza voor €4 ").lower()
try:
    if antwoord1 == 'ja':
        antwoorda = input("Hoeveel wil je er? ")
        antwoorda = int(antwoorda)
except:
    print("Je moet een cijfer invullen. ")
    antwoorda = 0

antwoord2 = input("Wil je een size medium pizza voor €7? ").lower()
try:
    if antwoord2 =='ja':
        antwoordb = input("Hoeveel wil je er? ")
        antwoordb = int(antwoordb)
except:
    print("Je moet een cijfer invullen. ")
    antwoordb = 0

antwoord3 = input("Wil je een size large pizza voor €12?").lower()   
try:
    if antwoord3 == 'ja':
        antwoordc = input("Hoeveel wil je er? ")
        antwoordc = int(antwoordc)
except:
    print("Je moet een cijfer invullen!")
    antwoordc = 0
print("--------------------------------------------------------------------")

# Prijzen pizza maten
small = 4
medium = 7
large = 12

# Omschrijving aantal bestelde pizza's & prijs
print("Je hebt {} pizza's in size small gekozen, dit word in totaal €{}".format(antwoorda, antwoorda*small))
print("Je hebt {} pizza's in size medium gekozen, dit word in totaal {}".format(antwoordb, antwoordb*medium))
print("Je hebt {} pizza's in size large gekozen, dit word in totaal €{}".format(antwoordc, antwoordc*large))
print("Als je geen small/medium/large pizza's besteld heb dan komen er uiteraard geen extra kosten bij")
print("--------------------------------------------------------------------")

# Totaalprijs alle pizza's
smalltotaalprijs = 0
mediumtotaalprijs = 0
largetotaalprijs = 0

# Toon op het scherm de totaalprijs van alle pizza's.
smalltotaalprijs = antwoorda*small
mediumtotaalprijs = antwoordb*medium
largetotaalprijs = antwoordc*large
totaalprijs = smalltotaalprijs+mediumtotaalprijs+largetotaalprijs
totaalprijs = int(totaalprijs)

print("In totaal betaal je dan {} voor alle pizza's".format(totaalprijs))