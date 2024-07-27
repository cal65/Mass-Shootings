from numpy import *
import itertools
import time

primes = [i for i in range(2,4)]
not_prime = set()
t = time.time()
num = 3
lim_num = 1000000
	#check if num is in not prime
for i in range(num, lim_num, 2):
	if i in not_prime:
		continue
	#everything multiplied by 3, and then counting by i*2 will also be in not_prime
	for j in range(i*3, lim_num, i*2):
		not_prime.add(j)
	primes.append(i)
print(time.time() - t)

def circulate(n):
	string_n = list(str(n))
	rotations = []
	for i in range(0, len(string_n) -1): #the -1 is a bit of a trick
	#because we will run this on primes, and we know the original input is prime
		string_n.append(string_n.pop(0))
		rotations.append(string_n.copy())
	joined_rotations = [''.join(map(str,p)) for p in rotations] 
	unique_joined = list(unique(joined_rotations))
	unique_ints = [int(p) for p in unique_joined]
	return unique_ints

answers = []
for p in primes:
	not_all = True
	for c in circulate(p):
		if c not in primes:
			not_all = False
			continue
	if not_all: answers.append(p)

print(time.time() - t)

#answer
len(answers)