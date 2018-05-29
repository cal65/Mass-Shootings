from math import *
import numpy as np
import pandas as pd
factors = []
for value in range(5, 10000):
	#1 is a factor for everyone
	current_set = [1]
	for i in range(2, int(pow(value, .5))+1):
		if value % i ==0:
			current_set.append(i)
			current_set.append(value // i)
	factors.append(np.unique(current_set))

d = [sum(f) for f in factors]
pair = []
for i in range(5, 10000):
	pair.append(sorted([i, d[i-5]]))
pair = pd.Series(pair)
#lists are unhashable, need to convert to tuple
pair_counts = pair.apply(tuple).value_counts()

amicable = pair_counts[pair_counts.ge(2)]
amicable_sum = 0
for i in amicable.index:
	amicable_sum += sum(i)

#pd.Series([tuple([i + j]) for i in range(6, 20) , j in d])

	#factors.append(list(np.unique([i, value//i] for i in range(2, int(pow(value, .5)) + 1) if value % i == 0)))