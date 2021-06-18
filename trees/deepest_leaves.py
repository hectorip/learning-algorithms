def deepestLeavesSum(root: TreeNode) -> int:
    next_level = []
    nodes = [root]
    last_sum = 0
    while nodes:
        node = nodes.pop()
        last_sum += node.val
        node.left and next_level.append(node.left)
        node.right and next_level.append(node.right)
        if not nodes:
            if next_level:
                nodes = next_level
                last_sum = 0
                next_level = []
            else:
                return last_sum