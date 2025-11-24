from activity24_1 import info, cont

cont(input("Are you a Prince? (yes/no): "))
if cont == 'yes':
    print("Your Highness!")
elif cont == 'no':
    print("Peasantry?")

print("\nWould you like an escort, your highness? But first, please introduce yourself.\n")
name = input("Who: ")
status = input("Status: ")
locale = input("From: ")

info(name, status, locale)