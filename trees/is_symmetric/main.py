"""
Verify if a tree is symmetrical
"""


def is_symmetrical(root):
    """
    Idea: verify by level, if each level is symmetrical, the tree is
    symmetrical. To verify if each level is symmetrical we will
    split it in right and left and compare the left with the right
    side reversed
    """
    if not root.left and root.right:
        return False  # A tree cannot be symetrical
    level = [root.left, root.right]
