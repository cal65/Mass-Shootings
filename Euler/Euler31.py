from math import *
import numpy as np
import pandas as pd
import itertools

vals = list(itertools.product(range(0,8), repeat=range(2, 20)))

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
permutations = [0]*(target+1)
permutations[0] = 1
for c in coins:
	for i in range(c, target+1):
		permutations[i] += permutations[i-c]

permutations[target]