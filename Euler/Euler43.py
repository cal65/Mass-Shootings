import pandas as pd
import numpy as np


## substrings
## The number 1406357289 is a 0 to 9 pandigital number because it is made up of each of the digits 
#  0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, 
#  d2 be the 2nd digit, and so on. In this way, we note the following:

#  is divisible by 
#  is divisible by 
#  is divisible by 
#  is divisible by 
#  is divisible by 
#  is divisible by 
#  is divisible by 
# Find the sum of all 
#  to 
#  pandigital numbers with this property.

def number_to_array(n):
	n_str = str(n)
	n_list = list(n_str)
	return n_list

def array_to_number(a):
	if not isinstance(a, list):
		raise Exception("a must be a list")
		return
	digits = len(a)
	n = 0
	for i in range(digits):
		n += int(a[i]) * 10 ** (digits - i - 1)
	return n

def evaluate_divisible(n, factor):
	return n % factor == 0


primes = [2, 3, 5, 7, 11, 13, 17]

def get_pandigitals():
	digits = [str(i) for i in  range(10)]
	perms = permutation(digits)
	pan_digitals = [array_to_number(p) for p in perms]
	return pan_digitals


def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l


def evaluate_pandigital(n):
	for i in range(0, 7):
		digit = i+1
		value = array_to_number(number_to_array(n)[digit: digit+3])
		if not evaluate_divisible(value, primes[i]):
			return False
	return True


def find_pandigitals():
	ps = get_pandigitals()
	answers = []
	for p in ps:
		if len(str(p)) != 10:
			continue
		if p == 1023546978:
			print(p)
		if evaluate_pandigital(p):
			answers.append(p)
	return answers



