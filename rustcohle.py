## I want to make a code that has typewriter effect in python and the output has red color text. How can I do that?
## I want to call the function with the text "Why should I live in history huh?" and a delay of 0.2 seconds between each character. But I want it as a horizontal sentence, not vertical.

import sys
import time
def typewriter_effect(text, delay = 0.1):
    for char in text:
        sys.stdout.write(f"\033[91m{char}\033[0m")
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Add a newline at the end of the text

def main():
    typewriter_effect("Why should I live in history huh?", delay=0.2)
    typewriter_effect("Fuck...I dont want to know anything anymore", delay=0.2)
    typewriter_effect("This is the world where nothing is solved", delay=0.2)
    typewriter_effect(".......", delay=0.2)
    typewriter_effect("And someone told me...time is a flat circle", delay=0.2)
    typewriter_effect("Whatever we do or we'll do will be repeated over and over again", delay=0.2)
    typewriter_effect("......", delay=0.2)
    typewriter_effect("You had any sleep last night?", delay=0.2)
    typewriter_effect("......", delay=0.2)
    typewriter_effect("I dont sleep....I just dream", delay=0.2)
    typewriter_effect("..........", delay=0.2)
    typewriter_effect("You wonder ever.....you're a bad man?", delay=0.2)
    typewriter_effect("Choo...chooo...choo...choo....chooo", delay=0.1)
    typewriter_effect("No....I dont wonder Marty.....the world need bad man", delay=0.2)
    typewriter_effect(".....", delay=0.2)
    typewriter_effect("We keep the other bad man from the door", delay=0.2)
    typewriter_effect("......", delay=0.2)
    typewriter_effect("Strange?.....heheheh...y-yeah", delay=0.2)
    typewriter_effect("Rust...is a type of a guy who would fight the sky...if he doesnt see the color blue", delay=0.2)
    typewriter_effect("Tell me about Cohle...he...kinda a strange guy huh?", delay=0.2)
    


if __name__ == "__main__":
    main()