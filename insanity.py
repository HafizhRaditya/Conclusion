## This is a simple code, I only write the output or printf only, but i want to add a typewritter effect on the output
## Here it is amigos....
import sys
import time
def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main():
    typewriter_effect("Do you want to see what's in my head? Dont try to tell anyone.", delay=0.2)
    if input("Type 'yes' to continue: ").lower() != 'yes':
        typewriter_effect("Fine, be that way.", delay=0.2)
        return
    typewriter_effect("Did I ever tell you....the definition of insanity?", delay=0.2)
    typewriter_effect("Insanity....is doing the same fucking thing and expecting....shit to change", delay=0.2)
    typewriter_effect("Insanity...is where people kleep doing the same routine....and expecting their life is gonna change", delay=0.2)
    typewriter_effect("Lyle....is that you?", delay=0.2)
    typewriter_effect("Im sorry...I dont like the way......you're looking at me okay?", delay=0.2)
    typewriter_effect("Do you have a problem with me? Do you think Im bulshitting you? FUCK YOU!! OKAY? FUCK....YOU", delay=0.2)
    typewriter_effect("THEY SAID ME ME ME......WHO THE FUCK....IS IT GOING TO BE????? ME OR THEM?????? THEM......OR ME?", delay=0.2)
    typewriter_effect("Like....they fucking think I'm a fucking maniac.....", delay=0.2)
    typewriter_effect("I'm too lazy for this shithole", delay=0.2)
    typewriter_effect("Do you like your job?", delay=0.2)
    typewriter_effect("Not Exactly", delay=0.2)
    typewriter_effect("What do you want? You wanna go back to your shit job? Fucking condo and watching sitcom", delay=0.2)
    typewriter_effect("Fuck you....I wont do it", delay=0.2)
    typewriter_effect("I took a souvenir....her pretty head", delay=0.2)
    typewriter_effect("I saw you with the box...whats in the box?", delay=0.2)
    typewriter_effect("Whats in the fucking box?", delay=0.2)
    typewriter_effect("TELL ME SHE'S ALIVE!!!", delay=0.2)
    typewriter_effect("They wouldnt let you kill the suspect David", delay=0.2)
    typewriter_effect(" You wanna do something? You better think it wisely", delay=0.2)



    
    
if __name__ == "__main__":
    main()