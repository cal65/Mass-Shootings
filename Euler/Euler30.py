from math import *
import numpy as np
import pandas as pd
import itertools

upper = (9**5)*7
#because the max sum of the 5th power of digits of a 7 digit number would be a 6 digit number, we can stop at all 6 digit numbers 

answers = []
for i in range(2, 1000000):
	characters = str(i)
	sum_fifth = 0
	for c in characters:
		sum_fifth += int(c)**5
	if (sum_fifth == i):
		answers.append(i)

sum(answers)
443839