import random
print("= Guessing Game =")

value = random.randrange(1,5)
attempts = 0

while True:
    num = eval(input("Guess a number = "))

    if value == num:
        attempts += 1
        print(f"{num} Correct number!")
        break
    else:
        attempts += 1
        print(f"{num} Incorrect number.")
        continue

print(f"You had {attempts} attempts!")