dagen = True
dag = input("Tot welke dag van de week wil je weten? ").lower()
while dagen == True:
    if dag == 'maandag':
        print("Maandag")
        dagen = False
    elif dag == 'dinsdag':
        print("Maandag, Dinsdag")
        dagen = False
    elif dag == 'woensdag':
        print("Maandag, Dinsdag, Woensdag")
        dagen = False
    elif dag == 'donderdag':
        print("Maandag, Dinsdag, Woensdag, Donderdag")
        dagen = False
    elif dag == 'vrijdag':
        print("Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag")
        dagen = False
    elif dag == 'zaterdag':
        print("Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag")
        dagen = False
    elif dag == 'zondag':
        print("Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag")
        dagen = False
    else:
        print("Je moet Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag of Zondag invullen")
        dagen = False