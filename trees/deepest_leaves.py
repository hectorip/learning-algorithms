    def deepestLeavesSum(self, root: TreeNode) -> int:
        levels = [[root]]
        deepest = 0
        nodes = levels[deepest][:]
        while nodes:
            node = nodes.pop()
            if node.left or node.right:
                if len(levels) - 1 == deepest:
                    levels.append([])
                    deepest += 1
                node.left and levels[deepest].append(node.left)
                node.right and levels[deepest].append(node.right)
            if not nodes and len(levels) - 1 == deepest:
                nodes = levels[deepest][:]
                
        return sum([x.val for x in levels[-1]])