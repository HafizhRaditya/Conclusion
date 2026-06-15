print("=" * 50)
print("FANTASY")
print("=" * 50)

print("\nYou ever had a fantasy?")
while True:
    answer = input("(yes/no): ").lower().strip()
    if answer in ['yes', 'y']:
        is_fantasy = True
        break
    elif answer in ['no', 'n']:
        is_fantasy = False
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if is_fantasy:
    print("\nDo you believe in it?")
    while True:
        answer = input("(yes/no): ").lower().strip()
        if answer in ['yes', 'y']:
            print("\n>>> Then you are capable of imagination and hope.")
            break
        elif answer in ['no', 'n']:
            print("\n>>> Perhaps it's just a distraction from reality.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
else:
    print("\nDo you want one?")
    while True:
        answer = input("(yes/no): ").lower().strip()
        if answer in ['yes', 'y']:
            print("\n>>> Dreams are what make us human.")
            break
        elif answer in ['no', 'n']:
            print("\n>>> Reality is enough for some.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

print("\n" + "=" * 50)
print("Thank you for your time.")
print("=" * 50)