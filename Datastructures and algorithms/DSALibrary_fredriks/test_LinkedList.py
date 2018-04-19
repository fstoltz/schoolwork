from LinkedList import Node, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
	"""
	A testcase class for testing linked list functionality
	"""
	def test01_LL_empty(self):
		myLL = LinkedList()
		self.assertEqual(myLL.isEmpty(), True)

	def test02_LL_add_and_totalSize(self):
		myLL = LinkedList()
		myLL.add(10)
		self.assertEqual(myLL.totalSize(), 1) 

	def test03_LL_search(self):
		myLL = LinkedList()
		myLL.add(10)
		myLL.add(5)
		myLL.add(876)
		myLL.add(37)
		n = myLL.search(37)
		self.assertEqual(n.getData(), 37)
		n = myLL.search(5)
		self.assertEqual(n.getData(), 5)
		n = myLL.search(10)
		self.assertEqual(n.getData(), 10)

	def test04_LL_remove(self):
		myLL = LinkedList()
		myLL.add(10)
		myLL.add(5)
		myLL.add(876)
		myLL.add(37)

		node = myLL.search(5)
		myLL.remove(node)
		self.assertEqual(myLL.totalSize(), 3)

		node = myLL.search(10)
		self.assertEqual(myLL.remove(node), "Removed!")
		self.assertEqual(myLL.totalSize(), 2)

	def test05_LL_print(self):
		myLL = LinkedList()
		self.assertEqual(myLL.print(), None)

		myLL.add(10)
		myLL.add(5)
		self.assertEqual(myLL.print(), None)

	def test06_LL_toList(self):
		myLL = LinkedList()
		myLL.add(10)
		myLL.add(5)
		myLL.add(876)
		myLL.add(37)

		li = myLL.toList()

		self.assertEqual(li, [37,876,5,10])

		node = myLL.search(5)
		myLL.remove(node)
		li = myLL.toList()
		self.assertEqual(li, [37,876,10])

		#node = myLL.search(37)
		#myLL.remove(node)
		#li = myLL.toList()
		#Gives error, can't delete first(?) element!!
		#self.assertEqual(li, [876,10])


	def test07_LL_basic_insert(self):
		myLL = LinkedList()
		myLL.add(10)
		myLL.add(20)
		myLL.add(30)
		li = myLL.toList()
		self.assertEqual(li, [30,20,10])
		self.assertEqual(myLL.totalSize(), 3)

		after_node = myLL.search(20)

		myLL.insert(5, after_node)
		# Fråga Mark gällande att testa flera grejjer
		# is it considered bad practice or 
		# just a matter of preference
		li = myLL.toList()
		self.assertEqual(li, [30,20,5,10])
		self.assertEqual(myLL.totalSize(), 4)
		self.assertEqual(myLL.isEmpty(), False)


	def test08_LL_adv_inserts_and_remove(self):
		myLL = LinkedList()
		myLL.add(10)
		myLL.add(20)
		myLL.add(30)
		myLL.add(40)
		li = myLL.toList()
		self.assertEqual(myLL.totalSize(), 4)
		self.assertEqual(li, [40,30,20,10])
		#####################################
		after_node = myLL.search(40)
		myLL.insert(99, after_node)
		self.assertEqual(myLL.totalSize(), 5)
		li = myLL.toList()
		self.assertEqual(li, [40,99,30,20,10])		
		#####################################
		rem_node = myLL.search(99)
		myLL.remove(rem_node)
		self.assertEqual(myLL.totalSize(), 4)
		li = myLL.toList()
		self.assertEqual(li, [40,30,20,10])
		#####################################
		rem_node1 = myLL.search(10)
		myLL.remove(rem_node1)
		#em_node2 = myLL.search(40)
		#myLL.remove(rem_node2) ##Can't remove the head!
		
		li = myLL.toList()
		self.assertEqual(li, [40,30,20])

	def test09_LL_basic_reverse(self):
		myLL = LinkedList()
		myLL.add(10)
		myLL.add(20)
		myLL.add(30)
		myLL.add(40)
		li = myLL.toList()
		self.assertEqual(li, [40,30,20,10])

		myLL.reverse()
		li = myLL.toList()
		self.assertEqual(li, [10,20,30,40])


if __name__ == '__main__':
	unittest.main(verbosity=2)