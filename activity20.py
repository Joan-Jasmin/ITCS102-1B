for J in range(1,11,1):
    for A in range(10,J,-1):
        print(' ', end='')
    for S in range(1,J,1):
        print('x', end='')
    for P in range(1,J,1):
        print('x', end='')
    print()

for E in range(1,11,1):
    for R in range(E,1,-1):
        print(' ',end='')
    for G in range(10,E,-1):
        print('x',end='')
    for F in range(10,E,-1):
        print('x',end='')
    print()