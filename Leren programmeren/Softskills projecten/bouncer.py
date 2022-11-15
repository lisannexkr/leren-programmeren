leeftijd = input("Wat is jouw leeftijd? ")
leeftijd = int(leeftijd)
if leeftijd >17:
    print("Je mag naar binnen!")
    naam = input("Wat is jouw naam? ").lower()
    bandje = False
    if naam == 'rudi':
        if naam =='arnold':
            if naam == 'jeroen':
                if naam == 'kjeld':
                    if leeftijd <21:
                        sticker = True
                        print('Je krijgt een sticker!')
                        drinken = input("Wat wil je drinken? A) Bier B) Cola ").upper()
                        if drinken == 'A':
                             print("Je bent te jong, je mag geen alcohol.")
                        if drinken == 'B':
                            print("Je cola is 1,00")
                            print("Geniet ervan!")
                    else:
                        sticker = False
    else:            
        if leeftijd>20:
            bandje = True 
            print("Alsjeblieft, een bandje zodat je alcohol kan kopen.")
            drinken = input("Wat wil je drinken? A) Bier B) Cola ").upper()
            if drinken == 'A':
                print("Bier is 1,50.")
                print("Geniet ervan!")
            if drinken == 'B':
                print("Cola is 1,50.")
                print("Geniet ervan!")
        else:
            print("Je krijgt geen bandje/mag geen alcohol bestellen in deze club. ")
            drinken = input("Wat wil je drinken? A) Bier B) Cola").upper()
            if drinken == 'A':
                print("Je bent te jong, je mag geen alcohol.")
            if drinken == 'B':
                print("Je cola is 1,00")
                print("Geniet ervan!")
else:
    print("Sorry, je mag niet naar binnen.")
    