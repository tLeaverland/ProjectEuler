import math
from Problem3 import PrimeFactors
from collections import Counter

def triangular_numbers(n):
    i, t = 1, 0
    while i <= n:
        yield t
        t += i
        i += 1

triangles = triangular_numbers(12700) #12700
next(triangles)

run = True

while run:

    factor_powers = 1
    next_triangle = next(triangles)
    print(next_triangle)
    factors = PrimeFactors(next_triangle)
    factor_values = Counter(factors).values()

    for each in factor_values:
        factor_powers *= (each + 1)
        
    print(factor_powers)
        
    if factor_powers > 500:
        run = False
        print(next_triangle)



