from numpy import *
from matplotlib.pyplot import *
from functools import lru_cache

@lru_cache(maxsize=5000)
def create_primes(n):
	"""
	Get list of all primes under n
	"""
	primes = [2,3]
	num = 3
	while len(primes) < n:
		num += 2
		new_prime = True
		for j in range(len(primes)):
			if num % primes[j] == 0: new_prime = False	
		if not new_prime: continue
		primes.append(num)
	return primes
	