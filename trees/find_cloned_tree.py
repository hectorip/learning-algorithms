"""LeetCode:
"""


def find_cloned_node(original, cloned, target):
    nodes = [cloned]
    while nodes:
        node = nodes.pop()
        if node.val == target.val:
            return node
        else:
            node.left and nodes.append(node.left)
            node.right and nodes.append(node.right)
