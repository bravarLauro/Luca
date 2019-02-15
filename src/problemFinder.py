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

import subprocess
import sys
import time
from evaluate import transform_into_uci, reformat, arraify, evaluate_sf
from analizer import analize

def main():

	start = time.time()

	gamesInPgn = transform_into_uci(sys.argv[1])

	listOfGames = reformat(gamesInPgn)

	gamesAndMoves = arraify(listOfGames)

	output = evaluate_sf(gamesAndMoves)

	analize(output)

	finish = time.time()
	
	print "TIME ELAPSED: %s s" % (round(finish-start))

if __name__ == "__main__":
    main()