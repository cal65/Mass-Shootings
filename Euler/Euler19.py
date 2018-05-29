from datetime import *
#using datetime, this is easy
sundays = 0
#iterate through all the years of the 20th century
for year in range(1901, 2001):
	for month in range(1,13):
		month_start = date(year, month, 1)
		if month_start.weekday() == 6:
			sundays += 1

#171