# Oefening 8
from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for j in range (0,5):
    for i in range (0,6):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    for i in range (0,2):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

#Verplaats de stapel naar de rechterkant.
#Je mag maximaal 11 regels code gebruiken inclusief de import, het laden van de robotarm en de wait