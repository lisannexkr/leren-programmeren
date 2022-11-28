## Variables
introvert = 0
extrovert = 0
earlybird = 0
nightowl = 0

# First question
print("Question 1")
print("Do you like being alone?")
print("Yes, no or maybe")
Q1 = input("").lower()
if Q1 == 'yes':
    introvert = introvert + 50
    nightowl = nightowl + 25
if Q1 == 'no':
    extrovert = extrovert + 50
if Q1 == 'maybe':
    earlybird = earlybird + 25
    nightowl = nightowl + 25
else:
    print("You have to anser with yes, no or maybe.")

print("Question 2")
print("How often do you make excuses to not go out?")
print("Almost always, Never, Only if theyre late in the afternoon or only if theyre early in the morning")
Q2 = input("").lower()
if Q2 == 'almost always':
    introvert = introvert + 50




if introvert > 100:
    introvert = 100
if introvert < 100:
    pass

print(introvert,extrovert,earlybird,nightowl)


