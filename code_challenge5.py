number = eval(input('Your number? '))
factorial = 1
for n in range(number, 0, -1):
    factorial *= n
print('The factorial of',number,'is',factorial)