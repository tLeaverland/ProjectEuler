import math

def PrimeFactors(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
    
    for i in range(3, math.ceil(math.sqrt(n)), 2):
        while n % i == 0:
            primes.append(i)
            n = n / i

    if n > 2:
        primes.append(n)
    
    return primes

print(PrimeFactors(315))
