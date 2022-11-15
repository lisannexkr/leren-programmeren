gastheer = True
gasten = 5
drank = False
chips = True
gastheer = input("Hoe heet de gastheer? ").lower()

# Feest kan alleen beginnen met gastheer OF gasten chips en drank
#if gastheer or gasten and chips and drank == True:
# Feest met chips maar zonder drank kan NIET beginnen 
#if drank == True:
# Feest met gasten kan NIET beginnen geen drank en chips
#if drank and chips == True:
# Gastheer kan feest geven zonder chips en gasten ALS er drank is
#if gastheer and drank == True:
# Feest moet gasten OF gastheer hebben
#if gastheer or gasten == True:
# Alleen chips is geen feest

gasten0k = ((gasten >= 5 and gasten <= 12)) 
if drank and ((gasten>5 and gasten<12) or (gastheer and gastheer != "rudi")): 
    print("Start The Party!")
else: 
    print("No party!")