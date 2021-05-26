class Empty(Exception):
    """Error attempting to access a element form empty container"""
    pass

class ArrayStack:
    """LIFO Stack implemented using a python list as underlying storage"""
    def __init__(self):
        """Create an empty stack"""
        self._data=[]

    def __len__(self):
        """Return number of element in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if stack is empty"""
        return len(self._data)==0

    def push(self, e):
        self._data.append(e)

    def top(self):

        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):

        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

class LinkedStack:
    """LIFO stack implemented using singly linked list as underlying storage"""
    #-------- Nested Node Class -------------
    class _Node:

        __slots__ = '_element','_next'

        def __init__(self,element,next):
            self._element=element
            self._next=next

    #--------------- Stack Methods -----------------------------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head=None
        self._size=0

    def __len__(self):
        """Return number of element in stack"""
        return self._size

    def is_empty(self):
        """Return true if stack is empty"""
        return self._size==0

    def push(self,element):
        """Add a new element at top of stack"""
        self._head=self._Node(element,self._head)
        self._size +=1

    def top(self):
        """Return (but do not remove) top element from stack
        Raise Empty exception if stack is empty
        """
        if(self.is_empty()):
            raise Empty('Stack is empty')

        return self._head._element

    def pop(self):
        """Return and remove top element
        Raise Empty exception if stack is empty
        """

        if(self.is_empty()):
            raise Empty('Stack is empty')
        currentElement=self._head._element
        self._head=self._head._next
        self._size-=1
        return currentElement




