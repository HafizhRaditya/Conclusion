import sys
import time
from playsound3 import playsound

def typewriter_effect(text, delay=0.1): 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
   
    playsound("Ooh Ahh (My Life Be Like) (feat. Tobymac) - Grits.mp3", block=False)

    typewriter_effect("Hello...")
    typewriter_effect("In here you will answer your preferences about cars.")
    typewriter_effect("Let's find out if you belong to Tuner, Muscle, or Exotic!\n")

    typewriter_effect("What is your favorite car brand?")

    
    brands = ["Nissan", "Mitsubishi", "Chevrolet", "Dodge", "Lamborghini", "Porsche"]
    
    
    for i, brand in enumerate(brands, 1):
        print(f"{i}. {brand}")

    print("\n" + "-" * 30)
    
   
    try:
        choice = int(input("Enter the number corresponding to your favorite brand: "))
        
        if choice < 1 or choice > len(brands):
            print("Invalid choice. Please try again.")
            return
            
        selected_brand = brands[choice - 1]
        print("\n" + "=" * 30)
        typewriter_effect(f"You selected: {selected_brand}")
        
       
        if selected_brand in ["Nissan", "Mitsubishi"]:
            typewriter_effect("Awesome! You love TUNER cars.")
            typewriter_effect("You probably love street racing and modifying your cars to the absolute limit!")
            
        elif selected_brand in ["Chevrolet", "Dodge"]:
            typewriter_effect("Hell yeah! You love MUSCLE cars.")
            typewriter_effect("Nothing beats pure raw V8 power and burning rubber on a drag strip, right?")
            
        elif selected_brand in ["Lamborghini", "Porsche"]:
            typewriter_effect("Classy! You love EXOTIC cars.")
            typewriter_effect("Speed, luxury, and head-turning aerodynamic designs are your top priorities.")

    except ValueError:
        
        print("Please enter a valid number!")

    print("=" * 30)
    typewriter_effect("\nThank you for sharing your preferences!")

    typewriter_effect("Hold on....this is not the end!")
    typewriter_effect("More questions for you")

    typewriter_effect("Pick One Car")
    typewriter_effect("1. 1992 Nissan Skyline GT-R R32")
    typewriter_effect("2. 1969 Ford Mustang Boss 429 ")
    typewriter_effect("3. 1988 BMW M3 E30")

    choice2 = input("Enter the number corresponding to your favorite car:")
    if choice2 == "1":
        typewriter_effect("A JDM Car? Huh...must be a tuner and japanese freak")
    elif choice2 == "2":
        typewriter_effect("Boss 429? You a fan of John Wick?")
    elif choice2 == "3":
        typewriter_effect("The Beamer? Cant complain about it")
    else:
        typewriter_effect("Invalid choice. Please try again.")
    
    typewriter_effect("\n If you are Dominic Toretto, which car would you choose to drive?")
    typewriter_effect("1. 1970 Dodge Charger R/T")
    typewriter_effect("2. 1987 Buick GNX")
    typewriter_effect("3. 1970 Playmouth Road Runner")

    choice3 = input("Enter the number corresponding to your favorite car:")
    if choice3 == "1":
        typewriter_effect("The charger? This baby hits harder than family")
    elif choice3 == "2":
        typewriter_effect("Ahh..the GNX. A sleeper car with a turbocharged V6. Not bad at all!")
    elif choice3 == "3":
        typewriter_effect("The Road Runner? Now that's a classic!")
    else:
        typewriter_effect("Invalid choice. Please try again.")

    typewriter_effect("\n Last question! If you could have one supercar, which one would it be?")
    typewriter_effect("1. Lamborghini Aventador")
    typewriter_effect("2. Porsche 911 Turbo S")
    typewriter_effect("3. Ferrari 488 GTB")

    choice4 = input("Enter the number corresponding to your favorite supercar:")
    if choice4 == "1":
        typewriter_effect("The Aventador? That's a beast!")
    elif choice4 == "2":
        typewriter_effect("The 911 Turbo S? Pure perfection!")
    elif choice4 == "3":
        typewriter_effect("The 488 GTB? A true icon!")
    else:
        typewriter_effect("Invalid choice. Please try again.")

    typewriter_effect("\n You still love cars?")
    typewriter_effect("I always love cars man...")
    typewriter_effect("Ahahaha...what did you ride back there?")
    typewriter_effect("Subway...")
    typewriter_effect(".........")
    typewriter_effect("I see")
    typewriter_effect("Well, I hope you enjoyed this little quiz about your car preferences!")
    typewriter_effect("Remember, it's all in good fun and there's no right or wrong answers when it comes to cars. Everyone has their own unique tastes and preferences.")
    typewriter_effect("Thanks for participating, and keep loving cars!")

if __name__ == "__main__":
    main()