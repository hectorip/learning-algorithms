def merge(t1, t2):
    if t1 and t2:
        t1.val += t2.val
        t1.left = merge(t1.left, t2.left)
        t1.right = merge(t1.right, t2.right)
        return t1

    return t1 or t2