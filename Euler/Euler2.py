from numpy import *

fibonnaci = [1]

x= 1

i = 2
while (x < 4000000):
	fibonnaci.append(x)
	x = fibonnaci[i-1] + fibonnaci[i-2]
	i=i+1

even_fibs = array(fibonnaci)
even_fibs = even_fibs.compress(even_fibs % 2 == 0)
sum(even_fibs)