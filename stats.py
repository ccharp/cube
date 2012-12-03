#!/usr/bin/python
from collections import defaultdict
import matplotlib.pyplot as plt

# Returns a dictionary of converted mana costs as keys, and
# lists of cards with those CMCs as values.
def get_cmc_dict( filename ):
	file = open( filename )
	cmc = defaultdict( list )
	cost = 0
	for line in file:
		line = line.rstrip()
		if not line:
			continue
		if '#' in line:
			if '# CMC' in line:
				if line.split()[-1] == 'X':
					cost = 'X'
				else:
					cost = int( line.split()[-1] )
			continue
		cmc[cost].append( line )
	return cmc

def show_cmc_plot():
	filenames = ['white', 'blue', 'black', 'red', 'green', 'colorless']
	for name in filenames:
		cmc = get_cmc_dict( name )
		counts = [0] * 15
		for key in sorted( cmc.keys() ):
			if key is not 'X':
				counts[int( key )] = len( cmc[key] )
		print name, sum( counts ) + len( cmc['X'] )
		color = name
		if color is 'colorless':
			color = 'grey'
		if color is 'white':
			color = 'yellow'
		plt.plot( counts, c=color )
	plt.show()

if __name__ == '__main__':
	show_cmc_plot()

