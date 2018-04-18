
from queue import LLQueue
from stack import LLStack

class Graph:
    def __init__(self):
        self._table = {}

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._table.keys())

    def addVertex(self, v):
        if v not in self._table.keys():
            self._table[v] = set([])

    def removeVertex(self, v ):
        if v in self._table.keys():
            del self._table[v]

    def addEdge(self, v1, v2, weight=1, directed=False):
        if not v1 in self._table.keys():
            self.addVertex( v1 )
        self._table[v1].add( (v2,weight) )
        if not directed:
            if not v2 in self._table.keys():
                self.addVertex( v2 )
            self._table[v2].add( (v1,weight) )

    def removeEdge(self, v1, v2, directed=False):
        for (v,w) in self._table[v1]:
            if v == v2:
                self._table[v1].remove( (v,w) )
                break
        if not directed:
            for (v,w) in self._table[v2]:
                if v == v1:
                    self._table[v2].remove( (v,w) )
                    break

    def areNeighbours(self, v1, v2 ):
        if v1 in self._table.keys():
            for (v, w) in self._table[v1]:
                if v == v2:
                    return True
        return False

    def cost(self, v1, v2 ):
        if v1 in self._table.keys():
            for (v, w) in self._table[v1]:
                if v == v2:
                    return w
        return 0


    #def findDFSPath(self, v1, v2, visited=[] ):
    #    if self.areNeighbours( v1, v2 ):
    #        return [ v1, v2 ]
    #    # else use DFS..
    #    if v1 in self._table.keys():
    #        neighbours = self._table[v1]
    #        for (n,w) in neighbours:
    #            if n not in visited:
    #                p = self.findDFSPath( n, v2, visited+[v1] )
    #                if p!=None:
    #                    return [v1] + p
    #    return None

    def findDFSPath(self, v1, v2 ):
        visited = []
        stack=LLStack()
        stack.push( (v1, [v1]) )
        while not stack.isEmpty():
            (node,path) = stack.pop()
            # visit node..
            visited.append( node )
            if node == v2:
                # found path!
                return path

            neighbours = self._table[node]
            for ( n, w ) in neighbours:
                if n not in visited:
                    stack.push( (n, path+[n] ) )
        return None

    def findBFSPath(self, v1, v2 ):
        visited = []
        queue=LLQueue()
        queue.enqueue( (v1, [v1]) )
        while not queue.isEmpty():
            (node,path) = queue.dequeue()
            # visit node..
            visited.append( node )
            if node == v2:
                # found path!
                return path

            neighbours = self._table[node]
            for ( n, w ) in neighbours:
                if n not in visited:
                    queue.enqueue( (n, path+[n] ) )
        return None




    def findCheapestPath(self, v1, v2, visited=[] ):
        cheapest_cost = None
        cheapest_path = None
        cheapest_is_neighbour = False
        if v2 not in visited and self.areNeighbours(v1, v2):
            cheapest_cost = self.cost(v1, v2)
            cheapest_path = [v1,v2]
            cheapest_is_neighbour = True

        # else use BFS..
        if v1 in self._table.keys():
            neighbours = self._table[v1]
            for (n,w) in neighbours:
                if n not in visited:
                    ( p, cost ) = self.findCheapestPath( n, v2, visited+[v1] )
                    if not cheapest_cost and not cheapest_path:
                        cheapest_cost = cost
                        cheapest_path = p
                    elif cost!= 0 and cost < cheapest_cost:
                        cheapest_cost = cost
                        cheapest_path = p
                        cheapest_is_neighbour = False

            if cheapest_path != None:
                if cheapest_is_neighbour:
                    return ( cheapest_path, cheapest_cost )
                else:
                    return ( [v1] + cheapest_path, cheapest_cost + self.cost(v1, cheapest_path[0]) )
        return (None, 0)

    def dijsktra(self, initial):
        # Note - this is for later in the course!
        visited = {initial: 0}
        path = {}
        nodes = set(self._table.keys())

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for (edge,distance) in self._table[min_node]:
                weight = current_weight + distance
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path



    def isConnected(self):
        for v1 in self._table.keys():
            for v2 in self._table.keys():
                if v1 != v2 and not self.findDFSPath( v1, v2 ):
                    return False
        return True



