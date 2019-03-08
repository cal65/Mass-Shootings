answers = []

def num_digit(n):
	return len(str(n))

full_set = [str(i) for i in range(1, 10)] #answers to compare to
for a in range(1, 1000):
	a_digits = num_digit(a)
	#the product of a x digit and y digit number is either (x+y-1) 
	#or (x+y) digits
	#we need x + y + (x + y) to equal 9
	#i.e. 2x + 2y = 9, y = 4.5-x
	b_range = [10**(3-a_digits), 10**(5-a_digits)] 
	for b in range(b_range[0], b_range[1]):
		c = a * b
		raw_combined = "".join([str(i) for i in [a,b,c]]) #one long string
		letters = list(raw_combined)
		unique_letters = sorted(set(letters))
		if unique_letters == full_set and len(letters) == 9:
			answers.append([a, b, c])

cs = [el[2] for el in answers]
products = np.unique(cs)