name = input("what is your name? ")
fare = eval(input("how much is your fare fee? "))
astudent = input("are you currently a student? (yes / no) ")

if astudent.lower() == 'yes' :
	discount = fare * 0.2
	#fare -= discount
	new_fare = fare - discount
	print("hi ", name)
	print("your discount is ", discount)
	print("your new fare is ", new_fare)
else:
	print("sorry you are not eligible for a discount")