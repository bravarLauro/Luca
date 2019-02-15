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

import re
import subprocess
import time

def transform_into_uci(file_with_games):

	arg_for_bash = "-f" + file_with_games
	p = subprocess.Popen(["pgn-extract", arg_for_bash,"-Wuci","-C"], stdout=subprocess.PIPE)
	out, err = p.communicate()

	return out

def reformat(gamesInPgn):

	a = gamesInPgn
	b = re.sub('\[.*\]','',a)
	c = re.sub('\n+','\n',b)
	d = re.sub('1-0\n|0-1\n|1/2-1/2\n','GAME',c)

	listOfGames = d.split('GAME')
	listOfGames.pop()

	return listOfGames

def arraify(listOfGames):

	gamesAndMoves = []
	for game in listOfGames:
		a = game.split(' ')
		a.pop()
		gamesAndMoves.append(a)
	gamesAndMoves[0][0] = gamesAndMoves[0][0].split("\n")[1]

	return gamesAndMoves

def evaluate_sf(gamesAndMoves):

	gameCounter = 0
	output = ""

	for game in gamesAndMoves:
		gameCounter = gameCounter + 1
		output = output + "GAME" + str(gameCounter)
		movex = ""

		for move in game:
			movex = movex + " " + move
			p = subprocess.Popen(["../Stockfish/src/script.sh", movex], stdout=subprocess.PIPE)
			out, err = p.communicate()
			out2 = out.split("uciok\n")[1]
			e = out2.split("\n")
			e.pop()
			e.pop()

			for element in e[:-1]:
				m = re.search('info depth\ (.+?)\ ', element)
				n = re.search('score\ (.+?)\ nodes', element)

				try:
					output = output + m.group(1) + " " + n.group(1) + "\n"
				except:
					pass

			output = output + e[-1] + "\n"
			
	return output
