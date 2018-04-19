
import unittest

from graph import Graph

class Test_Graph_Empty(unittest.TestCase):
    def test_create_empty_graph( self ):
        g = Graph()
        self.assertEqual( g.isEmpty(), True )
        self.assertEqual( g.size(), 0 )

    def test_not_empty_graph( self ):
        g = Graph()
        g.addVertex( "A" )
        self.assertEqual( g.isEmpty(), False )
        self.assertEqual( g.size(), 1 )

class Test_Graph_Edges(unittest.TestCase):
    def test_create_simple_graph( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        self.assertEqual( g.size(), 2 )
        g.addEdge( "A", "B" )
        g.addEdge( "A", "B" )
        self.assertEqual( g.size(), 2 )


class Test_Graph_Neighbours(unittest.TestCase):
    def test_create_simple_graph( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        g.addVertex( "C" )
        g.addEdge( "A", "B" )
        g.addEdge( "B", "C" )
        self.assertEqual( g.areNeighbours( "A", "B" ), True )
        self.assertEqual( g.areNeighbours( "B", "A" ), True )
        self.assertEqual( g.areNeighbours( "A", "C" ), False )

    def test_remove_simple_graph( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        g.addEdge( "A", "B" )
        self.assertEqual( g.areNeighbours( "A", "B" ), True )
        g.removeEdge( "A", "B" )
        self.assertEqual( g.areNeighbours( "A", "B" ), False )



class Test_Graph_FindDFSPath(unittest.TestCase):
    def test_simple_path( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        g.addEdge( "A", "B" )
        self.assertEqual( g.findDFSPath( "A", "B" ), [ "A", "B" ] )

    def test_two_edge_path( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        g.addVertex( "C" )
        g.addEdge( "A", "B" )
        g.addEdge( "B", "C" )
        self.assertEqual( g.findDFSPath( "A", "C" ), [ "A", "B", "C" ] )

    def test_many_edge_path( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        g.addVertex( "C" )
        g.addVertex( "D" )
        g.addVertex( "E" )
        g.addEdge( "A", "B" )
        g.addEdge( "A", "C" )
        g.addEdge( "C", "D" )
        g.addEdge( "D", "E" )
        g.addEdge( "C", "E" )
        self.assertEqual( g.findDFSPath( "A", "E" ), [ "A", "C", "D", "E" ] )

    def test_no_path( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        g.addVertex( "C" )
        g.addVertex( "D" )
        g.addVertex( "E" )
        g.addEdge( "A", "B" )
        g.addEdge( "A", "C" )
        g.addEdge( "C", "D" )
        g.addEdge( "D", "B" )
        g.addEdge( "C", "B" )
        self.assertEqual( g.findDFSPath( "A", "E" ), None )

    def test_cheapest_path(self):
        g = Graph()

        g.addEdge("STHLM", "OREBRO", 75)
        g.addEdge("OREBRO", "LIDK", 25)
        g.addEdge("LIDK", "GBG", 50)
        g.addEdge("GBG", "HELBG", 5)
        g.addEdge("HELBG", "LUND", 5)
        g.addEdge("LUND", "KRIST", 20)
        g.addEdge("KRIST", "JONK", 15)
        g.addEdge("HELBG", "JONK", 35)
        g.addEdge("JONK", "LINK", 100)
        g.addEdge("LINK", "STHLM", 30)

        (p,c) = g.findCheapestPath("STHLM", "LUND")
        self.assertEqual( c, 160 )



    def test_cheapest_path_when_start_stop_are_neighbours_and_cheapest(self):
        g = Graph()

        g.addEdge("STHLM", "OREBRO", 75)
        g.addEdge("OREBRO", "LIDK", 25)
        g.addEdge("LIDK", "GBG", 50)
        g.addEdge("GBG", "HELBG", 5)
        g.addEdge("HELBG", "LUND", 5)
        g.addEdge("LUND", "KRIST", 20)
        g.addEdge("KRIST", "JONK", 15)
        g.addEdge("HELBG", "JONK", 35)
        g.addEdge("JONK", "LINK", 100)
        g.addEdge("LINK", "STHLM", 30)
        g.addEdge("STHLM", "LUND", 10)


        (p,c) = g.findCheapestPath("STHLM", "LUND")

        self.assertEqual( c, 10 )
        self.assertEqual( p, ['STHLM','LUND'] )


    def test_cheapest_path_when_start_stop_are_neighbours_but_more_expensive(self):
        g = Graph()

        g.addEdge("STHLM", "OREBRO", 75)
        g.addEdge("OREBRO", "LIDK", 25)
        g.addEdge("LIDK", "GBG", 50)
        g.addEdge("GBG", "HELBG", 5)
        g.addEdge("HELBG", "LUND", 5)
        g.addEdge("LUND", "KRIST", 20)
        g.addEdge("KRIST", "JONK", 15)
        g.addEdge("HELBG", "JONK", 35)
        g.addEdge("JONK", "LINK", 100)
        g.addEdge("LINK", "STHLM", 30)
        g.addEdge("STHLM", "LUND", 400)


        (p,c) = g.findCheapestPath("STHLM", "LUND")
        self.assertEqual( c, 160 )



class Test_Graph_Connected(unittest.TestCase):
    def test_create_simple_graph( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        self.assertEqual( g.isConnected(), False )
        g.addEdge( "A", "B" )
        self.assertEqual( g.isConnected(), True )

    def test_create_complex_graph( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        g.addVertex( "C" )
        g.addVertex( "D" )
        g.addVertex( "E" )
        self.assertEqual( g.isConnected(), False )
        g.addEdge( "A", "B" )
        self.assertEqual( g.isConnected(), False )
        g.addEdge( "C", "D" )
        g.addEdge( "D", "E" )
        self.assertEqual( g.isConnected(), False )
        g.addEdge( "B", "C" )
        self.assertEqual( g.isConnected(), True )



class Test_Graph_Directed(unittest.TestCase):
    def test_create_simple_graph( self ):
        g = Graph()
        g.addVertex( "A" )
        g.addVertex( "B" )
        self.assertEqual( g.findDFSPath( "A", "B" ), None )
        g.addEdge( "A", "B", directed=True )
        self.assertEqual( g.findDFSPath( "A", "B" ), [ "A", "B" ] )
        self.assertEqual( g.findDFSPath( "B", "A" ), None )



