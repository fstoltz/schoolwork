
import unittest

from BinarySTreeMark import BinarySearchTree


class Test_BinarySearchTree_IsEmpty(unittest.TestCase):
    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.isEmpty(), True)

    def test_nonempty_tree(self):
        bst = BinarySearchTree(20)
        self.assertEqual(bst.isEmpty(), False)


class Test_BinarySearchTree_Size(unittest.TestCase):
    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.size(), 0)

    def test_nonempty_tree(self):
        bst = BinarySearchTree(20)
        self.assertEqual(bst.size(), 1)


class Test_BinarySearchTree_Insert(unittest.TestCase):
    def test_insert_from_empty_tree(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.size(), 0)
        bst.insert(10)
        self.assertEqual(bst.size(), 1)

    def test_insert_from_nonempty_tree(self):
        bst = BinarySearchTree(10)
        bst.insert(20)
        self.assertEqual(bst.size(), 2)

    def test_insert_multiple_items_from_empty_tree(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        self.assertEqual(bst.size(), 3)

    def test_insert_multiple_items_from_nonempty_tree(self):
        bst = BinarySearchTree(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        self.assertEqual(bst.size(), 4)


class Test_BinarySearchTree_Delete(unittest.TestCase):
    def test_delete_tree_size_1(self):
        bst = BinarySearchTree(10)
        self.assertEqual(bst.size(), 1)
        bst.delete(10)
        self.assertEqual(bst.size(), 0)

    def test_delete_root_node(self):
        bst = BinarySearchTree(10)
        bst.insert(20)
        bst.insert(30)
        bst.insert(5)
        bst.insert(9)
        self.assertEqual(bst.size(), 5)
        bst = bst.delete(10)
        self.assertEqual(bst.size(), 4)

    def test_insert_and_delete_tree(self):
        bst = BinarySearchTree(10)
        bst.insert(20)
        self.assertEqual(bst.size(), 2)
        bst = bst.delete(20)
        self.assertEqual(bst.size(), 1)
        bst = bst.delete(10)
        self.assertEqual(bst.size(), 0)

    def test_mimxed_insert_and_delete_tree(self):
        bst = BinarySearchTree(10)
        bst.insert(20)
        self.assertEqual(bst.size(), 2)
        bst = bst.delete(20)
        self.assertEqual(bst.size(), 1)
        bst.insert(50)
        bst.insert(1)
        self.assertEqual(bst.size(), 3)
        bst = bst.delete(1)
        bst = bst.delete(50)
        self.assertEqual(bst.size(), 1)


class Test_BinarySearchTree_Find(unittest.TestCase):
    def test_find_empty_tree(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find(10), None)

    def test_find_single_tree(self):
        bst = BinarySearchTree(10)
        self.assertNotEqual(bst.find(10), None)
        self.assertEqual(bst.find(10).getData(), 10)

    def test_find_nontrivial_tree(self):
        bst = BinarySearchTree()
        data = [20, 50, 1, 150, 42]
        for d in data:
            bst.insert(d)
        for d in data:
            self.assertEqual(bst.find(d).getData(), d)


class Test_BinarySearchTree_ToList(unittest.TestCase):
    def test_find_empty_tree(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.toList(), [])

    def test_find_single_tree(self):
        bst = BinarySearchTree(10)
        self.assertEqual(bst.toList(), [10])

    def test_find_nontrivial_tree(self):
        bst = BinarySearchTree()
        data = [20, 50, 1, 150, 42]
        for d in data:
            bst.insert(d)
        data.sort()
        self.assertEqual(bst.toList(), data)
