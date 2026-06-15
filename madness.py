import sys
import time

def typewriter_effect(text, delay = 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    typewriter_effect("I appreciate your realization....", delay=0.15)
    typewriter_effect(".....", delay=0.15)
    typewriter_effect("But this is too much....", delay=0.15)
    typewriter_effect("I dont want this.....", delay=0.15)
    typewriter_effect("WHAT DO YOU WANT?" , delay=0.15)
    typewriter_effect(".......", delay=0.15)
    typewriter_effect("You wanna go back to your shitjob? FUCKING CONDO AND WATCHING SITCOMS?", delay=0.15)
    typewriter_effect("FUCK YOU.....I WONT DO IT", delay=0.15)
    typewriter_effect("........", delay=0.15)
    typewriter_effect("Whats that smell?" , delay=0.15)
    typewriter_effect("Trust me....everything is gonna be fine.....", delay=0.15)
    typewriter_effect("........", delay=0.15)
    typewriter_effect("You met me in a very strange time....", delay=0.15)
    typewriter_effect("We are god's unwanted Children?", delay=0.15)
    typewriter_effect("FUCK YOU.......WHAT THE FUCK DO YOU KNOW?", delay=0.15)
    typewriter_effect("Cause I gotta Wake Up", delay=0.15)
    typewriter_effect("LET GO!")
    typewriter_effect("Not fear...but know...that someday you're gonna die", delay=0.15)
    typewriter_effect("Its only after we've lost everything that we're free to do anything", delay=0.15)
    typewriter_effect("But when his drinking and lusting and his hunger of power", delay=0.15)
    typewriter_effect("Become known and known to more people", delay=0.15)
    typewriter_effect("The demans to do something about this outrageous mean become louder and louder", delay=0.15)
    typewriter_effect(".......")
    typewriter_effect("YOU FAILED ME", delay=0.15)
    typewriter_effect("You're just trying to save me but its too late.....", delay=0.15)
    typewriter_effect("Cause I gotta wake up.......", delay=0.15)
    typewriter_effect(".........", delay=0.15)
    typewriter_effect("Ahhhh...fantasy....fantasy....fantasy", delay=0.15)
    typewriter_effect("Strongest drug ever", delay=0.15)
    typewriter_effect("FUCK YOU......I WONT DO IT", delay=0.15)
    typewriter_effect("The Baba Yaga.....")
    typewriter_effect("Is a man of focus......commitment....and sheer fucking will.....", delay=0.15)
    typewriter_effect("................", delay=0.15)
    typewriter_effect("Does a man like you ever know peace?", delay=0.15)
    typewriter_effect("Why not?", delay=0.15)
    typewriter_effect("......")


if __name__ == "__main__":
    main()