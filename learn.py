""" Running through a python tutorial; this is a google-conventionalized docstring

Usage: 
	Call main

Attributes:
	Google docstring guide: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
"""

import sys
from urllib.request import urlopen

def print_word_count(url):
	""" Prints a count of words taken from a web resource ident'd by URL
	 	Try https://www.gutenberg.org/cache/epub/47529/pg47529.txt, for example
	"""
	wc = {}
	with urlopen(url) as story:
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				wc.setdefault(word, 0)
				wc[word] += 1
	
	most_used = 0
	most_used_word = ''
	for word_key in wc:
		if(wc[word_key] > most_used):
			most_used = wc[word_key]
			most_used_word = word_key

	print('{} is used {} times'.format(most_used_word, wc[most_used_word]))


if __name__ == '__main__':
		print_word_count(sys.argv[1])