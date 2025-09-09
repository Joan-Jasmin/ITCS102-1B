temp = eval(input("Temperature is ? "))
if temp <= 0:
	print("Freezing Temperature")
elif temp >= 1 and temp <= 15:
	print("Cold Temperature")
elif temp >= 16 and temp <= 30:
	print("Cool Temperature")
elif temp >= 31 and temp <= 45:
	print("Lukewarm Temperature")
elif temp >= 46 and temp <= 60:
	print("Warm Temperature")
elif temp >= 61 and temp <= 75:
	print("Hot Temperature")
elif temp >= 76 and temp <= 90:
	print("Boiling Temperature")
elif temp >= 91:
	print("Burning Temperature")
else:
	print("Invalid")