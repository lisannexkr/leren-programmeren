k = 17
l = 0.39

o = 2
a = 2.78

x = 3
q = 0.50

croissant = (k*l)
stokbrood = (o*a)
korting = (x*q)

print('Dit is hoeveel jij kwijt gaat zijn voor jouw feestlunch')
print("Je bent {} euro kwijt voor de croissantjes".format(k*l))
print("Ook ben je {} euro kwijt aan de stokbroodjes".format(o*a))
print("Maar je hebt 3 kortingsbonnen die bij elkaar {} euro waard zijn".format(x*q))
print("Uiteindelijk moet je dan {} betalen voor alles!".format(croissant+stokbrood-korting))