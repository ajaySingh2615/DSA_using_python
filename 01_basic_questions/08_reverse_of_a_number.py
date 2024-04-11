n = 10899

while n > 0:
    lastdigit = n % 10
    print(lastdigit, end="")
    n//=10