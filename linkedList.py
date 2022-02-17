class _Node:
    """Class represent single node in linked list"""
    __slots__ = '_element','_next'

    def __init__(self,e,n):
        self._element=e
        self._next=n

    def __str__(self):
        return f'{self._element}'

class LinkedList:
    """Linked List ADT"""
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def is_empty(self):

        return self._size==0

    def add(self, e):
        newNode = _Node(e, None)

        if self.is_empty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def remove(self,ndx):
        assert len(self)>0, "Cant remove from an empty List"
        curNode=self._head
        prevNode=self._head

        if ndx==0:
            self._head=self._head._next
            self._size -= 1
            return

        for i in range(ndx):
            prevNode = curNode
            curNode=curNode._next

        if prevNode:
            prevNode._next=curNode._next
            self._size-=1


    def __str__(self):
        """return content of the whole array"""
        return " ".join([str(s) for s in self])

    def __len__(self):
        return self._size

    def __iter__(self):
        return _LinkedListIterator(self)

    def __index__(self,e):
        """Return index of first apprearance of given element"""
        for ndx,val in enumerate(self):
            if val==ndx:
                return ndx


class _LinkedListIterator:

    def __init__(self, theList):
        self._list=theList
        self._curItem = theList._head
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._list):
            item=self._curItem
            self._curItem = self._curItem._next
            self._curNdx += 1
            return item
        else:
            raise StopIteration
