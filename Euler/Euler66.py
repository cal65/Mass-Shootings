import pandas as pd
import numpy as np

def quadratic(a, b, c):
	return [-b + np.sqrt(b*b - 4*a*c)/2, -b - np.sqrt(b*b - 4*a*c)/2]


def solve_diophantine(d, x):
	solutions = quadratic(-d, 0, x*x-1)
	return solutions

def is_square(number: int) -> bool:
    floor = int(math.sqrt(number))
    return floor**2 == number

    