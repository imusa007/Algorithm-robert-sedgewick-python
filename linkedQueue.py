class Empty(Exception):
    """Error attempting to access a element form empty container"""
    pass


class LinkedQueue:
    """FIFO queue implemented using linked list"""

    # -------------- Nested Node class------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, n):
            self._element = e
            self._next = n

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):

        return self._size

    def __iter__(self):
        self.current=self._head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item=self.current._element
            self.current=self.current._next
            return item

    def __str__(self):
        """return content of the whole array"""
        return " ".join([str(s) for s in self])



    def is_empty(self):

        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)

        if self.is_empty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail=None
        return answer

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._head._element

