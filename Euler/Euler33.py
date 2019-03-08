answers = []

for a in range(10, 100):
	for b in range(a+1, 100):
		frac = a/b
		a_digits, b_digits = list(str(a)), list(str(b))
		inter_digit = set(a_digits).intersection(b_digits)
		if len(inter_digit) > 0:
			dig = inter_digit.pop()
			if dig != '0':
				a_digits.remove(dig) 
				b_digits.remove(dig)
				if (b_digits[0] != '0'):
					new_frac = int(a_digits[0])/int(b_digits[0])
					if frac == new_frac:
						answers.append([a,b])
