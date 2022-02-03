class BST:
    def __init__(self, val=None):
        self._left=None
        self._right=None
        self._val=val
    
    
    def insert(self,val):
        if not self._val:
            self._val=val
            return
        
        if self._val==val:
            return

        if val<self._val:
            if self._left:
                self._left.insert(val)
                return
            self._left=BST(val)
            return
        
        if self._right:
            self._right.insert(val)
            return
        self._right=BST(val)
    
    def preorder(self,vals=[]):
        
        if self._left:
            self._left.preorder(vals)
        
        if self._val:
            vals.append(self._val)

        if self._right:
            self._right.preorder(vals)
        
        return vals
    
    def exist(self,val):
        if val==self._val:
            return True

        if val<self._val:
            if self._left is None:
                return False
            return self._left.exist(val)

        if self._right is None:
            return False
        return self._right.exist(val)

if __name__=='__main__':
    t1=BST(16)
    t1.insert(3)
    t1.insert(28)
    print(t1.preorder())
    print(t1.exist(3))