from circle import Circle
from point import Point
from time import time

class Bullet( Circle ):
	
	#Constructor
	def __init__( self, x, y, rad, rot ):
		super().__init__(x, y, rad, rot)

		self.accelerate(10)
		self.ticks = 0
		self.timeCreated = time()

