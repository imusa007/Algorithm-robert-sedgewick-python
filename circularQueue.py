class Empty(Exception):
    """Error attempting to access a element form empty container"""
    pass


class CircularQueue:
    """FIFO queue implemented using list as underlying storage"""
    DEFAULT_SIZE = 10

    def __init__(self):
        """Create empty queue of Default size"""
        self._data = [None] * CircularQueue.DEFAULT_SIZE
        self._front = 0
        self._size = 0

    def __len__(self):
        """return number of element in queue"""
        return self._size

    def __str__(self):
        """return content of the whole array"""
        return " ".join([str(s) for s in self._data])

    def is_empty(self):
        """Return True if queue is empty"""
        return self._size == 0

    def is_full(self):
        """Return true if underlying storage array is full"""
        return self._size == len(self._data)

    def first(self):
        """return (but do not remove) first element of the queue
        raise Empty exception if array is empty
        """
        if self.is_empty():
            raise

        return self._data[self._front]

    def enqueue(self, e):
        if self.is_full():
            self._resize(2 * len(self._data))
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def _resize(self, newsize):
        oldData = self._data
        self._data = [None] * newsize
        for k in range(self._size):
            self._data[k] = oldData[(k + self._front) % len(oldData)]
        self._front = 0
