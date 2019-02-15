"""
	Author: Lauro Bravar Abril-Martorell
	Date: 12-08-2017
	-----------------------------------------------
	Program developed to find chess tactic problems
	from a given set of games given by the user.
	-----------------------------------------------
	This software was developed as a project for 
	Universidad Carlos III de Madrid.
"""

import math
import re

def analize(output):

	games = output.split("GAME")

	for a in games:

		if a:
			print "game " + a[0] + a[1]

		b = a.split("bestmove ")
		g = []
		for c in b:
			d = c.split("\n")
			g.append(d)

		counter = 0
		for h in g[:-1]:

			counter = counter + 1
			try:
				# Below lies the definition 
				# of the problems that you seek
				re.search("mate",a)
				h1=int(h[1].split("cp ")[1])
				h7 = re.search("mate", h[7])
				if math.fabs(h1)<500 and h7:
					print "PLY: " + str(counter)

			except IndexError:
				pass