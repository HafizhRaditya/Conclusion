import sys
import time

def typewriter_effect(text, delay = 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    typewriter_effect("My pain is constant and sharp", delay=0.15)
    typewriter_effect("....", delay=0.15)
    typewriter_effect("And I do not hope a better world for anyone....", delay=0.15)
    typewriter_effect("In fact....I want my pain to be conflicted with others", delay=0.15)
    typewriter_effect("......",delay=0.15)
    typewriter_effect("Loneliness has followed me in my whole life....", delay=0.15)
    typewriter_effect("In bars....in cars...sidewalks...store...everywhere...there's no escape....Im god's lonely man", delay=0.15)
    typewriter_effect("Happy or sad?", delay=0.15)
    typewriter_effect(".....",delay=0.15)
    typewriter_effect("Sad....", delay=0.15)
    typewriter_effect("Im warning you....I'll break your heart", delay=0.15)
    typewriter_effect(".....", delay=0.15)
    typewriter_effect("Already broken....", delay=0.15)
    typewriter_effect(".....", delay=0.15)
    typewriter_effect("Nearly got....FUCKING EVERYTHING...", delay=0.15)
    typewriter_effect("You look lonely.....I can fix that", delay=0.15)
    typewriter_effect("You're not your job.....", delay=0.15)
    typewriter_effect("There are no more barriers to cross...", delay=0.15)
    typewriter_effect("You're not how much money you have in the bank", delay=0.15)
    typewriter_effect("All I have in common....is the uncontrollable and the insanity", delay=0.15)
    typewriter_effect("All the mayhem I have caused.....I have now surprassed", delay=0.15)
    typewriter_effect("You're not the car you drive....", delay=0.15)
    typewriter_effect("I gain no deeper knowledge for myself...", delay=0.15)
    typewriter_effect("You're not the contents of your wallet", delay=0.15)
    typewriter_effect("You're not your fucking khakis....", delay=0.15)
    typewriter_effect("You are the all singing all dancing crap in the world", delay=0.15)
    typewriter_effect("But even after admitting this....there is no catharsis", delay=0.15)
    typewriter_effect("My pain continues to elude me", delay=0.15)
    typewriter_effect("This confession....has meant.....nothing", delay=0.15)
    typewriter_effect("I want.....I want a way out....of loneliness")
    typewriter_effect(".........", delay=0.15)


if __name__ == "__main__":
    main()
