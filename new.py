characters = ["Rustin Cohle", "The Driver", "Officer K"]

print("Choose a character by name or number:")
for i, name in enumerate(characters, 1):
	print("%d) %s" % (i, name))

choice = input("Enter name or number: ").strip()

if choice.isdigit():
	idx = int(choice)
	if idx == 1:
		print("You selected: %s — A contemplative detective." % characters[0])
	elif idx == 2:
		print("You selected: %s — A mysterious, quiet driver." % characters[1])
	elif idx == 3:
		print("You selected: %s — A future-seeing officer." % characters[2])
	else:
		print("Invalid number: %s" % choice)
else:
	low = choice.lower()
	if low in ("rustin cohle", "cohle", "rustin"):
		print("You selected: %s — A contemplative detective." % characters[0])
	elif low in ("the driver", "driver"):
		print("You selected: %s — A mysterious, quiet driver." % characters[1])
	elif low in ("officer k", "k", "officer"):
		print("You selected: %s — A future-seeing officer." % characters[2])
	else:
		print("Unknown character: %s" % choice)
