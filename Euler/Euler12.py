from numpy import *
from matplotlib.pyplot import *

tri_num=[1]
divisors = [1]
i=2
while max(divisors) < 500:
	tri_num.append(tri_num[i-2] + i)
	primes = array(prime_factors(tri_num[i-2]))
	uniques = array(unique(primes))
	factors = 1
	for j in uniques:
		factors *= (len(primes [ where (primes == j)])+1)
	divisors.append(factors)
	i+=1

tri_num[i-3]


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