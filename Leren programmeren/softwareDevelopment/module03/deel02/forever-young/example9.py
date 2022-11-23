from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
loop = 4
for i in range (0,3):
    robotArm.moveRight()
for s in range (4):
    for j in range (loop):
        robotArm.grab()
        for x in range (0,5):
            robotArm.moveRight()
        robotArm.drop()
        for n in range (0,5):
            robotArm.moveLeft()  
    if loop > 1:
        robotArm.moveLeft()
    loop -= 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

#Verplaats alle stapels vijf stappen naar rechts.

#Je mag maximaal 12 regels code gebruiken inclusief de import, het laden van de robotarm en de wait