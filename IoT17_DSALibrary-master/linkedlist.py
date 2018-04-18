
class Node:
    def __init__(self, data):
        self._data=data
        self._next=None

    def getData(self):
        return self._data

    def setData(self, d):
        self._data = d

    def getNext(self):
        return self._next

    def setNext(self, n):
        self._next = n


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # OBS: add infogar i BÖRJAN av listan
    def add(self, data):
        newnode = Node(data)         # Steg 1
        newnode.setNext( self.head ) # Steg 2
        self.head = newnode          # Steg 3

    def insert(self, data, after_node):
        assert( after_node != None )
        newnode = Node(data)                    # Steg 1
        newnode.setNext( after_node.getNext() ) # Steg 2
        after_node.setNext( newnode )           # Steg 3

    def appendAtEnd(self, data):
        newnode = Node(data)
        current = self.head
        while current and current.getNext()!=None:
            current = current.getNext() # stega framåt
        if current:
            current.setNext( newnode )
        else:
            # head = None...
            self.head = newnode


    def insertAfterValue(self, data, after_value):
        after_node = self.search( after_value )
        assert( after_node != None )
        newnode = Node(data)                    # Steg 1
        newnode.setNext( after_node.getNext() ) # Steg 2
        after_node.setNext( newnode )           # Steg 3


    def size(self):
        current = self.head
        sz = 0
        while current != None:
            sz += 1
            current = current.getNext()
        return sz

    def search(self, d):
        current = self.head
        while current != None:
            if current.getData() == d:
                return current
            current = current.getNext()
        return None

    def remove(self, node):
        if self.head == node:
            self.head = node.getNext()
            del node
            return True
        current = self.head
        while current != None:
            if current.getNext() == node:
                current.setNext( current.getNext().getNext() )
                del node
                return True
            current = current.getNext()
        return False  # eller raise

    def print(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def toList(self):
        l = []
        current = self.head
        while current != None:
            l.append( current.getData() )
            current = current.getNext()
        return l

    def reverse(self):
        current = self.head
        prev = None
        while current != None:
            # Switch places..
            next = current.getNext()
            current.setNext( prev )
            prev = current
            current = next
        self.head = prev


def pre_order_walk( root ):
    visit( root )
    pre_order_walk( root.left )
    pre_order_walk( root.right )

def in_order_walk( root ):
    pre_order_walk( root.left )
    visit( root )
    pre_order_walk( root.right )

def post_order_walk( root ):
    pre_order_walk( root.left )
    pre_order_walk( root.right )
    visit( root )


