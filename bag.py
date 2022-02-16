class Bag:

    def __init__(self):
        """Implements Bag ADT using list as base structure"""
        self._items = []

    def __len__(self):
        """Return number of items in the bag"""
        return len(self._items)

    def __contains__(self, item):
        """Return true if the item present in the bag"""
        return item in self._items

    def add(self, item):
        """Add item in the bag"""
        self._items.append(item)

    def remove(self, item):
        """Remove an item if it exist, raise value error if item
        is not present"""
        assert item in self._items, "The item must be in the bag"
        ndx = self._items.index(item)
        return self._items.pop(ndx)

    def __iter__(self):

        return _BagIterator(self._items)


class _BagIterator:

    def __init__(self, items):
        self._items = items
        self._curNdx = 0

    def __iter__(self):

        return self

    def __next__(self):
        if self._curNdx < len(self._items):
            item = self._items[self._curNdx]
            self._curNdx += 1
            return item
        else:
            raise StopIteration
