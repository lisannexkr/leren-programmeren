# Instructies van het kaas spel.
print("Ik ga raden welke kaas jij in gedachten hebt!")
print("Dit ga ik doen door vragen te stellen over de eigenschappen van de kaas")
print("Je mag alleen maar antwoorden met Ja of Nee.")
print("veel plezier!")

# Scheiding instructies en spel
print ("- - - - - - - - - - - - - - - - ")

# Begin van het kaas spel.
geel = input("Is de kaas geel? ").lower()
if geel == 'ja':
    gaten = input("Heeft de kaas gaten? ").lower()
    if gaten == 'ja':
        duur = input("Is de kaas belachelijk duur? ").lower()
        if duur == 'ja':
            print("Je hebt een emmenthaler kaas!")
        else:
            print("Je hebt een Leerdammer kaas!")
    if gaten == 'nee':
        hard = input("Is de kaas hard als steen? ").lower()
        if hard == 'ja': 
            print("Je hebt Parmigiano Reggiano kaas!")
        else:
            print("Je hebt Goudse kaas!")
else: 
    schimmel = input("Heeft de kaas blauwe schimmel?").lower()
    if schimmel == 'ja':
            korst = input("Heeft de kaas een korst? ").lower()
            if korst == 'ja':
                print("Je hebt een Blue de Rochbaron!")
            else:
                print("Je hebt een Foume d'Ambert!")
    else:
        korst = input ("Heeft de kaas een korst? ").lower()
        if korst == 'ja':
            print("Je hebt een Camembert!")
        else:
            print("Je hebt een Mozarella")