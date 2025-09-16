sum = 0
for n in range(1, 8, 1):
    number = eval(input("Enter number = "))
    if number % 2 != 0:
        sum += number
print('Odd sum is',sum)