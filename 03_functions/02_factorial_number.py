def factorial_number(num:int):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    
    return fact

num1 = factorial_number(5)
print(num1)
