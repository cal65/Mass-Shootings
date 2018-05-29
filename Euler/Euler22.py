import pandas as pd
import string
names = pd.read_csv('p022_names.txt', sep=',', header=None, index_col=False, squeeze=True, keep_default_na=False)
#pandas doesn't read in series very well
names = names.transpose()[0]
names[names.isnull()]
names_alphabetical = sorted(names)
#originally, one of the names is a nan, which because the first element in names_alphabetical

alphabet_dict = {}
for n in range(1, 27):
	alphabet_dict[string.ascii_uppercase[n-1]] = n

letter_sum=0
for i in range(0, len(names_alphabetical)):
	name = names_alphabetical[i]
	for letter in name:
		letter_sum += (i+1) * alphabet_dict[letter]