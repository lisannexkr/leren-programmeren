croissantjes = input("Hoeveel croissantjes heb je nodig?")
croissantjes = int(croissantjes)
kostcroissantjes = input("Hoeveel kost één croissantje?")
kostcroissantjes = float(kostcroissantjes)
stokbroodjes = input("Hoeveel stokbroodjes heb je nodig?")
stokbroodjes = int(stokbroodjes)
koststokbroodjes = input("Hoeveel kost een stokbroodje?")
koststokbroodjes = float(koststokbroodjes)
korting = input("Hoeveel kortingsbonnen heb je?")
korting = int(korting)
hoeveelheidkorting = input("Hoeveel is je kortingsbon waard?")
hoeveelheidkorting = float(hoeveelheidkorting)

print(" ---------------------------------------------------------------------")
print("| Voor de croissantjes ben je {} kwijt".format(croissantjes*kostcroissantjes))
print("| Daarbovenop ben je ook nog {} extra kwijt aan de stokbroodjes".format(stokbroodjes*koststokbroodjes))
print("| Maar gelukkig heb je {} aan kortingsbonnen".format(korting*hoeveelheidkorting))
print("| In totaal hoef je dus maar {} te betalen!".format(croissantjes*kostcroissantjes+stokbroodjes*koststokbroodjes-korting*hoeveelheidkorting))
print(" ---------------------------------------------------------------------")