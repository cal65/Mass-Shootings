from math import *
import numpy as np
import pandas as pd

dimension = 1001

main = np.zeros((dimension, dimension))

def formula(a, b, c, d):
	return [a + b + c + d, a*2**3 + b*2**2 + c*2 + d, a*3**3 + b*3**2 + c*3 + d, a*4**3 + b*4**2 + c*4 + d]