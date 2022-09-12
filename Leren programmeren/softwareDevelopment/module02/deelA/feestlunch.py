croissantjes = 17
l = 1.39

stokbroodjes = 2
a = 2.78

kortingen = 3
q = 3.43

croissant = (croissantjes*l)
stokbrood = (stokbroodjes*a)
korting = (kortingen*q)

print("De feestlunch kost je bij de bakker 18.88 euro voor de {} croissantjes en de {} stokbroden als de {} kortingsbonnen nog geldig zijn!".format (croissantjes, stokbroodjes, kortingen))
print("Je bent {} euro kwijt voor de croissantjes".format(croissantjes*l))
print("Ook ben je {} euro kwijt aan de stokbroodjes".format(stokbroodjes*a))
print("Maar je hebt 3 kortingsbonnen die bij elkaar {} euro waard zijn".format(kortingen*q))
print("Uiteindelijk moet je dan {} betalen voor alles!".format(croissant+stokbrood-korting))