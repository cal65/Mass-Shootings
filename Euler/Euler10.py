import numpy as np
from matplotlib.pyplot import *

def make_primes(n):
	primes = np.arange(2,n+1)
	i=0
	num=0
	while num < sqrt(2000000):
		num = primes[i]
		primes = primes[((primes % num != 0) | (primes == num)).nonzero()]
		i += 1
	return primes

def sieve_of_eratosthenes(N):
    # Create a boolean array "prime[0..N]" and initialize all entries as true.
    # A value in prime[i] will be false if i is not a prime, true if i is a prime.
    prime = [True for _ in range(N+1)]
    p = 2

    while p * p <= N:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to False starting from p*p
            for i in range(p * p, N+1, p):
                prime[i] = False
        p += 1

    # Collecting all prime numbers
    prime_numbers = [p for p in range(2, N) if prime[p]]

    return prime_numbers