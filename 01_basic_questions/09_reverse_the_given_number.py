n = 10899

reverseNumber = 0

while n > 0:
    lastDigit = n % 10
    reverseNumber = reverseNumber * 10 + lastDigit
    n//=10

print(reverseNumber)
