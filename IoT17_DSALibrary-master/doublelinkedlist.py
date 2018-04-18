
class Node:
    def __init__(self, data):
        self._data=data
        self._next=None
        self._prev=None

    def getData(self):
        return self._data

    def setData(self, d):
        self._data = d

    def getNext(self):
        return self._next

    def setNext(self, n):
        self._next = n

    def getPrev(self):
        return self._prev

    def setPrev(self, p):
        self._prev = p


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        newnode = Node(data)         # Steg 1
        newnode.setPrev( None )
        newnode.setNext( self.head ) # Steg 2
        if self.head:
            self.head.setPrev( newnode )
        self.head = newnode          # Steg 3
        if self.tail == None:
            self.tail = newnode

    def addEnd(self, data):
        newnode = Node(data)         # Steg 1
        if self.tail:
            self.tail.setNext( newnode )
        newnode.setPrev( self.tail ) # Steg 2
        self.tail = newnode          # Steg 3
        if not self.head:
            self.head = newnode

    def insert(self, data, after_node):
        assert( after_node != None )
        newnode = Node(data)                    # Steg 1
        newnode.setPrev( after_node )
        newnode.setNext( after_node.getNext() ) # Steg 2
        if after_node.getNext():
            after_node.getNext().setPrev( newnode )
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
        assert( node!=None )
        next = node.getNext()
        prev = node.getPrev()
        if prev:
            prev.setNext( next )
        else:
            self.head = next
        if next:
            next.setPrev( prev )
        else:
            self.tail = prev
        del node

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
        while current != None:
            # Switch places..
            tmp = current.getNext()
            current.setNext( current.getPrev() )
            current.setPrev( tmp )
            current = tmp
        tmp = self.tail
        self.tail = self.head
        self.head = tmp
