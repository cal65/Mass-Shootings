import math

def extract_digits(n):
	string_list = list(str(n))
	int_list = [int(i) for i in string_list]
	return(int_list)

answers = []
for n in range(3, 100000):
	digits = extract_digits(n)
	factorial_sum = sum([math.factorial(i) for i in digits])
	if factorial_sum == n:
		answers.append(n)