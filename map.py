class _MapEntry:
        def __init__(self,key,value):
            self._key=key
            self._value=value

class Map:
    """Map is a collection of data records in which each record is
    associated with a key. keys must be comparable with each other"""

    def __init__(self):
        self._map_entry_list=[]

    def __len__(self):
        """Returns the number of key/value pairs in the Map"""
        return len(self._map_entry_list)

    def __contains__(self,key):
        """Determine if a key exists in the map. return true 
        if the key exists"""
        ndx=self._FindKey(self,key)
        return ndx is not None

    def add(self,key, value):
        """Add a new key/value pair or replaces value if the key
         already exist. return true if the key does not exist before
         and return false  if the key exist and value replaced"""
        ndx=self._FindKey(key)
        if ndx is not None:
            self._map_entry_list[ndx]._value=value
            return False
        else:
            entry=_MapEntry(key,value)
            self._map_entry_list.append(entry)
            return True

    
    def remove(self, key):
        """Remove key/value pair if the key exist and return true.
        if the key did not exist return false"""

        ndx=self._FindKey(key)
        assert ndx is not None, "Key does not exist"
        self._map_entry_list.pop(ndx)

    def valueOf(self,key):
        """return value associated with a key"""
        ndx=self._FindKey(key)
        assert ndx is not None, "Key does not exist"
        return self._map_entry_list[ndx]._value

    def __iter__(self):
        """return a iterator"""
        return _MapIterator(self._map_entry_list)

    def _FindKey(self,key):
        for i in range(len(self)):
            if self._map_entry_list[i]._key==key:
                return i
        
        return None

class _MapIterator:
    def __init__(self, theArray):
        self._array=theArray
        self._curItem=0
    
    def __iter__(self):

        return self
    
    def __next__(self):
        if self._curItem<len(self._array):
            item=self._array[self._curItem]
            self._curItem+=1
            return item
        else:
            raise StopIteration

if __name__=='__main__':
    m=Map()
    m.add('musa','31')
    m.add('arif','34')
    m.add('krif','23')
    print(m.valueOf('musa'))