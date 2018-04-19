from Queue import Queue
from Stack import Stack

class Graph:
	"""
	An attempt to implement a graph abstract data structure
	"""

	def __init__(self):
		self._table = {}

	def isEmpty(self):
		"""
		If there's no keys in the self._table, return True
		Otherwise, return False
		"""
		if self.size() != 0:
			return False
		else:
			return True

	def size(self):
		"""
		Returns the amount of keys in self._table
		"""
		return len(self._table.keys())

	def addVertex(self, v):
		if v not in self._table.keys():
			self._table[v] = set([])

	def removeVertex(self, v):
		if v in self._table.keys():
			del self._table[v]
		#obs: måste också ta bort alla values med v

	def addEdge(self, v1, v2):
		if not v1 in self._table.keys():
			self.addVertex(v1)

		self._table[v1].add(v2)

		if not v2 in self._table.keys():
			self.addVertex(v2)

		self._table[v2].add(v1)

	def removeEdge(self, v1, v2):
		if v2 in self._table[v1]:
			self._table[v1].remove(v2)
		if v1 in self._table[v2]:
			self._table[v2].remove(v1)

	def areNeighbours(self, v1, v2):
		if v2 in self._table[v1]:
			return True
		else:
			return False

    #def findDFSPath(self, v1, v2, visited=[] ):
    #    if self.areNeighbours( v1, v2 ):
    #        return [ v1, v2 ]
    #    # else use DFS..
    #    if v1 in self._table.keys():
    #        neighbours = self._table[v1]
    #        for (n,w) in neighbours:
    #            if n not in visited:
    #                p = self.findDFSPath( n, v2, visited+[v1] )
    #                if p!=None:
    #                    return [v1] + p
    #    return None

	def findDFSPath(self, v1, v2):
		visited = []
		stack = Stack()
		stack.push( (v1, [v1]) )

		while not stack.isEmpty():
			(node,path) = stack.pop()
			#visit node..
			visited.append(node)
			if node == v2:
				#found path!
				return path

			neighbours = self._table[node]
			for ( n, w ) in neighbours:
				if n not in visited:
					stack.push( (n, path+[n]) )
		return None


	def findBFSPath(self, v1, v2): #v for vertex
		"""
		Using Queue container datastructure for implementing
		breadth-first search. This method will always return the shortest path in distance,
		but it might take long to find it if the node is far away, though if it's close,
		it will find it faster than DFS.
		"""
		visited = []
		queue = Queue()
		queue.enqueue( (v1, [v1]) )
		while not queue.isEmpty():
			(node, path) = queue.dequeue()
			# visit node..
			visited.append(node)
			if node == v2:
				# found path!
				return path

			neighbours = self._table[node]
			for (n, w) in neighbours:
				if n not in visited:
					queue.enqueue((n, path + [n]))
		return None


	def isConnected(self):
		"""
		:return: True if there is a path, False if there's no path.
		"""

		for v1 in self._table.keys():
			for v2 in self._table.keys():
				#	For each pair of nodes, see if there is a path?
				if v1 != v2 and not self.findDFSPath(v1, v2):
					return False #	No path could be found

		return True #	A path was found


