

import sys
import time

def typewriter_effect(text, delay = 0.1):
    for char in text:
        sys.stdout.write(f"\033[91m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    typewriter_effect("You know a story about a scorpion and a frog?", delay=0.15)
    typewriter_effect("......", delay=0.15)
    typewriter_effect("The scorpion asks the frog to carry him across the river", delay=0.15)
    typewriter_effect("How Do I Know You Won't Sting me? Asks the frog", delay=0.15)
    typewriter_effect("Because If I Do....We Both Will be Drowned", delay=0.15)
    typewriter_effect("The frog carry the scorpion across the river", delay=0.15)
    typewriter_effect("Later...the scorpion stings the frog on the water", delay=0.15)
    typewriter_effect("Why? Asks the frog", delay=0.15)
    typewriter_effect("Because It's My Nature To Do So", delay=0.15)
    typewriter_effect(".........", delay=0.15)
    typewriter_effect("What do you do?", delay=0.15)
    typewriter_effect("I Drive......")
    typewriter_effect("Like a Limo Driver?", delay=0.15)
    typewriter_effect("No....for movies and stunt", delay=0.15)
    typewriter_effect(".........", delay=0.15)
    typewriter_effect("I have to go somewhere else and I dont think I can come back", delay=0.15)
    typewriter_effect("But I just want you to know....", delay=0.15)
    typewriter_effect("...........", delay=0.15)
    typewriter_effect("Meeting you and Benicio is one of the beautiful thing I've ever seen", delay=0.15)
    typewriter_effect(".......", delay=0.15)
    typewriter_effect("......", delay=0.15)
    typewriter_effect("My hands are a little dirty")
    typewriter_effect("........", delay=0.15)
    typewriter_effect("YOU TOLD HIM ABOUT IRENE!!!!!!!!!", delay=0.15)
    typewriter_effect("There's a hundred thousand streets in the city....", delay=0.15)
    typewriter_effect("You dont need to know the route", delay=0.15)
    typewriter_effect("Anything that happens in that five minutes and Im yours...", delay=0.15)
    typewriter_effect("Anything that happens a minute on the either side of that...", delay=0.15)
    typewriter_effect("And you're on your own....", delay=0.15)
    typewriter_effect("Do you Understand?", delay=0.15)
    typewriter_effect("You tell me where we start..where we're going...where we're going afterwards...I give you five minutes when we get there", delay=0.15)
    typewriter_effect("I don't carry a gun....I drive", delay=0.15)

if __name__ == "__main__":
    main()
