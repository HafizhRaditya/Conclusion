# I wanna make a code about my deatwish

print("It's Fiz")
if input("Do you know who it is? (fiz/rust):") .strip().lower() == "fiz":
    print("Just Let It Happen")
else:
    print("Death should be deliverance from pain")
age = 18
print("I am", age, "years old")

# If else condition. So I ask the user whether if they care about me
# if they say yes, the output will be saying "I am Jack's wasted life"
# if they say no, the output will be "I am Jack's wasted deathwish"

if input("Do you care about me? (yes/no): ").strip().lower() == "yes":
    print("I am Jack's wasted life")
else:
    print("I am Jack's wasted deathwish")

print("\n" + "="*50 + "\n")

# Interlinked section: user must type "within cells interlinked" three times (case/space tolerant)
if input("What it's like to hold someone that you love? (interlinked/cells): ").strip().lower() == "interlinked":
    print("Why don't you say that three times? Say: within cells interlinked")
    count = 0
    for i in range(3):
        response = input(f"Say it ({i+1}/3): ").strip().lower()
        if response == "within cells interlinked":
            count += 1
            print("You said it", count, "times")
        else:
            print("That wasn't correct")

    if count == 3:
        print("Well done")
    else:
        print("You're not even close to baseline")

else:
    print("Have you ever been truly alone?")
    if input("yes/no: ").strip().lower() == "yes":
        print("Hello friend...hello friend. You at least try, you at least understand, what it's like...to feel alone, you understand the pain")
    else:
        print("I think my mask of sanity is about to slip")
        print("YOU...FAILED ME")
        print("You were just trying to save me but its too late...cause I gotta wake up")

print("\n" + "="*50 + "\n")

if input("What do you do? (i drive / i want to fit in) : ").strip().lower() == "i drive":
    print("There's a hundred thousand streets in the city. You dont need to know the route, you give me a time and a place, I'll give you five minutes window")
    print("Anything that happens in that five minutes and Im yours, no matter what. Anything that happens a minute on the either side of that...and you're on your own")
else:
    print("There are no more barriers to cross. All I have in common with the uncontrollable and the insane, the vicious and the evil, all the mayhem I have caused and my utter indifference toward it, I have now surpassed")
    print("My mask of sanity is about to slip")

print("\n" + "="*50 + "\n")

if input("You look lonely....I can fix that (yes/no): ").strip().lower() == "yes":
    print("you look like a good Joe")
else:
    print("Wanted....loved. You're special")

print("\n" + "="*50 + "\n")

if input("Want to know a secret? (yes/no): ").strip().lower() == "yes":
    print("I think human consiousness is a tragic misstep in evolution")
else:
    print("What's the point of waking up?")

print("\n" + "="*50 + "\n")

if input("When you're not performing your duties do they keep you in a box? (cells/interlinked): ").strip().lower() == "cells":
    print("A bloodbath tall white fountain played")
    
else:
    print("What its like to hold a child? (cells/interlinked)")
    if input("cells/interlinked: ").strip().lower() == "interlinked":
        print("Within cells interlinked")
    else:
        print("A bloodbath tall white fountain played")

print("\n" + "="*50 + "\n")

if input("Do you wanna know about my dreams? (yes/no): ").strip().lower() == "yes":
    print("Feels like we're living in a fucking moon")
else:
    print("You ever fired your gun? Once...you dont wanna shot your gun")

print("\n" + "="*50 + "\n")

if input("Do you feel sorry? (yes/no): ").strip().lower() == "yes":
    print("You were just trying to save me but its too late...cause I gotta wake up")
else:
    print("You're not your fucking khakis...you are the all singing, all dancing crap of the world")

print("\n" + "="*50 + "\n")

if input("Want to hear my final words? (yes/no): ").strip().lower() == "yes":
    print("But even after admitting this....there is no catharsis.")
    print("My pain is constant and sharp ")
    print("This confession has meant nothing")
else:
    print("All those...moments...will be lost in time...like tears...in rain...")