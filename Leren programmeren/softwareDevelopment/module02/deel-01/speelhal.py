personen = 4
toegangsticket = 7.45
vipvr = 0.37
minuten = 45
minuten2 = 5
ticketsheledag = 29.8
ticketsvipvr = 13.32

print("de rekening van de speelhal is")
print("Voor tickets voor de hele dag betaal je {} met 4 mensen".format(personen*toegangsticket))
print("En als je de VIP-VR Game-seat wilt doen dan is het {} ".format(minuten/minuten2*vipvr*personen))
print("Dus dan ben je {} kwijt voor de hele dag".format(ticketsheledag+ticketsvipvr))