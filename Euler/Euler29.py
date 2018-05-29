from math import *
import numpy as np
import pandas as pd
import itertools

start = 2
end = 100
vals = list(itertools.product(range(start,end + 1), repeat=2))
sequence = []
for val in vals:
	a = val[0]
	b = val[1]
	sequence.append(a**b)

sequence.sort()
sequence_unique = np.unique(sequence)
len(sequence_unique)