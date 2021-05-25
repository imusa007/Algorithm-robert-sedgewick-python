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