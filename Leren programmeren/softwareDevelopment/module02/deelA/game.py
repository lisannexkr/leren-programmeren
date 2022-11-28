# Intro van de game
print("Welkom bij;")
print("Stuck In Greece")
lezen = input("Wil je de uitleg lezen van het spel? Ja/Nee ").lower()
if lezen == 'ja':
    print("Je zit vast in een verlaten berg dorp in Griekenland.")
    print("Je gaat in dit spel proberen te ontsnappen door midden van de keuzes die je maakt.")
else:
    pass

# Vraag of wil beginnen
beginnen = input("Wil je beginnen met het spel? Ja/Nee ").lower()
if beginnen == 'ja':
    print("Veel plezier!")
else:
    raise NameError("Je hebt nee ingevuld, en gaat dus niet door met het spel")

# Begin game
print("Je weet niet wat er gebeurd is..")
print("Je wordt opeens wakker in een oude stad in het midden van Griekenland.")
print("Wat ga je doen?")
print("A) Zoeken naar vervoer")
print("B) Zoeken naar eten")
print("C) Zoeken naar mensen")
watdoen = input("").upper()

# Optie A
if watdoen == 'A':
    print("Je gaat op zoek naar vervoer.")
    print("Je ziet A) een oud karretje, B) een oude step en C) een oude fiets") 
    print("Wat ga je gebruiken om te proberen te ontsnappen?")
    vervoer = input("").upper()
    # Optie A
    if vervoer == 'A':
        print("Je pakt het oude karretje")
        print("Wat ga je er nu mee doen?")
        print("A) Het weggetje uitrijden in de kar naar een ander deel van het landschap.")
        print("B) De berg afrollen met je kar.")
        karretje = input("").upper()
        if karretje == 'A':
            print("GAME OVER")
            print("Je gaat met je karretje de weg op.")
            print("Het blijkt goed te gaan.")
            print("Tot je opeens een kuil in de weg ziet en niet kunt stoppen.")
            print("Je wiel blijft steken in de kuil, en je vliegt van de berg af.")
        elif karretje == 'B':
            print("GAME OVER")
            print("Je pakt het karretje en gaat van de berg af")
            print("Het blijkt goed te gaan, totdat je een grote groep struiken met doorns ziet")
            print("Je probeert te remmen maar het karretje heeft geen remmen")
            print("Je land met je gezicht vol in de doorns")
    # Optie B
    elif vervoer == 'B':
        print("Je pakt de oude step")
        print("Wat ga je er mee doen?")
        print("A) Een weggetje dat naar een ander dorpje leid")
        print("B) Van de berg af steppen")
        step = input("").upper()
        if step == 'A':
            print("GAME OVER!")
            print("Je kiest ervoor om op en weggetje dat naar een ander dorpje leid te fietsen")
            print("Helaas was je te langzaam met steppen en kwam er een grote steen de berg af rollen")
            print("Deze steen word gevolgd door een waterstroom")
        elif step == 'B':
            print("GAME OVER!")
            print("Je stept met veel moed van de berg af")
            print("De step gaat heel hard vooruit")
            print("Maar als je uiteindelijk wilt remmen vlieg je over de kop")
            print("En land je keihard op de grond.")
    # Optie C
    elif vervoer == 'C':
        print("Je pakt de oude fiets")
        print("Wat ga je er mee doen?")
        print("A) Een pad de berg op op fietsen")
        print("B) Een pad de berg af af fietsen")
        fiets = input("").upper()
        if fiets == 'A':
            print("Je fiets haastig de berg op op de oude roestbak")
            print("Er komt een hobbel in de weg")
            print("Je fiets erover heen en land netjes op de weg")
            print("Eindelijk, vrij uit het dorp!")
        elif fiets == 'B':
            print("GAME OVER!")
            print("Je rolt van de berg af")
            print("Je gaat te snel van de berg af")
            print("Je valt van je fiets an en rolt van de berg af tot je dood")

# Optie B
elif watdoen == 'B':
    print("Je gaat op zoek naar eten.")
    print("Je ziet meerdere fruit soorten.")
    print("Wat ga je eten om te overleven?")
    print("A) Olijven")
    print("B) Bessen")
    print("C) Appels")
    eten = input("").upper()
    # Optie A
    if eten == 'A':
        print("Je kiest voor de olijven.")
        print("Ze zien er erg verleidelijk uit..")
        print("Ga je ze eten?")
        print("A) Ja")
        print("B) Nee")
        olijven = input("").upper()
        if olijven == 'A':
            print("GAME OVER!")
            print("De olijven zijn erg lekker")
            print("Je blijft ze maar eten, je kan er niet vanaf blijven")
            print("Opeens begin je over te geven, je bent vergiftigd.")
        elif olijven == 'B':
            print("GAME OVER!")
            print("Je kiest ervoor de olijven niet te eten en door te lopen.")
            print("'Oh, dat komt wel goed, ik vind wel ander eten' denk je")
            print("Maar, je komt geen eten meer tegen en verhongert")
    # Optie B
    elif eten == 'B':
        print("Je kiest voor de Bessen.")
        print("Ze zien er erg verleidelijk uit..")
        print("Ga je ze eten?")
        print("A) Ja")
        print("B) Nee")
        bessen = input("").upper()
        # Optie A
        if bessen == 'A':
            # Hoeveelheid bessen
            hoeveelbessen = input("Hoeveel bessen eet je? ")
            hoeveelbessen = float(hoeveelbessen)
            if hoeveelbessen > 1:
                print("GAME OVER!")
                print("De bessen zijn erg lekker")
                print("Je blijft ze maar eten, je kan er niet vanaf blijven")
                print("Opeens begin je over te geven, je bent vergiftigd.")
            elif hoeveelbessen == 1:
                print("GAME OVER!")
                print("De bessen zijn erg lekker")
                print("Je eet er een")
                print("Je denkt dat je veilig bent maar, een uur later begin je te kotsen")
                print("Je bent vegiftigd.")
            elif hoeveelbessen < 1:
                print("GAME OVER!")
                print("Je kiest er toch voor de bessen niet te eten en door te lopen.")
                print("'Oh, dat komt wel goed, ik vind wel ander eten' denk je")
                print("Maar, je komt geen eten meer tegen en verhongert")
        # Optie B
        elif bessen == 'B':
            print("GAME OVER!")
            print("Je kiest ervoor de bessen niet te eten en door te lopen.")
            print("'Oh, dat komt wel goed, ik vind wel ander eten' denk je")
            print("Maar, je komt geen eten meer tegen en verhongert")
    # Optie C
    elif eten == 'C':
        print("Je kijkt naar de appelboom")
        print("Je ziet twee soorten appels hangen")
        print("A) Rode appels")
        print("B) Groene appels")
        print("Welke kleur appel kies je?")
        # Welke kleur appel
        appel = input("").upper()
        if appel == 'A':
            print("Je pakt de rode appel en inspecteert het")
            print("Het ziet er goed uit en je hebt best honger")
            print("Wat ga je er mee doen?")
            print("A) Eten")
            print("B) Niet eten")
            appeletenrood = input("").upper()
            if appeletenrood == 'A':
                print("GAME OVER!")
                print("De rode appel was giftig")
                print("Je valt gelijk dood neer")
            elif appeletenrood == 'B':
                print("GAME OVER!")
                print("Je verhongert")
                print("En je gaat dood")
        elif appel == 'B':
            print("Je pakt de groene appel en inspecteert het")
            print("Het ziet er goed uit en je hebt best honger")
            print("Wat ga je er mee doen?")
            print("A) Eten")
            print("B) Niet eten")
            appeletengroen = input("").upper()
            if appeletengroen == 'A':
                print("De groene appel was lekker")
                print("Je eet het helemaal op")
                print("Je krijgt geen bijwerkingen")
                print("Je pakt er meer voor een langere overlevingstijd en onstnapt")
            elif appeletengroen == 'B':
                print("GAME OVER!")
                print("Je verhongert")
                print("En je gaat dood")

# Optie C
elif watdoen == 'C':
    print("Je gaat mensen zoeken")
    print("Je ziet een groepje mensen en één persoon")
    print("Je zit te twijfelen wat je moet doen")
    print("A) In je eentje blijven")
    print("B) Een groepje mensen proberen te joinen")
    print("C) Met de persoon die alleen staat meelopen")
    mensen = input("").upper()
    if mensen == 'A':
        print("Je kiest ervoor in je eentje te gaan.")
        print("Maar wat is dat? Het is de groep mensen!")
        print("Ze komen erg dreigend naar je toe.")
        print("Wat ga je doen?")
        print("A) Weg rennen van de groep")
        print("B) Weg lopen van de groep")
        print("C) Proberen vrienden te worden met de groep")
        dreigendegroep = input("").upper()
        if dreigendegroep == 'A':
            print("Je rent weg van de groep zo hard als je kan")
            print("Je hoort de groep achter je aan rennen en word bang")
            print("Je komt opeens politie tegen, en ze helpen je met onstnappen")
        elif dreigendegroep == 'B' or 'C':
            print("GAME OVER!")
            print("Je koos voor {}".format(dreigendegroep))
            print("Helaas werkt dit niet en ga je dood")
    if mensen == 'B':
        print("Je gaat met een groepje mee")
        print("Ze vragen of je mee gaat om eten te vinden")
        print("Ga je mee?")
        print("A) Ja")
        print("B) Nee")
        etenvinden = input("").upper()
        if etenvinden == 'A':
            print("GAME OVER!")
            print("Je vind eten, het is genoeg voor iedereen!")
            print("Helaas zijn het bessen en je overlijdt")
        elif etenvinden == 'B':
            print("GAME OVER!")
            print("De groep word boos op je en valt je aan")
            print("Je probeerd weg te rennen maar het lukt niet")
    if mensen == 'C':
        print("GAME OVER!")
        print("Ga nooit mee met één persoon")
        print("Je word als lokaas gebruikt voor gevaarlijke groepen mensen")

# Einde game
print("")
print("Bedankt voor het spelen van mijn game!")
print("Ik hoop dat je genoten hebt")
print("Als je verloren hebt kan je het zeker nog een keer proberen, het is mogelijk om te winnen!")