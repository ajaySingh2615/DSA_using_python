# hollow rhombus

n = 5

for i in range(1, n+1):
    
    # for spaces
    for j in range(1, n-i+1):
        print(" ", end="")
    
    # for stars
    for j in range(1, n+1):
        if(i==1 or j ==1 or i == 5 or j == 5):
            print("*", end="")
        else:
            print(" ", end="")
    
    print()