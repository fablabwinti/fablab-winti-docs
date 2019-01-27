#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import subprocess
import difflib
import re

def main(filename):
	oldlines = subprocess.check_output(['git', 'show', 'HEAD:./' + filename]).splitlines(True)
	with open(filename, 'rb') as f:
		newlines = f.readlines()
	outlines = newlines[:]
	
	# for matching, ignore leading/trailing whitespace and ItemIDs
	spacere = re.compile('^\\s+|\\s+$')
	itemidre = re.compile('\\bItemID="[^"]*"')
	oldlinesmatch = [itemidre.sub('ItemID=""', spacere.sub('', l)) for l in oldlines]
	newlinesmatch = [itemidre.sub('ItemID=""', spacere.sub('', l)) for l in newlines]
	
	# process one pair of matched lines: copy ItemID if both have one
	def process(oldlineno, newlineno):
		oldid = itemidre.search(oldlines[oldlineno])
		newid = itemidre.search(newlines[newlineno])
		if oldid and newid:
			outlines[newlineno] = newid.string[:newid.start()] + oldid.group() + newid.string[newid.end():]
	
	differ = difflib.SequenceMatcher(a = oldlinesmatch, b = newlinesmatch)
	oldb = newb = 0
	for olde, newe, size in differ.get_matching_blocks():
		# [oldb:olde] and [newb:newe] are differing lines
		#print(' diff', oldb, olde, newb, newe)
		if olde - oldb == 1 and newe - newb == 1:
			linediffer = difflib.SequenceMatcher(a = oldlinesmatch[oldb], b = newlinesmatch[newb])
			if linediffer.ratio() >= 0.6:
				process(oldb, newb)
		else:
			# TODO match them up by similarity
			if olde != oldb or newe != newb:
				print('TODO multi-line mismatch [{}:{}] [{}:{}]'.format(oldb, olde, newb, newe))
		# [olde:olde+size] and [newe:newe+size] are matching lines
		#print('match', olde, olde+size, newe, newe+size)
		for i in range(size):
			process(olde+i, newe+i)
		oldb = olde + size
		newb = newe + size
	
	try:
		os.remove(filename + '.bak')
	except OSError as e:
		pass
	os.rename(filename, filename + '.bak')
	with open(filename, 'wb') as f:
		for line in outlines:
			f.write(line)

if __name__ == '__main__':
	main(sys.argv[1])
