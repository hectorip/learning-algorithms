# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge(t1, t2):
    """
    Idea: merge recursively over the tallest tree
    """
    if t1:
        if t2:
            t1.val += t2.val
            t1.left = merge(t1.left, t2.left)
            t1.right = merge(t2.right, t2.right)
    else:
        return t2

    return t1
