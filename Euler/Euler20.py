from math import *
big_factor = factorial(100)
big_sum = 0
for digit in str(big_factor):
	big_sum += int(digit)