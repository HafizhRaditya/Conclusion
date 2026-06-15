from playsound3 import playsound

import sys
import time

def typewriter_effect(text, delay = 0.15):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    typewriter_effect("Ahh...this is a story about two girls in Oregon")
    typewriter_effect("The one girl who can rewind times...")
    typewriter_effect("The other one who wanted to go to Los Angeles...")
    typewriter_effect("But it didnt work out because...")
    typewriter_effect("That girl is a sex and love maniac")
    typewriter_effect("Oh and the other one is a blue haired punk girl")
    typewriter_effect("Wait...thats not two girls...that is three")
    typewriter_effect("Yeah well what can I say....")
    typewriter_effect("Anyway.....")
    typewriter_effect("These girls...are a broken ass kids")
    typewriter_effect("Or should I say not broken but rather...")
    typewriter_effect("........")
    typewriter_effect("Well...yeah broken")
    typewriter_effect("Alright here's the thing")
    typewriter_effect("The girl who can rewinds time")
    typewriter_effect("Left the girl with the blue haired girl somewhere in Oregon")
    typewriter_effect("The blue haired girl was addicted into some kind of things")
    typewriter_effect("Drugs, Smoke, Sex, you name it")
    typewriter_effect("Turns out...the blue has or should I say had a friend")
    typewriter_effect("The ones who wanted to go to Los Angeles")
    typewriter_effect("Guess what? They fell in love")
    typewriter_effect("I dont know....doesnt sound magical to me")
    typewriter_effect("Sounds like a....")
    typewriter_effect("Anyway forget what I said")
    typewriter_effect("So the 'Los Angeles' girl was cheated on blue haired girl")
    typewriter_effect("Guess what?")
    typewriter_effect("She cheated with a drug dealer and a fucking art teacher from local school")
    typewriter_effect("Geez...poor girl")
    typewriter_effect("What a waste of life...")
    typewriter_effect("She was killed by the teacher cause the teacher is a sick psycho")
    typewriter_effect("The blue haired girl thought that her 'friend' just gone missing")
    typewriter_effect("They never speak afterwards")
    typewriter_effect("Now the girl who can rewind times is a intorverted shy little beauty")
    typewriter_effect("She is also...insecure about things that she faced")
    typewriter_effect("Anyway....I cant talk like this much longer since you have to figure out by yourself")
    typewriter_effect("Adios.....")
    typewriter_effect(".........")
    
    


playsound("(You're The) Devil in Disguise - Elvis Presley.mp3", block=False)

if __name__ == "__main__":
    main()