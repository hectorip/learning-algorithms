def univalued(root):
    """
    Traverse the tree checking if all the nodes have the 
    same value as the root
    """
    val = root.val
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node.val != val:
            return False
        else:
            # tricky way of doing an 'if', only adding not-null nodes
            node.left and nodes.append(node.left)
            node.right and nodes.append(node.right)
    return True