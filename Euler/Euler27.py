import itertools
from numpy import *
primes = arange(2,2000001)

i=0
num=0
while num < sqrt(2000000):
	num = primes[i]
	primes = primes[((primes % num != 0) | (primes == num)).nonzero()]
	i += 1
vals = list(itertools.permutations(range(-1000,1001), 2))
vals[9999]

counter = []
for value in vals:
	n = 0
	a = value[0]
	b = value[1]
	quad = n**2 + a*n + b
	total = 0
	while (quad in primes):
		n += 1
		total += 1
		quad = n**2 + a*n + b
	counter.append(total)

argmax(counter)
counter[1879970]

vals[argmax(counter)]
-61 * 679