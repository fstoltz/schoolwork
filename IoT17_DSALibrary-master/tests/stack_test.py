
import unittest

from stack import LLStack

class Test_Stack_Empty(unittest.TestCase):
    def test_isEmpty_on_empty_Stack( self ):
        Stack = LLStack()
        self.assertEqual( Stack.isEmpty(), True )
        self.assertEqual( Stack.size(), 0 )

    def test_isEmpty_on_nonempty_Stack( self ):
        Stack = LLStack()
        Stack.push( 50 )
        self.assertEqual( Stack.isEmpty(), False )


class Test_Stack_Push(unittest.TestCase):
    def test_push_one_item( self ):
        Stack = LLStack()
        Stack.push( 50 )
        self.assertEqual( Stack.isEmpty(), False )
        self.assertEqual( Stack.size(), 1 )

    def test_push_two_items( self ):
        Stack = LLStack()
        Stack.push( 50 )
        Stack.push( 75 )
        self.assertEqual( Stack.isEmpty(), False )
        self.assertEqual( Stack.size(), 2 )

class Test_Stack_Pop(unittest.TestCase):
    def test_pop_after_single_push( self ):
        Stack = LLStack()
        Stack.push( 50 )
        x = Stack.pop()
        self.assertEqual( x, 50 )
        self.assertEqual( Stack.isEmpty(), True )

    def test_pop_after_two_pushes( self ):
        Stack = LLStack()
        Stack.push( 50 )
        Stack.push( 75 )
        x = Stack.pop()
        self.assertEqual( x, 75 )
        self.assertEqual( Stack.isEmpty(), False )

    def test_three_pops_after_three_pushes( self ):
        Stack = LLStack()
        Stack.push( 25 )
        Stack.push( 50 )
        Stack.push( 75 )
        x = Stack.pop()
        self.assertEqual( x, 75 )
        x = Stack.pop()
        self.assertEqual( x, 50 )
        x = Stack.pop()
        self.assertEqual( x, 25 )
        self.assertEqual( Stack.isEmpty(), True )

