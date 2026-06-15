## I want to write a code about typewriter effect in python. 

import sys
import time
import os
import random
import string
import threading

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_string(length=10):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

def main ():
    typewriter_effect("Me wants coming for me...", delay=0.15)
    typewriter_effect("........", delay=0.15)
    typewriter_effect("Well what was coming for you?", delay=0.15)
    typewriter_effect("...........", delay=0.15)
    typewriter_effect("The World Chico..........and everything in it!", delay=0.15)
    typewriter_effect("......", delay=0.15)
    typewriter_effect("THERE IS NO NOBILITY......IN POVERTY", delay=0.15)
    typewriter_effect("......", delay=0.15)
    typewriter_effect("I HAVE BEEN A RICH MAN AND I'VE BEEN A POOR MAN AND I CHOSE TO BE RICH EVERY FUCKING SINGLE DAY", delay=0.15)
    typewriter_effect("......", delay=0.15)
    typewriter_effect("DOES YOUR GIRLFRIEND THINK THAT YOU ARE A FUCKING LOSER?", delay=0.15)
    typewriter_effect("DO YOUR PARENTS THINK THAT YOU ARE A WORTHLESS PIECE OF SHIT?", delay=0.15)
    typewriter_effect("ARE YOU SAD BECAUSE YOU CANNOT DO ANYTHING RIGHT?", delay=0.15)
    typewriter_effect("ARE YOU NOT SATISFIED WITH YOUR LIFE AND JEALOUS OF OTHERS ACHIEVEMENTS?", delay=0.15)
    typewriter_effect("DOES YOUR FRIEND THINK THAT YOU ARE A FUCKING IDIOT THAT NOBODY CARES?", delay=0.15)
    typewriter_effect("ARE YOU FUCKING LONELY? NOBODY WANTS TO TALK WITH YOU?", delay=0.15)
    typewriter_effect("................", delay=0.15)
    typewriter_effect("GOOD..........GET YOUR ASS TO THE GROUND AND JUMP INTO THE FUCKING MENTAL LAB", delay=0.15)
    typewriter_effect("............", delay=0.15)
    typewriter_effect("AND IF ANYONE TRIES TO STOP YOU?", delay=0.15)
    typewriter_effect("I DONT GIVE A FLYING FUCKING FUCK..........", delay=0.15)
    typewriter_effect("ASSHOLE.....", delay=0.15)


if __name__ == "__main__":
    main()