# Oefening 13
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
rechts = 9
links = 9
robotarm = True

while robotarm == True:
    robotArm.grab()
    if robotArm.scan() == '':
        robotarm = False
    else:
        for j in range (rechts):
            robotArm.moveRight()
        robotArm.drop()
        for x in range (links):
            robotArm.moveLeft()
        rechts = rechts - 1
        links = links - 1
        
# variabele
# while loop
# scannen aan het einde
# if robotArm.scan() == '':
#   variabele = False

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

# Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.