
from linkedlist import LinkedList

class LLStack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, x):
        # Put x into the stack
        super().add( x )
        return None

    def pop(self):
        # Remove and return the oldest member of the stack
        x = self.head.getData()
        super().remove( self.head )
        return x
