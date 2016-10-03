from numpy import *

prod_a = arange(901, 1000).repeat(100)
prod_b = arange(901, 1000)
for i in range(1, 100):
	prod_b = concatenate((prod_b, arange(901, 1000)))

#outer would work as well
products = unique(prod_a * prod_b)
for i in range(0, len(products)):
	answer = list(str(products[i]))
	answer_rev = answer[::-1]
	if answer == answer_rev:
		print i
