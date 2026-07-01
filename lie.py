import os
import time
import sys

def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    typewriter_effect("All I want is to have my peace of mind")
    typewriter_effect("I understand about indecision")
    typewriter_effect("Who the fuck are you?")
    typewriter_effect("I said fuck you....watch this asshole")
    typewriter_effect("Yeah")
    typewriter_effect(";.....")
    typewriter_effect("???????")
    typewriter_effect("People live in a competition")
    typewriter_effect("No no no")
    typewriter_effect("Thats right you creepy old....motherfucker")
    typewriter_effect("Asshole")
    typewriter_effect("Fuck you")
    typewriter_effect("Prick")
    typewriter_effect("Cocksucking piece of shit")

    if __name__ == "__main__":
        main()

    