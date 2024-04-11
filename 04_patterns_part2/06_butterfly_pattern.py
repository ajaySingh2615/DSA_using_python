# Butterfly pattern

n = 4

for i in range(1, n+1):

    # print star
    for j in range(i):
        print("*", end="")

    # print space
    for j in range(0, 2*(n-i)):
        print(" ", end="")
    
    # print star
    for j in range(i):
        print("*", end="")
    print()
    