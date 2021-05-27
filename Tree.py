class Tree:
    """Abstract base class of a tree structure"""

    # ------------nested Position class-------------
    class Position:
        """Abstract class represent position of a single class"""

        def element(self):
            """return element stored at this position"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """return true if other position represent same location"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """return true if other position doesnot represent same location"""
            return not (self == other)

        # ------Abstract methods that concrete class must support ----------------

        def root(self):
            """return Position repesenting root of the tree (None if tree empty)"""
            raise NotImplementedError("must be implemented by subclass")

        def parent(self, p):
            """return Position of p's parent (or None if p is root) """
            raise NotImplementedError("must be implemented by subclass")

        def num_children(self, p):
            """return number of children of Position p"""
            raise NotImplementedError("must be implemented by subclass")

        def children(self, p):
            """return a iterator over the children of position P """
            raise NotImplementedError("must be implemented by subclass")

        def __len__(self):
            """return total number of element in tree """
            raise NotImplementedError("must be implemented by subclass")

        # --------Concrete method implemented in this code---------------

        def is_root(self, p):
            """return true if Position p is root of tree"""
            return self.root == p

        def is_leaf(self, p):
            """return true if Position p has no children"""
            return self.num_children(p) == 0

        def is_empty(self):
            """return true if tree is empty"""
            return len(self) == 0

        def depth(self,p):
            """return number of ancestor of Position p (0 if p is root)"""

            if self.is_root(p):
                return 0
            else:
                return 1+self.depth(self.parent(p))

        def _height2(self,p):
            if self.is_leaf(p):
                return 0
            else:
                return 1+max(self._height2(c) for c in self.children(p))

        def height(self,p=None):

            if p is None:
                p=self.root()
            return self._height2(p)


