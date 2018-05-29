from decimal import *
import numpy as np
#important for establishing number of digits
getcontext().prec = 3002
#initializing # of repeating digits with 1 for d = 1
rep_digits = [1]
for d in range(2, 1000):
	digits = 0
	x = str(Decimal(1)/Decimal(d))
	if (len(x) > 10 and x[1] == '.'):
		k = 1
		while k < len(x)/2 and digits == 0:
			last = x[-k:]
			second_last = x[-(2*k):-k]
			if (last == second_last):
				digits = len(last)
			k += 1
	rep_digits.append(digits)

rep_digits = np.array(rep_digits)
rep_digits[np.argmax(rep_digits)]

#answer is
