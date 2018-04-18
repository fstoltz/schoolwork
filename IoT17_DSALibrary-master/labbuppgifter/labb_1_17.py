
from graph import Graph

g = Graph()

g.addEdge( "A", "B" )
g.addEdge( "A", "E" )
g.addEdge( "B", "C" )
g.addEdge( "C", "D" )
g.addEdge( "C", "G" )
g.addEdge( "D", "H" )
g.addEdge( "E", "I" )
g.addEdge( "F", "J" )
g.addEdge( "G", "K" )
g.addEdge( "I", "M" )
g.addEdge( "J", "N" )
g.addEdge( "L", "P" )
g.addEdge( "M", "N" )
g.addEdge( "N", "O" )
g.addEdge( "O", "P" )


print( g.findDFSPath( "M", "H" ) )
# Should be
#  ['M', 'I', 'E', 'A', 'B', 'C', 'D', 'H']
