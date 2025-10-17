number = int(input("Give number = "))

for J in range(1, 11):
    for G in range(1, number + 1):
        print(f"{J} x {G} = {J * G}\t", end='')
    print()