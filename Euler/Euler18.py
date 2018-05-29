import numpy as np

rows = []
with open('Euler18.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])

treeCopy = rows
height = len(rows)
for i in range(1, height):
	current = height-i - 1
	rowSums = []
	for j in range(0, len(rows[current])):
		rowSums.append(max(rows[current][j] + treeCopy[current+1][j], treeCopy[current][j] + treeCopy[current+1][j+1]))
	treeCopy[current] = rowSums
#tree copy now contains the max sum of each branch, and top ndoe represents answer