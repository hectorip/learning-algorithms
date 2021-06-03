def search(root, val):
    if not root:
        return None
    if root.val > val:
        return search(root.left, val)
    if root.val < val:
        return search(root.right, val)

    return root