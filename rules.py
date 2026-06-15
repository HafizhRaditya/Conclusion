import sys
import time

def typewriter_effect(text, delay = 0.25):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main ():
    typewriter_effect("Hello....", delay=0.25)
    typewriter_effect("Gentlemen.....Welcome to Fight Club", delay=0.25)
    typewriter_effect("........", delay=0.25)
    typewriter_effect("First rule of Fight Club is......You do not talk about Fight Club", delay=0.25)
    typewriter_effect(".......", delay=0.25)
    typewriter_effect("Second rule of Fight Club is....You do not talk about Fight Club",delay=0.25)
    typewriter_effect("......", delay=0.25)
    typewriter_effect("Third rule....someone yells stop...goes limb....taps out....the fight is over", delay=0.25)
    typewriter_effect("Fourth rule...only two guys in a fight", delay=0.25)
    typewriter_effect("Fifth rule.....one fight at one time fellas" , delay=0.25)
    typewriter_effect("Sixth rule....no shirt....no shoes", delay=0.25)
    typewriter_effect("Seven rule.....fight will go on as long as they have to",  delay=0.25)
    typewriter_effect("And the eight and the final rule......If this is your first night in Fight Club", delay=0.25)
    typewriter_effect(".............", delay=0.25)
    typewriter_effect("You have to Fight.....", delay=0.25)




if __name__ == "__main__":
   main()