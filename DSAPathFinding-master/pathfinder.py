import sys, math, random

class Pathfinder:
	def __init__(self, visualiser, map):
		self._visualiser = visualiser
		self._map = map
		
		self.nextSteps = []
		self.indexErrors = 0

	def findCheapestPath(self):

		# Mark's silly algorithm for finding the cheapest path:
		#   Use random logic - virtually gauranteed to give the correct answer
		#   eventually if we just run it enough times.
		#   NOTE: Since problem is NP-hard - we won't know for sure that it is
		#         the correct answer when we get it which is a bummer.

		# Starting at a random position on the left:

		lowestCost = 100000
		improvedCostTimes = 0
		for startingR in range(10, 480):
			#starting_row = random.randint( 10, self._map.getHeight() )
			(cost, path) = self.findPath(startingR)
			#print("Starting row: ", startingR, "Cost: ", cost)
			if cost < lowestCost:
				#print("Went in here!")
				lowestCost = cost
				bestPath = path
				self._visualiser.setBestPath(bestPath)
			self._visualiser.addPath(path)

		# Search for one random path:
		#( cost, path ) = self.findPath( starting_row )

		# It is the only path we have found, visualise it:
		#self._visualiser.addPath(path)

		# The only path so it must also be the best path, visualise that:
		#self._visualiser.setBestPath(path)

		# And the cost of this so called "best" path:
		print("Number of times improved: ", improvedCostTimes)
		self._visualiser.setBestPathCost( lowestCost )

		# What next?  Can you do better than random?
		# TODO:  Step 1 - a greeedy algorithm from a random starting position
		# TODO:  Step 2 - best greedy of all possible starting positions
		# TODO:  Step 3 - improve even more!
		return


	def findLeastResistance(self, r, c, matrix):
		"""
		r : row
		c : column
		Returns 1 / -1 / 0 for up/down/right
		"""

		current_alti = matrix[r][c]
		minCostEnc = 9999999
		bestPathEnc = []
		# Arrays holding the sequence of steps taken,
		firstPath1 = [-1, -1]
		firstPath2 = [-1, 0]
		firstPath3 = [-1, 1]

		secondPath1 = [0, -1]
		secondPath2 = [0, 0]
		secondPath3 = [0, 1]

		thirdPath1 = [1, -1]
		thirdPath2 = [1, 0]
		thirdPath3 = [1, 1]

#FirstPath1########################################
		tmpCost = 0
		tmpCost += abs(matrix[r-1][c+1] - current_alti)
		new_alti = matrix[r-1][c+1]
		tmpCost += abs(matrix[r-2][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 254
			minCostEnc = tmpCost
			bestPathEnc = firstPath1
#FirstPath2########################################
		tmpCost = 0
		tmpCost += abs(matrix[r-1][c+1] - current_alti)
		new_alti = matrix[r-1][c+1]
		tmpCost += abs(matrix[r-1][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 91
			minCostEnc = tmpCost
			bestPathEnc = firstPath2
#FirstPath3########################################
		tmpCost = 0
		tmpCost += abs(matrix[r-1][c+1]) - current_alti
		new_alti = matrix[r-1][c+1]
		tmpCost += abs(matrix[r+0][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 256
			minCostEnc = tmpCost
			bestPathEnc = firstPath3
#SecondPath1########################################
		tmpCost = 0
		tmpCost += abs(matrix[r+0][c+1] - current_alti)
		new_alti = matrix[r+0][c+1]
		tmpCost += abs(matrix[r-1][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 109
			minCostEnc = tmpCost
			bestPathEnc = secondPath1
#SecondPath2########################################
		tmpCost = 0
		tmpCost += abs(matrix[r+0][c+1] - current_alti)
		new_alti = matrix[r+0][c+1]
		tmpCost += abs(matrix[r+0][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 342
			minCostEnc = tmpCost
			bestPathEnc = secondPath2
#SecondPath3########################################
		tmpCost = 0
		tmpCost += abs(matrix[r+0][c+1] - current_alti)
		new_alti = matrix[r+0][c+1]
		tmpCost += abs(matrix[r+1][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 290
			minCostEnc = tmpCost
			bestPathEnc = secondPath3
#ThirdPath1########################################
		tmpCost = 0
		tmpCost += abs(matrix[r+1][c+1] - current_alti)
		new_alti = matrix[r+1][c+1]
		tmpCost += abs(matrix[r+0][c+2] - new_alti)
		if tmpCost < minCostEnc: # at row 10, tmpCost should be: 256
			minCostEnc = tmpCost
			bestPathEnc = thirdPath1
#ThirdPath2########################################
		tmpCost = 0
		tmpCost += abs(matrix[r+1][c+1] - current_alti)
		new_alti = matrix[r+1][c+1]
		tmpCost += abs(matrix[r+1][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 204
			minCostEnc = tmpCost
			bestPathEnc = thirdPath2
#ThirdPath3########################################
		tmpCost = 0
		tmpCost += abs(matrix[r+1][c+1] - current_alti)
		new_alti = matrix[r+1][c+1]
		tmpCost += abs(matrix[r+2][c+2] - new_alti)
		if tmpCost < minCostEnc:  # at row 10, tmpCost should be: 188
			minCostEnc = tmpCost
			bestPathEnc = thirdPath3

		return bestPathEnc


	def findPath(self, starting_row):
		# Code to find one path from left to right through the map
		# And return the total "cost" and path
		# Current finds only a random path - can you make it better?

		matrix = self._map.getMatrix()
		rows = self._map.getHeight()
		cols = self._map.getWidth()

		row = starting_row

		cost = 0
		col=0
		path=[ row ]


		while col+1 < cols:
			# how high are we right now?
			current_altitude = matrix[row][col]

			# Pick a random direction - up/right,  right,  down/right
			#r = random.randint(-1,1)
			if len(self.nextSteps) == 0:
				try:
					self.nextSteps = self.findLeastResistance(row, col, matrix)
				except IndexError:
					self.nextSteps = [0]
					self.indexErrors += 1
				
			
			direction = self.nextSteps[0]
			del self.nextSteps[0]

			#secondDirection = self.findLeastResistance(row, col+1, matrix)

			#thirdDirection = self.findLeastResistance(row+1, col+1, matrix)
			#fourthDirection = self.findLeastResistance(row-1, col+1, matrix)
			
			row += direction
			if row < 0:
				row = 0
			if row > rows-1:
				row = rows-1
			col += 1

			# how high are we now?
			new_altitude = matrix[row][col]

			# change in height:
			delta = int( math.fabs( new_altitude - current_altitude ) )

			# cost is the absolute change in height per step
			cost += delta

			# add this step to the path we are following
			path.append( row )

		print("Errors encountered: ", self.indexErrors)
		return ( cost, path )

