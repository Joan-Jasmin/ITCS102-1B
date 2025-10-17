gold = True

while gold == True:
    brine = input("Is the water salty? (yes/no): ").lower()
    if brine == 'yes':
        print("Unable to drink..")
        continue
    else:
        print("Able to dirnk!")
        break