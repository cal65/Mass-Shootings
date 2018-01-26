import numpy as np

collatz = list()
for i in range(2, 1000000):
	value = i
	sequence = []
	while(value != 1):
		sequence.append(value)
		if value % 2 == 1:
			value = value * 3 + 1
		elif value % 2 == 0:
			value = value /2
	collatz.append(sequence)

longest = max(collatz, key=len)