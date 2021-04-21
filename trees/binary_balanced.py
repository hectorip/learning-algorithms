# Binary search Tree is a search tree that helps in search


class Tree():
    """Implements all the functions of a tree"""
   def __init__(self, value, left=None, right=None):
        self._left = left
        self._right = right
        self.value = value

    def add(self, value):
        if self.value >= value:
            self._left.add(value)
        else:

