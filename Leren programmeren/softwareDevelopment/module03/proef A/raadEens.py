import random

# Variabele
x = 1
randomNum = 0
score = 0
aantalGeraden = 0

# Welkom bij het programma
print("Welkom bij dit programma waar je een random getal gaat raden (0 tot 1000)")
print("Het is vrij simpel, je mag 10 keer raden per ronde.")
print("Er komen 20 rondes, behalve als u ervoor kiest om er mee te stoppen.")
print("Aan het einde van alle gespeelde rondes krijgt u een eindscore.")
print("Veel succes! (plezier misschien ook wel)")

# Het programma zelf
while x <= 20:
    y = 0
    randomNum = random.randint(1, 1000)
    print("ronde", x)
    # Rondes    
    while y < 10:
        antwoord = int(input("voer een getal in tussen 1 en 1000: "))
        if antwoord == randomNum:
            y = 10
            score += 1
            print("U heeft het antwoord geraden!")
        elif antwoord - randomNum <= 20 and antwoord - randomNum > 0 or randomNum - antwoord <= 20 and randomNum - antwoord > 0:
            print("U bent heel warm")
        elif antwoord - randomNum <= 50 and antwoord - randomNum > 0 or randomNum - antwoord <= 50 and randomNum - antwoord > 0:
            print("U bent warm")
        elif antwoord > randomNum:
            print("U moet lager raden")
        else:
            print("U moet hoger raden")
        y += 1
        aantalGeraden += 1
    if x < 20:
        antwoord = input("Wilt u stoppen met spelen? ").lower()
        if antwoord == "ja":
            x = 20
    x += 1

# Afsluiting
print(f"U heeft {aantalGeraden} keer geraden")
if score >= 1:
    print(f"U heeft {score} keer goed geraden :)")
if score == 0:
    print(f"U heeft {score} keer goed geraden ):")