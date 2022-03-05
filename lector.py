import functools
import math
'''
making some changes on this projecgt
que mas ombe herber.


'''
def calc_avg(list):
	sum = functools.reduce(lambda a, b: a + b, list)
	return sum / len(list)

def calc_sd(list):
	diffs = []
	avg = calc_avg(list)
	for val in list:
		diff = val - avg
		diffs.append(diff * diff)
	avg_diffs = calc_avg(diffs)
	return math.sqrt(avg_diffs)


def run():
	file_path = 'reader.csv'
	rows = []
	list_from_file = []
	with open(file_path) as file:
		rows = file.readlines()
	for row in rows:
		row = [ int(val) for val in row.split(',') ]
		avg = calc_avg(row)
		sd = calc_sd(row)
		list_from_file.append([ row, avg, sd ])

	print(list_from_file)

if __name__ == '__main__':
	run()
