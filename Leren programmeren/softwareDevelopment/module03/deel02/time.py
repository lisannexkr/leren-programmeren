AM = True
while AM == True:
    for i in range(0,13):
        print("{} AM".format(i))
    if i == 12:
        AM = False

PM = True
while PM == True:
    for j in range(0,13):
        print("{} PM".format(j))
    if j == 12:
        PM = False