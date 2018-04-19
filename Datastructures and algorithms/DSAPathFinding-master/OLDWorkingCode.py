	def findLeastResistance(self, r, c, matrix, altitude):
		"""
		r : row
		c : column
		Returns 1 / -1 / 0 for up/down/right
		"""

		downVal = matrix[r + 1][c + 1]
		straightVal = matrix[r][c + 1]
		upVal = matrix[r - 1][c + 1]

		##########################################
		downDiff = altitude - downVal
		straightDiff = altitude - straightVal
		upDiff = altitude - upVal

		options = [downDiff, straightDiff, upDiff]
		##########################################
		leastResistance = min(options, key=abs)

		if options[0] == leastResistance:
			return 1  # go down

		if options[1] == leastResistance:
			return 0  # go forward

		if options[2] == leastResistance:
			return -1  # go up

		return None

    # Above gave 16km best result! Greedy algo looking 1 step ahead


		altitude = matrix[r][c]

		downVal = matrix[r + 1][c + 1]
		straightVal = matrix[r][c + 1]
		upVal = matrix[r - 1][c + 1]

		##########################################
		downDiff = altitude - downVal
		straightDiff = altitude - straightVal
		upDiff = altitude - upVal

		options = [downDiff, straightDiff, upDiff]

		##########################################
		leastResistance = min(options, key=abs)

		if options[0] == leastResistance:
			return 1  # go down

		if options[1] == leastResistance:
			return 0  # go forward

		if options[2] == leastResistance:
			return -1  # go up

		return None
