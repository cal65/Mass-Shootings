import numpy as np
import decimal

# Set the precision to 60 digits
decimal.getcontext().prec = 60


# Example usage
N = 30

def get_e_sequence_n(n):
	if n%3 ==2:
		return (n+1)/3 *2
	else:
		return 1

def e_arithmetic_sequence(n):

	last_fraction = 1/get_e_sequence_n(n)
	while n > 1:
		last_fraction = 1 /(get_e_sequence_n(n-1) + last_fraction)
		n = n-1
	e_sum = 2 + last_fraction
	return e_sum


def get_fraction(v, start, end):
	for denom in range(start, end):
		nom = v*denom
		if (np.isclose(nom, int(nom), atol=1e-10)):
			return nom, denom
	return False


# there's a pattern
def numerator_sequence(n):
	numerators = [2, 3]
	for i in range(2, n):
		numerators.append(numerators[i-1] * get_e_sequence_n(i) + numerators[i-2])
	return numerators


 def digit_sum(num): 
 	sum = 0
 	while num > 0: 
 		sum = sum + (num % 10)
 		num = num // 10
 		return sum 

 