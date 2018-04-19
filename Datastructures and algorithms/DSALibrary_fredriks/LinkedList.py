
class Node:
	def __init__(self, d):
		self.data = d
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self, n):
		self.next = n

	def setData(self, d):
		self.data = d


#################################
#################################

class LinkedList:
	"""
	An attempt to implement a linked list datastructure
	"""
	def __init__(self):
		self.head = None

		#Insert at start of linked list
	def add(self, d):
		"""
		Adds a new node to the linked list
		"""
		newNode = Node(d)
		newNode.setNext(self.head)
		self.head = newNode

	def totalSize(self):
		"""
		Returns the number of items in 
		the linked list
		"""
		current = self.head
		size = 0
		while current != None:
			current = current.getNext()
			size += 1
		return size

	def search(self, value):
		"""
		Returns a node that holds
		the param value as its data
		"""
		current = self.head
		while current != None: #While it's not the tail
			if current.getData() == value:
				return current
			current = current.getNext()
		return "Not found."

	def reverse(self):
		current = self.head
		prev = None
		while current != None: #while current is not the tail
			next_node = current.getNext()
			current.setNext(prev)
			prev = current
			current = next_node
		self.head = prev


	def remove(self, node):
		if self.head == node:
			self.head = node.getNext()
			del node
			return True
		current = self.head
		while current != None:
			if current.getNext() == node:
				current.setNext( current.getNext().getNext() )
				del node
				return "Removed!"
			current = current.getNext()

	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False


	def print(self):
		current = self.head
		while current != None:
			print(current.getData())
			current = current.getNext()
		return 

	def toList(self):
		"""
		Returns a list with all the elements
		"""
		current = self.head
		li = []
		while current != None:
			li.append(current.getData())
			current = current.getNext()
		return li


	def insert(self, d, after_node):
		"""
		d: the data value to insert
		after_node: the node to insert the newnode after
		"""
		newNode = Node(d)
		newNode.setNext( after_node.getNext() )
		after_node.setNext( newNode )

	def appendAtEnd(self, data):
		newNode = Node(data)
		current = self.head
		
		while current and current.getNext() != None:
			current = current.getNext()
		if current:
			current.setNext(newNode)
		else:
			# head = None
			self.head = newNode

	def insertAfterValue(self, data, afterVal):
		afterNode = self.search(afterVal)

		assert(afterNode != None) #Verify that it found the node
		
		newNode = Node(data)					#Steg 1
		newNode.setNext( afterNode.getNext() )  #Steg 2
		afterNode.setNext(newNode)				#Steg 3

	def __str__(self):
		"""
		Determines how print(linkedlistObj) should be handled
		"""
		pass