import random

MenMkleur = ["rood", "blauw", "groen", "geel", "bruin"]
hoeveel = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))

zakMenMs = {
    'rood' : 0,
    'blauw' : 0,
    'groen' : 0,
    'geel' : 0,
    'bruin' : 0
}

for i in range (hoeveel):
    kleur = random.choice(MenMkleur)
    zakMenMs[kleur] += 1

print(zakMenMs)