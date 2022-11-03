# Oefening 12
from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
x = 9
y = 8

for i in range (9):
    robotArm.grab()
    colour = robotArm.scan()
    if colour == 'red':
        for i in range (x):
            robotArm.moveRight()
        robotArm.drop()
        for i in range (y):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    x = x - 1
    y = y - 1 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

# Verplaats alle rode blokken naar het einde.
# Let op, de blokken zijn iedere keer anders als je het programma start!