# Oefening 4
from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for i in range(0,5):
    robotArm.grab()
    for i in range(0,2):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(0,2):
        robotArm.moveLeft()
robotArm.moveRight()
robotArm.moveRight()
for i in range(0,5):
    robotArm.grab()
    for i in range(0,1):
        robotArm.moveLeft()
    robotArm.drop()
    for i in range(0,1):
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

# Verplaats de hele stapel blokken één plek naar rechts. Zorg ervoor dat de volgorde van de blokken gelijk blijft.