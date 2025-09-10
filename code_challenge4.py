print("Wanna watch an Animated Movie? Pick your studio!")
print("1. DreamWorks / 2. Disney & Pixar / 3. Sony")
studio_choice = input("Your choice? (1/2/3): ")

if studio_choice == "1":
	print("You chose DreamWorks!")
	length = (input("Preferred length? (short/medium/long): "))

	if length == ("short"):
		print("Kung Fu Panda!")
	elif length == ("medium"):
		print("How to Train your Dragon!")
	elif length == ("long"):
		print("Shrek or Puss in Boots!")
	else:
		print("You can search online for more options!")

if studio_choice == "2":
	print("You chose Disney & Pixar!")
	length = (input("Preferred length? (short/medium/long): "))

	if length == ("short"):
		print("Tangled!")
	elif length == ("medium"):
		print("Brave!")
	elif length == ("long"):
		print("Moana!")
	else:
		print("You can search online for more options!")

if studio_choice == "3":
	print("You chose Sony!")
	length = (input("Preferred length? (short/medium/long): "))

	if length == ("short"):
		print("Mitchells and the Machines!")
	elif length == ("medium"):
		print("Kpop Demon Hunters!")
	elif length == ("long"):
		print("The Spider-Verse Movies!")
	else:
		print("You can search online for more options!")

