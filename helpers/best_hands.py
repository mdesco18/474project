"""
best_hands.py
"""

import random
import os
import sys


def main():

	file = sys.argv[1]
	infile = os.path.abspath(file)
	max = 0
	with open(infile) as f:
		lines = f.readlines()
	
	for line in lines:
		line = line.split()
		#print(line)
		#print(line[-1])
		if float(line[-1]) > max:
			max = float(line[-1])
			hand = "".join(line)
			print(hand)
			print(max)
	print(hand)
	print(max)
if __name__ == '__main__':
	main()
