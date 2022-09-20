# Inleiding sollicitatie
print("Solicitatie Circusdirecteur voor Circus HotelDeBotel")
print("Wat leuk dat je hier wilt komen werken!")
print("Ik moet je wel eerst wat vragen stellen voor je jouw cv kan insturen.")
print("De meeste vragen zullen beantwoord moeten worden met J/N")
print("Behalve sommige, die moeten worden beantwoord met een getal.")
print("Lees de vragen goed")
print("Veel succes!")
print("┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬")
print("┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴")

# De vragen
snor = 'N'
haar = 'H'

skills = input("Heb je meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek? ").upper()
MBO = input("Heb je een Diploma MBO-4 ondernemen? ").upper()
vrachtwagenbewijs = input("Heb je een geldig vrachtwagenbewijs? ").upper()
hogehoed = input("Ben je in bezit van een hoge hoed? ").upper()
man = input("Ben je een man? ").upper()
if man == 'J':
        snor = input("Heb je een snor breeder dan 10 cm? ").upper()
        if snor == 'J':
            lengte = input("Hoelang ben je in (volle) cm?")
            lengte = int(lengte)
            gewicht = input("Hoeveel weeg je in (volle) kg? ")
            gewicht = int(gewicht)
            certificaat = input("Heb je het certificaat “Overleven met gevaarlijk personeel”? ").upper()
            rodejas = input("Ben je in bezit van een extrinsieke rode jas? ").upper() 
            medemens = input("Ga je goed om met je medemens? ").upper()
            eten = input("Kan je goed eten koken? ").upper()
            duits = input("Kan je Duits spreken/verstaan? ").upper()
        if snor == 'N':
            pass
else:
    vrouw = input("Ben je een vrouw?").upper()
    if vrouw == 'J':
        haar = input("Heb je rood krulhaar langer dan 20 cm?").upper() 
        if haar == 'J':
            lengte = input("Hoelang ben je in (volle) cm?")
            lengte = int(lengte)
            gewicht = input("Hoeveel weeg je in (volle) kg? ")
            gewicht = int(gewicht)
            certificaat = input("Heb je het certificaat “Overleven met gevaarlijk personeel”? ").upper()
            rodejas = input("Ben je in bezit van een extrinsieke rode jas? ").upper() 
            medemens = input("Ga je goed om met je medemens? ").upper()
            eten = input("Kan je goed eten koken? ").upper()
            duits = input("Kan je Duits spreken/verstaan? ").upper()
    if vrouw == 'N':
        pass
print("┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬")
print("┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴")

# Het resultaat
failed = True
if skills == 'J':
    if MBO == 'J':
        if vrachtwagenbewijs == 'J':
            if hogehoed == 'J':
                if snor or haar == 'J':
                    if lengte>150:
                      if gewicht>90:
                           if certificaat == 'J':
                                print("Gefeliciteerd, Je bent geschikt voor de baan!")
                                print("Stuur je cv in waar je het moet sturen en we zullen snel een reactie sturen.")
                                failed = False
if failed == True:
    print("Helaas! Je hebt niet voldaan aan alle criteria")
    print("Je kan dus je cv niet insturen.")
    print("Als er ooit een andere vacature vrijkomt kan je het altijd opnieuw proberen!")