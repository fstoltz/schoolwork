from Graph import Graph
import unittest


class TestGraph(unittest.TestCase):

	def test_01_is_empty(self):
		grp = Graph()

		self.assertEqual(grp.isEmpty(), True)
		self.assertEqual(grp.size(), 0)

	def test_02_simple_add(self):
		grp = Graph()

		grp.addVertex(50)

		self.assertEqual(grp.size(), 1)
		self.assertEqual(grp.isEmpty(), False)

	def test_03_simple_remove(self):
		grp = Graph()
		grp.addVertex(40)
		grp.addVertex(80)

		self.assertEqual(grp.size(), 2)

		grp.removeVertex(40)

		self.assertEqual(grp.size(), 1)

		grp.removeVertex(80)

		self.assertEqual(grp.isEmpty(), True)

	def test_04_add_simple_edge(self):
		grp = Graph()

		grp.addVertex(50)
		grp.addVertex(90)

		grp.addEdge(50, 90)

		self.assertEqual(grp.areNeighbours(50, 90), True)

	def test_05_remove_simple_edge_using_areNeighbours(self):

		grp = Graph()

		grp.addVertex(50)
		grp.addVertex(90)

		grp.addEdge(50, 90)

		self.assertEqual(grp.areNeighbours(50, 90), True)

		grp.removeEdge(50, 90)	

		self.assertEqual(grp.areNeighbours(50, 90), False)
		self.assertEqual(grp.size(), 2)

	def test_06_find_path_simple(self):
		grp = Graph()
		grp.addVertex(50)
		grp.addVertex(30)
		grp.addVertex(150)
		grp.addVertex(600)

		grp.addEdge(50, 30)
		grp.addEdge(30, 150)
		grp.addEdge(150, 600)

		self.assertEqual(grp.findDFSPath(30,600), [30, 150, 600])
		self.assertEqual(grp.isConnected(), True)

	def test_07_BFS_simple(self):
		g = Graph()

		g.addVertex(10)
		g.addVertex(970)
		g.addVertex(571)
		g.addVertex(7713)
		g.addVertex(513)
		g.addVertex(231)
		g.addVertex(432)
		g.addVertex(981)
		g.addVertex(181)
		g.addVertex(873)

		g.addEdge(10, 571)
		g.addEdge(970, 10)
		g.addEdge(513, 981)
		g.addEdge(571, 873)
		g.addEdge(432, 10)
		g.addEdge(231, 513)
		g.addEdge(981, 571)
		g.addEdge(7713, 981)
		g.addEdge(181, 981)
		g.addEdge(231, 571)
		g.addEdge(873, 7713)
		
		#print("BFS result: ", g.findBFSPath(432, 10))

		#print("checkpoint")



if __name__ == '__main__':
	unittest.main(verbosity=2)
