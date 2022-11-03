# Oefening 13
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
for i in range (9):
    robotArm.grab()
    for j in range (9,0,-1):
        robotArm.moveRight()
    robotArm.drop()
    for x in range (9,0,-1):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

# Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.