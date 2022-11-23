from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for i in range (0,5):
    robotArm.moveRight()
    for j in range (0,6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verplaats iedere stapel één plek naar links.

#Je mag maximaal 11 regels code gebruiken inclusief de import, het laden van de robotarm en de wait