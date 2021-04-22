"""Binary search Tree is a search tree that helps in search"""


class Tree:
    """Implements all the functions of a tree"""

    def __init__(self, value, left=None, right=None):
        self._left = left
        self._right = right
        self.value = value

    def add(self, value):
        if self.value > value:
            if self._left is not None:
                self._left.add(value)
            else:
                self.left = Tree(value)
        elif self.value < value:
            if self._right is not None:
                self._right.add(value)
            else:
                self._right = Tree(value)
        # Balance Tree
        # Investigate if it is unbalanced
        # Balance

    def print(self, level=0):
        print(self.value)
        if self._left is not None:
            print("|")
            self._left.print()


values =  [3, 2, 1]

for v in values:
