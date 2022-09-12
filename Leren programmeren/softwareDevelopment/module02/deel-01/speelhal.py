personen = 4
toegangsticket = 7.45
vipvr = 0.37
minuten = 45
minuten2 = 5
ticketsheledag = 29.8
ticketsvipvr = 14.60

print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro")
print("Voor tickets voor de hele dag betaal je {} met 4 mensen".format(personen*toegangsticket))
print("En als je de VIP-VR Game-seat wilt doen dan is het {} ".format(minuten/minuten2*vipvr*personen))
print("Dus dan ben je {} kwijt voor de hele dag".format(ticketsheledag+ticketsvipvr))