from Tree import Tree


class BinaryTree(Tree):
    """Abstract Base class representing Binary Tree"""

    def left(self, p):
        """return left child of Position p
        return None if p does not have any left child"""
        raise NotImplementedError("must implement in subclass")

    def right(self, p):
        """return right child of position p
        return None if p does not have any right child"""
        raise NotImplementedError("must be implemented in subclass")

    def sibling(self, p):
        """return sibling of position p
        return None if No sibling"""

        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
