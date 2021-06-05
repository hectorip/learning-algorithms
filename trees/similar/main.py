def leaf(root1):
    """
    Sacar hojas de los dos y comparar
    Sacar todas la hojas de uno y ir scando las del otro eliminado las originales
    Sacar una de a y una de b hasta terminar
    """
    leafs1 = []
]
    while nodes:
        node = nodes.pop()
        if node.left or node.right:
            node.left and nodes.append(node.left)
            node.right and nodes.append(node.right)
        else:
            yield node.val

def similar(root1, root2):
    l = leaf(root1)
    l2 = leaf(root2)

    while True:
        try:
            v = next(l)
        except:
            v = -1
        try:
            v2 = next(l2)
        except:
            v2 = -1

        if v != v2:
            return False
        if v == -1:
            return True

    return True
