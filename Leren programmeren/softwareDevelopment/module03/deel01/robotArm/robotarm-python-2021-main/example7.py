# Oefening 7
from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for j in range (0,5):
    for i in range (0,6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    for i in range (0,2):
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
