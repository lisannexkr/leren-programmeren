# Oefening 10
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
for i in range (0,5):
    robotArm.grab()
    for j in range (9, 0, -2):
        robotArm.moveRight()
    robotArm.drop()
    for x in range (8, 0, -2):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

# Draai de volgorde van de blokken om.
# Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait