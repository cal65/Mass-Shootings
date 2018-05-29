from math import *
import numpy as np
import pandas as pd
import itertools
factors = []
ceil_val = 28123 - 12
for value in range(12, ceil_val):
	#1 is a factor for everyone
	current_set = [1]
	for i in range(2, int(pow(value, .5))+1):
		if value % i ==0:
			current_set.append(i)
			current_set.append(value // i)
	factors.append(np.unique(current_set))

d = [sum(f) for f in factors]
#store all integers and 
df = pd.DataFrame({'Integer': range(12, ceil_val), 'Sum': d})
#this 
abundant = df[df['Sum'] > df['Integer']]
#find all combinations, include the sum of an abundnat with itself, hence the need for _with_replacement
perms = list(itertools.combinations_with_replacement(abundant['Integer'], 2))
#for all these combinations, calculate their sum
perm_sums = [sum(i) for i in perms]

#the problem asks to find non sums
all_non_sums = list(set(range(1,28123)) - set(perm_sums))
#this is the answer
sum(all_non_sums)
4179871