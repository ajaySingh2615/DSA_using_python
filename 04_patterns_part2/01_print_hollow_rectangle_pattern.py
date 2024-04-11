#print hollow rectangle pattern

row = 4
col = 5

for i in range(1, row+1):
    for j in range(1, col+1):
        if i == 1 or j == 1 or i == 4 or j == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()
