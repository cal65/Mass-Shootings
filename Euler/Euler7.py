from numpy import *
from matplotlib.pyplot import *

primes = range(1,4)

num = 3
while len(primes) < 10001:
	num += 2
	new_prime = True
	for j in range(1, len(primes)):
		if num % primes[j] == 0: new_prime = False	
	if not new_prime: continue
	primes.append(num)
	