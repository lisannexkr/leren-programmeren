# Oefening 10
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
rechts = 1
links = 2        

for i in range (4):
    robotArm.moveRight()
for x in range (5):
    robotArm.grab()
    for j in range(rechts):
        robotArm.moveRight()
    robotArm.drop()
    for m in range(links):
        robotArm.moveLeft()
    rechts = rechts + 2
    links = links + 2

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

# Draai de volgorde van de blokken om.
# Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait