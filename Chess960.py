#Chess960 row generator. This generates white, black is mirrored.
#Rules: King between rooks, bishops on different colors.
#Black: 0, 2, 4, 6
#White: 1, 3, 5, 7

import sys, random

class gen960(object):
	def __init__(self):
			self.mainRow = [0 for x in range(8)]

	def rookTest(self, row, rookLocation):
		rookBool = False
		kingOpenings = []
		for x in range(rookLocation[0] + 1, rookLocation[1]):
			if row[x] == 0:
				rookBool = True
				kingOpenings.append(x)
		return(rookBool, kingOpenings)

	#generates row

	#generate white bishop 1, 3, 5, 7
	#then black bishop. 0, 2, 4, 6
	#generate first rook, generate second rook, ensuring they're at least 1 apart. 
	#generate king between rooks
	#generate rest
	def generate(self):
		self.__init__()
		inRow = self.mainRow
		
		#white bishop, 8 open squares
		rando = random.randint(1, 4) * 2 - 1
		inRow[rando] = "B"
		
		#black bishop, 7 open squares
		rando = random.randint(0, 3) * 2
		inRow[rando] = "B"
		#rooks, 6 open squares

		rookLoc = [0, 0]
		while True:
			rookLoc[0] = random.randint(0, 7)
			rookLoc[1] = random.randint(0, 7)
			rookLoc.sort()
			tester = self.rookTest(inRow, rookLoc)
			if inRow[rookLoc[0]] == 0 and inRow[rookLoc[1]] == 0 and tester[0]:				
				inRow[rookLoc[0]] = "R"
				inRow[rookLoc[1]] = "R"
				break

		#King, 4 open squares
		rando = random.randint(0, len(tester[1]) - 1)
		inRow[tester[1][rando]] = "K"

		tracker = []
		for x in range(8):
			if inRow[x] == 0:
				tracker.append(x)

		#Queen, 3 open squares
		rando = random.randint(0, 2)
		inRow[tracker[rando]] = "Q"
		tracker.remove(tracker[rando])

		#Knights, 2 open squares
		inRow[tracker[0]] = "N"
		inRow[tracker[1]] = "N"

		self.mainRow = inRow

	def rowID(self, row):
		idDict = {}
		fIN = open('c960id.txt', 'r')
		f = fIN.readlines()
		for x in f:
			y = x.split(' ')
			idDict[y[1].rstrip('\n')] = y[0]
		fIN.close()
		strRow = ''.join(row)

		return(idDict[strRow])
	

	def printRow(self, spid):
		row = self.mainRow
		print("\nRow ID: ", spid)
		for y in range(0, 8):
			print(row[y], " ", end="")
		print("\n")

# row = gen960()
# uniqueRow = []
# wrongCount = 0
# for x in range(100000):
# 	row.generate()
# 	if row.mainRow in uniqueRow:
# 		wrongCount += 1
# 	else:
# 		uniqueRow.append(row.mainRow)
# print("Number of unique rows generated: ", len(uniqueRow))
# print("Number of duplicate rows generated: ", wrongCount)

row = gen960()
while True:
	row.generate()
	spid = row.rowID(row.mainRow)
	row.printRow(spid)
	i = input("Press Enter to generate, q to quit: ")
	if i == 'q':
		break
