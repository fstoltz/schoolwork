
import unittest

from doublelinkedlist import DoubleLinkedList

class Test_DoubleLinkedList_Add(unittest.TestCase):
    def test_create_empty_list( self ):
        ll = DoubleLinkedList()
        self.assertEqual( ll.size(), 0 )
        self.assertEqual( ll.head, None )
        self.assertEqual( ll.tail, None )

    def test_add_empty_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        self.assertNotEqual( ll.head, None )
        self.assertNotEqual( ll.tail, None )
        self.assertEqual( ll.size(), 1 )
        self.assertEqual( ll.head, ll.tail )

    def test_add_nonempty_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.add( 100 )
        self.assertEqual( ll.size(), 2 )

class Test_DoubleLinkedList_AddEnd(unittest.TestCase):
    def test_add_empty_list( self ):
        ll = DoubleLinkedList()
        ll.addEnd( 50 )
        self.assertEqual( ll.size(), 1 )
        self.assertNotEqual( ll.head, None )
        self.assertNotEqual( ll.tail, None )
        self.assertEqual( ll.head, ll.tail )

    def test_add_nonempty_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.add( 100 )
        self.assertEqual( ll.size(), 2 )
        self.assertNotEqual( ll.head, None )
        self.assertNotEqual( ll.tail, None )
        self.assertNotEqual( ll.head, ll.tail )



class Test_DoubleLinkedList_Search(unittest.TestCase):

    def test_search_empty_list( self ):
        ll = DoubleLinkedList()
        self.assertEqual( ll.search(10), None )

    def test_search_nonempty_list( self ):
        ll = DoubleLinkedList()
        ll.add( 10 )
        self.assertNotEqual( ll.search(10), None )

    def test_search_nonempty_list_notfound( self ):
        ll = DoubleLinkedList()
        ll.add( 10 )
        self.assertEqual( ll.search(11), None )


class Test_DoubleLinkedList_Insert(unittest.TestCase):

    def test_insert_end_nonempty_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.insert( 100, ll.search(50) )
        self.assertEqual( ll.size(), 2 )


class Test_DoubleLinkedList_Remove(unittest.TestCase):

    def test_remove_head_list( self ):
        ll = DoubleLinkedList()
        ll.addEnd( 50 )
        ll.addEnd( 55 )
        ll.addEnd( 60 )
        ll.addEnd( 65 )
        ll.remove( ll.search(50) )
        self.assertEqual( ll.size(), 3 )
        self.assertNotEqual( ll.head, None )
        self.assertEqual( ll.head.getData(), 55 )

    def test_remove_middle_list( self ):
        ll = DoubleLinkedList()
        ll.addEnd( 50 )
        ll.addEnd( 55 )
        ll.addEnd( 60 )
        ll.addEnd( 65 )
        ll.remove( ll.search(55) )
        self.assertEqual( ll.size(), 3 )

    def test_remove_end_list( self ):
        ll = DoubleLinkedList()
        ll.addEnd( 50 )
        ll.addEnd( 55 )
        ll.addEnd( 60 )
        ll.addEnd( 65 )
        ll.remove( ll.search(65) )
        self.assertEqual( ll.size(), 3 )
        self.assertNotEqual( ll.tail, None )
        self.assertEqual( ll.tail.getData(), 60 )

    def test_remove_entire_list( self ):
        ll = DoubleLinkedList()
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

    def test_insert_and_remove_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.addEnd( 100 )
        ll.insert( 150, ll.search(50) ) # insert in middle
        self.assertEqual( ll.size(), 3 )
        ll.remove( ll.search( 150 ) )
        self.assertEqual( ll.size(), 2 )
        self.assertEqual( ll.toList(), [50, 100] )




class Test_DoubleLinkedList_ToList(unittest.TestCase):

    def test_empty_list( self ):
        ll = DoubleLinkedList()
        self.assertEqual( ll.toList(), [] )

    def test_nonempty_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        self.assertEqual( ll.toList(), [65,60,55,50] )

class Test_LinkedList_Reverse(unittest.TestCase):

    def test_empty_list( self ):
        ll = DoubleLinkedList()
        ll.reverse()
        self.assertEqual( ll.toList(), [] )

    def test_nonempty_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        old_head = ll.head
        old_tail = ll.tail
        ll.reverse()
        self.assertEqual( ll.head, old_tail )
        self.assertEqual( ll.tail, old_head )
        self.assertEqual( ll.toList(), [50,55,60,65] )

    def test_nonempty_list_reverse_updates_prev_ptr( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.add( 55 )
        ll.add( 60 )
        ll.add( 65 )
        ll.reverse()
        n60 = ll.remove( ll.search( 60 ) )
        # NOTE: This test is testing that you aren't cheating with
        # your reverse() function by just doing what a singly linked
        # list does..  it might run into an infinite loop :)
        self.assertEqual( ll.toList(), [50,55,65] )


    def test_insert_remove_and_reverse_list( self ):
        ll = DoubleLinkedList()
        ll.add( 50 )
        ll.addEnd( 100 )
        ll.insert( 150, ll.search(50) ) # insert in middle
        self.assertEqual( ll.size(), 3 )
        ll.remove( ll.search( 50 ) )
        self.assertEqual( ll.size(), 2 )
        ll.reverse()
        # NOTE: This test is testing that you don't forget to
        # update next / prev properly when inserting..
        self.assertEqual( ll.toList(), [100, 150] )

