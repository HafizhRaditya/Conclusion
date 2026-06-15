def ask_question(question):
    print(f"\n{question}")
    while True:
        answer = input("(yes/no): ").lower().strip()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    print("=" * 50)
    print("CHOICE")
    print("=" * 50)
    

    is_human = ask_question("Are you human?")
    
    if is_human:
        has_heart = ask_question("Do you have a heart?")
        if has_heart:
            print("\n>>> Then you are capable of love and compassion.")
        else:
            print("\n>>> Perhaps you keep it hidden from the world.")
    else:
        is_worthy = ask_question("Do you think you are worthy?")
        if is_worthy:
            print("\n>>> Self-worth is a powerful thing to possess.")
        else:
            print("\n>>> Maybe worthiness is something you need to discover.")
    
    print("\n" + "=" * 50)
    print("Thank you for your time.")
    print("=" * 50)

if __name__ == "__main__":
    main()
