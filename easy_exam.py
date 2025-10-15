# Part 1
for J in range(1,6,1):
    for A in range(6,J,-1):
        print(" ",end='')
    for S in range(1,2*J,1):
        print("*",end='')
    print()

# Part 2
for J in range(1,6,1):
    for G in range(1,J+1,1):
        print(J,end='')
    print()