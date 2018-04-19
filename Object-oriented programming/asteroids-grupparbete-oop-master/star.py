from circle import Circle
import random

class Star(Circle):
    """
    Star extends the Circle class to create stars.
    A Star has a position, a radius, and an rotation (yes, really!)
    """
    def __init__(self):
        # create star at random position of x and y in the screen size
        super().__init__(x=random.randint(1,640), y=random.randint(1,480), r=4, rotation=1 )
        self.linewidth = 2