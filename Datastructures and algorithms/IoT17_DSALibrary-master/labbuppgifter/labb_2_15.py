
from graph import Graph

g = Graph()
g.addVertex("STHLM")
g.addVertex("OREBRO")
g.addVertex("LIDK")
g.addVertex("GBG")
g.addVertex("HELBG")
g.addVertex("LUND")
g.addVertex("KRIST")
g.addVertex("JONK")
g.addVertex("LINK")

g.addEdge( "STHLM",  "OREBRO", 75 )
g.addEdge( "OREBRO", "LIDK",   25 )
g.addEdge( "LIDK",   "GBG",    50 )
g.addEdge( "GBG",    "HELBG",  5 )
g.addEdge( "HELBG",  "LUND",   5 )
g.addEdge( "LUND",   "KRIST",  20 )
g.addEdge( "KRIST",  "JONK",   15 )
g.addEdge( "HELBG",  "JONK",   35 )
g.addEdge( "JONK",   "LINK",   100 )
g.addEdge( "LINK",   "STHLM",  30 )

print("Cheapest:", g.findCheapestPath( "STHLM", "LUND" ) )
print("DFS:", g.findDFSPath( "STHLM", "LUND" ) )
print("BFS:", g.findBFSPath( "STHLM", "LUND" ) )
