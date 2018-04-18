from polygon import Polygon
from point import Point
from random import randint

class Asteroid( Polygon ):
	def __init__(self):


		super().__init__(x=randint(10,640), y=randint(10,480), rotation=0)

		self.points = [  Point(-30,0), Point(-10,40), Point(40,0), Point(-20,-20)]

		super().accelerate(1.75)
		#self.pull = Point(0.02,0.02)
		self.angular_velocity = 0.1
		self.pull = Point(randint(-4,4), randint(-4,4))
