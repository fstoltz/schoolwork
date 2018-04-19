from LinkedList import LinkedList



class Stack( LinkedList ):

	def __init__(self):
		super().__init__()


	def push(self, val):
		# Put val into the stack
		super().add(val)


	def pop(self):
		#Remove and return the oldest member of the stack(???)
		# Shouldn't it return the youngest member of the stack?
		val = self.head.getData()
		super().remove( self.head )
		return val

	def peek(self):
		return self.head.getData()
