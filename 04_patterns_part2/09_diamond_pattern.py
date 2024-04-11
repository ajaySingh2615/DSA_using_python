# diamond pattern

n = 4

for i in range(1, n+1):
    
    # for space
    for j in range(1, n-i+1):
        print(" ", end="")
    
    # for stars
    for j in range(1, (2*i)-1+1):
        print("*", end="")

    print()