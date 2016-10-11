from numpy import *
from matplotlib.pyplot import *

tri_num=[1]
divisors = []

for i in range(2, 10001):
	tri_num.append(tri_num[i-2] + i)
	primes = prime_factors(tri_num[i-2])

	divisors.append(temp_div*2)

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors