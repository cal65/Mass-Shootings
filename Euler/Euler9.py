from numpy import *

a = outer(arange(1,1001), repeat(1,1000))
a = a.flatten('F')
b = arange(1, 1001).repeat(1000)
c = 1000-(a+b)

X = array(zip(a,b,c))
X[a**2 + b**2 == c**2,]
Y = X[(X[:,2] > 0).nonzero(),]
375 * 200 *425