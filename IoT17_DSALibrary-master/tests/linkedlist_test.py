
import unittest

from linkedlist import LinkedList

class Test_LinkedList_Add(unittest.TestCase):
    def test_create_empty_list( self ):
        ll = LinkedList()
        self.assertEqual( ll.isEmpty(), True )
        self.assertEqual( ll.size(), 0 )

    def test_add_empty_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        self.assertEqual( ll.size(), 1 )

    def test_add_nonempty_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 100 )
        self.assertEqual( ll.size(), 2 )


class Test_LinkedList_Search(unittest.TestCase):

    def test_search_empty_list( self ):
        ll = LinkedList()
        self.assertEqual( ll.search(10), None )

    def test_search_nonempty_list( self ):
        ll = LinkedList()
        ll.add( 10 )
        self.assertNotEqual( ll.search(10), None )

    def test_search_nonempty_list_notfound( self ):
        ll = LinkedList()
        ll.add( 10 )
        self.assertEqual( ll.search(11), None )


class Test_LinkedList_Insert(unittest.TestCase):

    def test_insert_end_nonempty_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 40 )
        ll.insert( 45, ll.search(40) )
        #ll.insertAfterValue( 100, 50 )
        self.assertEqual( ll.size(), 3 )
        self.assertNotEqual( ll.search(40), None )
        self.assertNotEqual( ll.search(40).getNext(), None )
        self.assertEqual( ll.search(40).getNext().getData(), 45 )



class Test_LinkedList_Remove(unittest.TestCase):

    def test_remove_head_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        ll.remove( ll.search(50) )
        self.assertEqual( ll.size(), 3 )

    def test_remove_middle_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        ll.remove( ll.search(55) )
        self.assertEqual( ll.size(), 3 )

    def test_remove_end_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        ll.remove( ll.search(65) )
        self.assertEqual( ll.size(), 3 )

    def test_remove_entire_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        ll.remove( ll.search(65) )
        self.assertEqual( ll.size(), 3 )
        ll.remove( ll.search(55) )
        self.assertEqual( ll.size(), 2 )
        ll.remove( ll.search(50) )
        self.assertEqual( ll.size(), 1 )
        ll.remove( ll.search(60) )
        self.assertEqual( ll.size(), 0 )




class Test_LinkedList_ToList(unittest.TestCase):

    def test_empty_list( self ):
        ll = LinkedList()
        self.assertEqual( ll.toList(), [] )

    def test_nonempty_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        self.assertEqual( ll.toList(), [65,60,55,50] )

class Test_LinkedList_Reverse(unittest.TestCase):

    def test_empty_list( self ):
        ll = LinkedList()
        ll.reverse()
        self.assertEqual( ll.toList(), [] )

    def test_nonempty_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        ll.reverse()
        self.assertEqual( ll.toList(), [50,55,60,65] )


