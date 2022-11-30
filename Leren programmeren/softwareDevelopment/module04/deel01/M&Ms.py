import random	

MenMkleuren = ("oranje", "groen", "blauw", "bruin")
zakMenMs = []
hoeveelMenMs = int(input("Hoeveel M&M's moeten er toegevoegd worden? "))

for i in range (hoeveelMenMs):
     keuze = random.choice(MenMkleuren)
     zakMenMs.append(keuze)

print(zakMenMs)

