from numpy import *
from matplotlib.pyplot import *

primes = arange(2,2000001)

i=0
num=0
while num < sqrt(2000000):
	num = primes[i]
	primes = primes[((primes % num != 0) | (primes == num)).nonzero()]
	i += 1