import time
import sys
import os

def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    typewriter_effect("Ashamed?")
    typewriter_effect("Maybe this is the fate i suppose to believe in?")
    typewriter_effect("I see....")
    typewriter_effect("I've been lying to myself for a long time")
    typewriter_effect("I never thought that im a bad person")
    typewriter_effect("Pressure.....")
    typewriter_effect("Changes Everything...")
    typewriter_effect("Pressure.....")
    typewriter_effect("Changes Human Being")

if __name__ == "__main__":
    main()