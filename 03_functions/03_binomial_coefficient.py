def binomial_coefficient(n:int, r:int):
    nth = factorial(n)
    rth = factorial(r)
    n_minus_r = factorial(n - r)

    return nth//(rth * (n_minus_r))

def factorial(a:int):
    fact = 1
    while a != 0:
        fact = fact * a
        a -= 1
    return fact


binomial_result = binomial_coefficient(5, 2)
print(binomial_result)