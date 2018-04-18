from polygon import Polygon
from point import Point
import random

class Ship( Polygon ):
	def __init__(self):

		# Start ship in the middle of the screen
		super().__init__(x=640/2, y=480/2)


		self.points = [ Point(0,0), Point(-10,10), Point(15,0), Point(-10,-10) ]