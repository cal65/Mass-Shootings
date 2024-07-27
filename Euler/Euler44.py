import pandas as pd
import numpy as np
import itertools
import time

def pentagon(n):
    p = n * (3*n-1)/2
    return p


def combinations(n):
    combinations = itertools.combinations(list(range(1, n)), 2)
    return list(combinations)

def pentagon_list(n):
    plist = [pentagon(i) for i in range(n)]
    return plist

def pentagon_arithmetics(n):
    t0 =time.time()
    clist = combinations(n)
    matches = []
    plist = pentagon_list(n)
    for i in range(len(clist)):
        plow = pentagon(clist[i][0])
        phigh = pentagon(clist[i][1])
        psum = plow + phigh
        pdiff = phigh - plow
        if (psum in plist):
            print(clist[i])
            if pdiff in plist:
                matches.append(clist[i])
        if i % 10000 == 0:
            print(i)
            print (round(time.time() - t0),2)
    print ('Time: ' + str(round(time.time() - t0),2))
    return matches