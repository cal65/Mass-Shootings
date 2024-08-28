from Euler7 import create_primes
import numpy as np
from itertools import combinations, permutations
import time
from functools import lru_cache


class ListPermutationConcatter():
	def __init__(self, grand_set):
		self.grand_set = set(grand_set)
		self.max_prime = max(self.grand_set)

	def create_concats(self, sub_list):
		perms = permutations(sub_list, 2)
		numbers = tuple(int(str(a) + str(b)) for a, b in perms)
		return numbers
	
	def evaluate_prime(self, n):
		if n > self.max_prime:
			return is_prime(n)
		else:
			return n in self.grand_set

	def evaluate_sub_list(self, sub_list):
		numbers = self.create_concats(sub_list)
		return all(self.evaluate_prime(n) for n in numbers)

def is_prime(n):
	return not any(n % i == 0 for i in range(3, int(n**0.5) + 1, 2)) if n > 2 else False

# primes = create_primes(n=80000)
# primes = np.array(primes)

# perm_concatter = ListPermutationConcatter(primes)

def iterate_groups(n, k=1000, candidates=None):
	## this was a one time pass through function to solve the test but it didn't work
	## it took forever and there were logic flaws in the while loop
	solutions = set()
	for j in range(1, 200):
		if candidates is None:
			candidate_sublist = [primes[j]]
		else:
			candidate_sublist = candidates
		i = j+1
		candidate_index=[]
		while(len(candidate_sublist) < n):
			if i == k:
				candidate_sublist.pop()
				if len(candidate_index) == 0:
					break
				i = candidate_index.pop() + 1
			try:
				p = primes[i]
			except:
				print(i)
				break
			try_sublist = candidate_sublist + [p]
			if perm_concatter.evaluate_sub_list(try_sublist):
				candidate_sublist = try_sublist
				candidate_index.append(i)
			i += 1
		solutions.add(tuple(candidate_sublist))
	return solutions

def try_sublist(candidate_sublist, exclude_set=set(), n=10000, p0 = None, ):
	counter = 0
	if p0 is None:
		p0 = max(candidate_sublist)
	try:
		i0 = np.where(primes == p0)[0][0]
	except Exception as e:
		print(e)
		return p0, primes[-1]
	for i in range(i0+1, n):
		p = primes[i]
		counter += 1
		if p in exclude_set:
			continue
		try_sublist = candidate_sublist + [p]
		if perm_concatter.evaluate_sub_list(try_sublist):
			return try_sublist, exclude_set
		exclude_set.add(p)
		
	return None, exclude_set.copy()

answers = {}
solutions = [[3], [5], [7], [11], [13], [17], [19]]

def iterate_size(solutions, exclude_sets=None, n=1000):
	t0 = time.time()
	if exclude_sets is None:
		exclude_sets = [set()]*len(solutions) 
	iter_answers = []
	counter = 0
	exclude_sets_new = []
	for sublist, exclude_set in zip(solutions, exclude_sets):
		larger_sublist = sublist
		while larger_sublist:
			pmax = max(larger_sublist)
			# see if there are other solutions with a prime larger than pmax
			larger_sublist, exclude_set_sub = try_sublist(sublist, exclude_set=exclude_set, n=n, p0=pmax)
			if larger_sublist:
				# add the solution we found
				iter_answers.append(larger_sublist)
				# add the exclusion set for that solution
				exclude_sets_new.append(exclude_set_sub.copy())
			counter += 1
	print(round(time.time() - t0))
	return iter_answers, exclude_sets_new

# t0 = time.time()
# true_solutions = []
# for p in primes[3:50]:
# 	solutions = [[p]]
# 	print(f"prime: {p}")
# 	answers[2], exclude_sets = iterate_size(solutions, n=4000) # 3 seconds
# 	if answers[2] == [None]:
# 		continue
# 	answers[3], exclude_sets = iterate_size(answers[2], exclude_sets, n=5000) # 
# 	if len(answers[3]) ==0:
# 		continue
# 	answers[4], exclude_sets = iterate_size(answers[3], exclude_sets=exclude_sets, n=9000)  
# 	if len(answers[4]) > 0:
# 		answers[5] = iterate_size(answers[4], exclude_sets=exclude_sets, n=9000)
# 		if len(answers[5]) > 0:
# 			print(answers[5]) 
# 			true_solutions.append(answers[5])

# t1 = time.time()

if __name__ == "__main__":
	primes = create_primes(n=15000)
	primes = np.array(primes)

	perm_concatter = ListPermutationConcatter(primes)
	t0 = time.time()
	true_solutions = []
	for p in primes[2:50]:
		solutions = [[p]]
		print(f"prime: {p}")
		answers[2], exclude_sets = iterate_size(solutions, n=1000) # 3 seconds
		if answers[2] == [None]:
			continue
		answers[3], exclude_sets = iterate_size(answers[2], exclude_sets, n=1000) # 
		if len(answers[3]) ==0:
			continue
		answers[4], exclude_sets = iterate_size(answers[3], exclude_sets=exclude_sets, n=2000)  
		if len(answers[4]) > 0:
			answers[5], exclude_sets_final = iterate_size(answers[4], exclude_sets=exclude_sets, n=3000)
			if len(answers[5]) > 0:
				print(answers[5]) 
				true_solutions.append(answers[5])

	t1 = time.time()
	trues_unlisted = [t for ts in true_solutions for t in ts]
	
