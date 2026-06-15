import sys
import time
import os

from confession import typewriter_effect

def typewrter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        print()

def main():
    typewriter_effect("I thnik human consiusness is a tragic mistep of evolution")
    typewriter_effect("You see thats what the preacher tried to sell")
    typewriter_effect("same as shrink")
    typewriter_effect("You see thats what the preacher tried to tell you")
    typewriter_effect("By the end of the tunnel there will be a light shining through your soul")
    typewriter_effect("And they tell you about virtue")
    typewriter_effect(".............")
    typewriter_effect("It means im bad at parties")
    typewriter_effect("I tell myself to stop reproducing but obviously my programming that tells me to do so")
    typewriter_effect("No...I never found peace in my whole life")
    typewriter_effect("Im an addict")
    typewriter_effect("I dont know what you're talking about chief")

if __name__ == "__main__":
    main()