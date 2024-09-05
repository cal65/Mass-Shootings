import numpy as np
import pandas as pd
import itertools as it 

cubes = [i**3 for i in range(300, 50000)]   

def reorder(n):
	str_list = list(str(n))
	str_list.sort()
	lowest_str = ''.join(str_list)
	return lowest_str

cube_dict = {}
for cube in cubes:
	cube_dict[cube] = [reorder(cube)]

# eh, use pandas because I'm too lazy to rewrite value counts
reorder_df = pd.DataFrame(cube_dict).T 
reorder_df.reset_index(inplace=True)   
# reorder df will have duplicates in 0 column where the lowest str is same amongst cubes
counts_df = pd.DataFrame(reorder_df[0].value_counts()) 

def get_options(counts_df, reorder_df, n):
	options = counts_df.loc[counts_df[0] == n].index
	originals = reorder_df.loc[reorder_df[0].isin(options)]['index']
	return originals.min()

get_options(counts_df, reorder_df, 5) 