import sys
import time
from playsound3 import playsound

def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_line():
    print("\n" + "-" * 30 + "\n")

def main():
    playsound("No Below.mp3", block=False)

    typewriter_effect("[Mason slowly opens his eyes. His head feels heavy.]")
    typewriter_effect("[The room is pitch black and feels freezing cold. Suddenly, the sound of approaching footsteps echoes...]")
    time.sleep(1)

    typewriter_effect("Paul: Hello Hello....")

    print("\n1. Where Am I?")
    print("2. Who The Fuck Are You?")
    print("3. What? What The Fuck is this?")

    choice = input("\nType the right number (1/2/3): ")
    draw_line()

    if choice == "1":
        typewriter_effect("Mason: Where am I?")
        typewriter_effect("[Paul smirks faintly from the shadows.]")
        typewriter_effect("Paul: Let's just say you are in a deep void that no one will find you.")
    elif choice == "2":
        typewriter_effect("Mason: Who the fuck are you?!")
        typewriter_effect("[Paul chuckles softly, his laughter echoing in the empty room.]")
        typewriter_effect("Paul: Me? Ahahahahha....sooner or later you will know.")
    elif choice == "3":
        typewriter_effect("Mason: What? What the fuck is this?!")
        typewriter_effect("Paul: This? This is the fuck my soggy little friend.")
    else:
        typewriter_effect("Paul: Type the right number you stupid son of a bitch.")

    draw_line()
    
    typewriter_effect("[Paul walks around the tied-up Mason, glaring at him intensely.]")
    typewriter_effect("Paul: Anyway it doesnt matter anymore...you are here okay.")
    typewriter_effect("Paul: I dont give a damn whether you feel happy or sad or angry.")
    typewriter_effect("Paul: I'll say lets play a little game huh?")
    typewriter_effect("Paul: Simple...you answer my questions...and I let you live.")
    
    time.sleep(1)
    typewriter_effect("\nPaul: What do you know about Oregon?")

    typewriter_effect("\n1. Arcadia Bay?")
    typewriter_effect("2. A state in the USA?")
    typewriter_effect("3. Uhh...no I dont know")

    choice = input("\nType the right number (1/2/3): ")
    draw_line()

    if choice == "1":
        typewriter_effect("Mason: Arcadia bay?")
        typewriter_effect("[Paul stops in his tracks. He stares at Mason with a surprised yet satisfied look.]")
        typewriter_effect("Paul: Hahahahaha...didnt expect that much.")
        typewriter_effect("Paul: But I tell you what...you got the right answer cause thats what I mean.")
        
    elif choice == "2":
        typewriter_effect("Mason: A state in the USA?")
        typewriter_effect("[Paul scoffs in annoyance and rolls his eyes.]")
        typewriter_effect("Paul: I know that dummy...tell me something that I dont know.")
        typewriter_effect("Paul: .........")
        
        print("\nA. A state like...your favorite state?")
        print("B. Its where your parents come from?")
        print("C. Ahh...your girlfriend lives there.")
        
        choice2 = input("\nType the letter (A/B/C): ").upper()
        draw_line()
        
        if choice2 == "A":
            typewriter_effect("Mason: A state like...your favorite state?")
            typewriter_effect("Paul: Favorite Place? You have got to be kidding me.")
            typewriter_effect("Paul: You could say that...but I expect something more.")
            typewriter_effect("Paul: Its Arcadia Bay dummy.")
            typewriter_effect("Paul: A town full of mystery and probably where two broken girls found each other.")
        elif choice2 == "B":
            typewriter_effect("Mason: Its where your parents come from?")
            typewriter_effect("Paul: No..fuck no.")
            typewriter_effect("Paul: Arcadia Bay....thats my expectations.")
        elif choice2 == "C":
            typewriter_effect("Mason: Ahh...your girlfriend lives there.")
            typewriter_effect("[Paul laughs out loud, though his laughter sounds hollow.]")
            typewriter_effect("Paul: Hahahaa ahhh...I wish.")
            typewriter_effect("Paul: But Im not looking that answer.")
        else:
            typewriter_effect("Paul: You can't even pick a simple letter.")
            
    elif choice == "3":
        typewriter_effect("Mason: Uhh...no I dont know.")
        typewriter_effect("Paul: I cant take that answer.")
        typewriter_effect("[You Got Shot]")
        sys.exit()
    else:
        typewriter_effect("Paul: Type the right number you stupid son of a bitch.")

    
    typewriter_effect("Paul : Well you know what...Im getting bored of this")
    typewriter_effect("Paul : No no no...I'll be back, but right now...Im too lazy seeing your ugly faces")
    sys.exit()

if __name__ == "__main__":
    main()