import random

kaarten = [2,3,4,5,6,7,8,9,10,"boer", "vrouw", "heer", "aas"]
kaartkleur = ["harten", "klaveren", "schoppen", "ruiten", "joker", "joker"]

y = 1
while y <= 7:
    if (random.choice(kaartkleur)) == 'joker':
        print(f"Kaart {y}: joker")
        y = y + 1
    else:
        print(f"Kaart {y}: {random.choice(kaartkleur)} {random.choice(kaarten)}")
        y = y + 1