# Floyd's Triangle

n = 5
increment = 1

for i in range(n):
    for j in range(0, i+1):
        print(increment, end="")
        increment+=1
    print()
