from numpy import *

factors = []
for i in arange(1, 1000):
	if i % 3 == 0 or i % 5 == 0 :
		factors.append(i)

sum(factors)