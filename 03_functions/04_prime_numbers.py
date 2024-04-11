#prime numbers
import math

def prime_number(num: int):
    isPrimeNumber = True
    if num == 0:
        return True
    
    if num == 1:
        return True
    
    for i in range(2, int((math.sqrt(num)))+1):
        if num % i == 0:
            return False
        
    return isPrimeNumber

user = int(input("Enter any number to check prime or not:"))

result = prime_number(user)

if result:
    print(f"{user} is a prime number")
else:
    print(f"{user} is not a prime number")


