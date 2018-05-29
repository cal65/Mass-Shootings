from numpy import *

fibonnaci = [1]

x= 1

i = 2
while (len(str(x)) < 1000):
	fibonnaci.append(x)
	x = fibonnaci[i-1] + fibonnaci[i-2]
	i=i+1

x
#answer is
len(fibonnaci)+1