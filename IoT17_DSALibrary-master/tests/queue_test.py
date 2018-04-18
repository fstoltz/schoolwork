
import unittest

from queue import LLQueue

class Test_Queue_Empty(unittest.TestCase):
    def test_isEmpty_on_empty_queue( self ):
        queue = LLQueue()
        self.assertEqual( queue.isEmpty(), True )
        self.assertEqual( queue.size(), 0 )

    def test_isEmpty_on_nonempty_queue( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        self.assertEqual( queue.isEmpty(), False )


class Test_Queue_Enqueue(unittest.TestCase):
    def test_enqueue_one_item( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        self.assertEqual( queue.isEmpty(), False )
        self.assertEqual( queue.size(), 1 )

    def test_enqueue_two_items( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        queue.enqueue( 75 )
        self.assertEqual( queue.isEmpty(), False )
        self.assertEqual( queue.size(), 2 )

class Test_Queue_Dequeue(unittest.TestCase):
    def test_dequeue_after_single_enqueue( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        x = queue.dequeue()
        self.assertEqual( x, 50 )
        self.assertEqual( queue.isEmpty(), True )

    def test_dequeue_after_two_enqueues( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        queue.enqueue( 75 )
        x = queue.dequeue()
        self.assertEqual( x, 50 )
        self.assertEqual( queue.isEmpty(), False )

    def test_three_dequeues_after_three_enqueues( self ):
        queue = LLQueue()
        queue.enqueue( 25 )
        queue.enqueue( 50 )
        queue.enqueue( 75 )
        x = queue.dequeue()
        self.assertEqual( x, 25 )
        x = queue.dequeue()
        self.assertEqual( x, 50 )
        x = queue.dequeue()
        self.assertEqual( x, 75 )
        self.assertEqual( queue.isEmpty(), True )

