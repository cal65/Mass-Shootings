import csv
from numpy import *

rows = []

with open('Euler11_grid.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		rows.append(row)

side = []
for i in range(0, len(rows)):
	side.append([])
	for j in range(0, len(rows[i]) - 3):
		side[i].append(reduce(lambda x, y: x*y, map(int, rows[i][j:j+4])))

max(amax(side, axis=0))

nd_rows = asarray(rows).astype(int)
vert = []
for i in range(0, len(rows)):
	vert.append([])
	for j in range(0, len(rows[i]) - 3):
		vert[i].append(reduce(lambda x, y: x*y, nd_rows[:,i][j:j+4]))

diag = []
for i in range(0, len(rows) - 4):
	diag.append([])
	for j in range(0, len(rows[i]) - 4):
		diag[i].append(nd_rows[i,j] * nd_rows[i+1, j+1] * nd_rows[i+2, j+2] * nd_rows[i+3, j+3])

diag2 = []
for i in range(len(rows)-1, 2, -1):
	diag2.append([])
	for j in range(0, len(rows[i])-4):
		diag2[19-i].append(nd_rows[i,j] * nd_rows[i-1, j+1] * nd_rows[i-2, j+2] * nd_rows[i-3, j+3])

amax(max(amax(side, axis=0)) , amax(vert, axis=0), amax(diag, axis=0))
