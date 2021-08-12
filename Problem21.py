import math
from collections import Counter

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

def Sum_Divisors(n):

    sum = 1
    factor_list = Counter(PrimeFactors(n))
    factors = list(factor_list.keys())
    power = list(factor_list.values())

    for i in range(len(factors)):
        sum *= (factors[i] ** (power[i] + 1) - 1)/(factors[i] - 1)
    
    sum -= n # P.Euler asks for sum of PROPER divisors i.e. exclude n itself...
    return sum

amicable = set()

def Is_Amicable(n):

    if n not in amicable:
        d = Sum_Divisors(n)
        if Sum_Divisors(d) == n and n != d:
            amicable.add(n)
            amicable.add(d)
    else:
        pass

    return amicable

for i in range(2,10000):
    Is_Amicable(i)

print(sum(amicable))

    

  


