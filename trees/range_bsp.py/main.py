"""
Sum all the nodes between the left and right values inclusive
"""

def range_sum(root, left, right):
    result = 0
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node.val >= left and node.val <= right:
            result += node.val
        node.left and nodes.append(node.left)
        node.right and nodes.append(node.right)
    return result
