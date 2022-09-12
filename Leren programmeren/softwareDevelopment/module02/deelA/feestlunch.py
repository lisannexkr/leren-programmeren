k = 17
l = 1.39

o = 2
a = 2.78

x = 3
q = 3.43

croissant = (k*l)
stokbrood = (o*a)
korting = (x*q)

print("De feestlunch kost je bij de bakker 18.88 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")
print("Je bent {} euro kwijt voor de croissantjes".format(k*l))
print("Ook ben je {} euro kwijt aan de stokbroodjes".format(o*a))
print("Maar je hebt 3 kortingsbonnen die bij elkaar {} euro waard zijn".format(x*q))
print("Uiteindelijk moet je dan {} betalen voor alles!".format(croissant+stokbrood-korting))