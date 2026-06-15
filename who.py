## I want to make a code about a tyepwriter efffect in python and its only an output based on what I wrtie

import sys
import time
def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main():
    typewriter_effect("Who can it be knocking at my door?", delay=0.1)
    typewriter_effect(".......", delay = 0.1)
    typewriter_effect("Go away, don't come around here no more", delay=0.1)
    typewriter_effect("Cant you see that its late at night?", delay=0.1)
    typewriter_effect("....", delay=0.1)
    typewriter_effect("Im very tired....and im not feeling right", delay=0.1)
    typewriter_effect("All I wish is to be alone", delay=0.1)
    typewriter_effect("....", delay=0.1)
    typewriter_effect("Stay away, dont you invade my home", delay=0.1)
    typewriter_effect("Best off if you hang outside....", delay=0.1)
    typewriter_effect("Dont come in....I only run and hide", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("......", delay=0.1)
    typewriter_effect("Who can it be knocking at my door?", delay=0.1)
    typewriter_effect("Make no sound....tiptoe across the floor", delay=0.1)
    typewriter_effect("If hears...he'll knock all day", delay=0.1)
    typewriter_effect("I'll be trapped...and here I'll have to stay", delay=0.1)
    typewriter_effect("I've done no harm and I keep to myself", delay=0.1)
    typewriter_effect("There's nothing wrong with my...state of mental health", delay=0.1)
    typewriter_effect("I like it here with my childhood friends", delay=0.1)
    typewriter_effect("Here they come...those feelings again", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("Who can it be now.....?", delay=0.1)
    typewriter_effect("......", delay=0.1)
    typewriter_effect("Is it the man come to take me away?", delay=0.1)
    typewriter_effect("Why do they follow me?", delay=0.1)
    typewriter_effect("Its not the future that I can see...", delay=0.1)
    typewriter_effect("It's just my fantasy", delay=0.1)
    typewriter_effect("Yeah....", delay=0.1)
    typewriter_effect("............", delay=0.1)
    typewriter_effect("............", delay=0.1)
    typewriter_effect("............", delay=0.1)
    typewriter_effect("Who?Who?Who?", delay=0.1)
    typewriter_effect("Who can it be now?....", delay=0.1)
    typewriter_effect("Who can it be now?....", delay=0.1)
    typewriter_effect("Who can it be now?....", delay=0.1)
    typewriter_effect("Who can it be now?....", delay=0.1)
    typewriter_effect("Ohhhhh....ohhhh....", delay=0.1)
    typewriter_effect("Who can it be now?....", delay=0.1)
    typewriter_effect("Ohhhhh....we....ohhh....", delay=0.1)
    typewriter_effect("Who can it? Who can it?", delay=0.1)
    typewriter_effect("Ohhhhh.....ohhhhh....", delay=0.1)
    typewriter_effect("Who can it be now?....", delay=0.1)
    typewriter_effect("Ohhhhh....we....ohhhh....", delay=0.1)
    typewriter_effect("Yeah...yeah.....yeah....", delay=0.1)




if __name__ == "__main__":
    main()