# solid rhombus

n = 5

for i in range(1, n+1):

    # for spaces
    for j in range(1, n-i+1):
        print(" ", end="")
    
    #for star
    for j in range(n):
        print("*", end="")
    print()
