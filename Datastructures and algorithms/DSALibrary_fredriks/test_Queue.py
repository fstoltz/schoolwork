import unittest
from Queue import Queue

"""
Things are working fine as of 1/12-2017
"""


class TestQueue(unittest.TestCase):

    def test_01_create_queue(self):
        q = Queue()
        q.enqueue(50)
        q.enqueue(100)
        q.enqueue(150)
    
        value = q.dequeue()

        self.assertEqual(value, 50)
    
    def test_02_adv_queue_stuff(self):
        q = Queue()

        q.enqueue(50)
        q.enqueue(55)
        q.enqueue(60)
        q.enqueue(65)

        li = q.toList()
        self.assertEqual(li, [50, 55, 60, 65])
        nextInLine = q.dequeue()

        li = q.toList()
        self.assertEqual(li, [55, 60, 65])

        nextInLine = q.dequeue()
        nextInLine = q.dequeue()
        nextInLine = q.dequeue()

        li = q.toList()
        self.assertEqual(li, [])

        q.enqueue(10)
        li = q.toList()
        self.assertEqual(li, [10])





if __name__ == '__main__':
    unittest.main(verbosity=2)
