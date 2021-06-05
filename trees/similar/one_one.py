def leaf(root1, root2):
    """
    Sacar una de a y una de b hasta terminar
    """
    nodes1 = [root1]
    nodes2 = [root2]
    while nodes:
        node = nodes.pop()
        if node.left or node.right:
            node.left and nodes.append(node.left)
            node.right and nodes.append(node.right)
        else:
            val = node.val
            while nodes2:
                node2 = nodes2.pop()
                if node2.left or node2.right:
                    node2.left and nodes2.append(node2.left)
                    node2.right and nodes2.append(node2.right)
                else:
                    if node2.val!=val:
                        return False
                    break
    if nodes2:
        return False
    return True
