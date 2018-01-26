import numpy as np
import pandas as pd
df = pd.read_table('Euler13.txt', sep='\n', header= None)
numbers = df.iloc[:,0]
truncated = []
for num in numbers:
	truncated.append(int(num[0:12]))


str(sum(truncated))[:10]