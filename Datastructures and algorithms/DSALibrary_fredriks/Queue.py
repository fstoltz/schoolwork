from LinkedList import LinkedList

class Queue(LinkedList):
    """
    An attempt to implement a Queue datastructure,
    using a linked list as implementation.
    """
    def __init__(self):
        super().__init__()

    def enqueue(self, x):
        """ Put x into the queue """
        super().appendAtEnd(x)
        return None

    def dequeue(self):
        #   Remove and return the oldest member
        #   of the queue
        x = self.head.getData()
        super().remove( self.head )
        return x