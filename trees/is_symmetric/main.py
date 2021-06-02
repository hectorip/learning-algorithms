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
    level_left = [root.left]
    level_right = [root.right]  # This is the right side but reversed
    while level_left and level_right:
        new_level_left = []
        new_level_right = []
        for i, left_node in enumerate(level_left):
            if left_node and level_right[i]:
                if left_node.val == level_right[i].val:
                    # Continue and create the new nodes
                    new_level_left.append(left_node.left)
                    new_level_left.append(left_node.right)

                    new_level_right.append(level_right.right)  # adding in reverse
                    new_level_right.append(level_right.left)
                else:
                    return False
            elif left_node or level_right[i]:
                return False

            level_left = new_level_left
            level_right = new_level_right

    return True