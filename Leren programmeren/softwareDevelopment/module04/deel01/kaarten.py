import random

kaarten = ["2","3","4","5","6","7","8","9","10","boer", "vrouw", "heer", "aas"]
kaartkleur = ["harten", "klaveren", "schoppen", "ruiten"]
jokers = 2
deck = []

for i in range (len(kaartkleur)):
    for j in range (len(kaarten)):
        deck.append(f"{kaartkleur[i]} {kaarten[j]}")

kaartnummer = 1
for i in range (7):
    random.shuffle(deck)
    print(f"Kaart {kaartnummer}; {deck.pop(0)}")
    kaartnummer = kaartnummer + 1
print("")
print(f"deck (47 kaarten): {deck}")