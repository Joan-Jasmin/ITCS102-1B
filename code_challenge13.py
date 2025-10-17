name = input("What's your name? ")
odd = 0
oddval = ""
even = 0
evenval = ""

while True:
    val = eval(input("Give a number = "))
    if val == 0:
        print(f"Stop!\nHey! {name}, \nThe odds total is: {odd}\nThe odds are: {oddval}")
        print(f"The evens total is: {even}\nThe evens are: {evenval}")
        break
    elif val % 2 == 1:
        print("Odd!")
        odd += val
        oddval += str(val) + " "
        continue
    else:
        if val % 2 == 0:
            print("Even!")
            even += val
            evenval += str(val) + " "
        continue