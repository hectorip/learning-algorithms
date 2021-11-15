def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    lb = n
    lg = n // 2
    while lg >= 1 and lg < lb:
        # print(lg, lb)
        if isBadVersion(lg):
            lb = lg
            lg -= lg // 2
        else:
            i = (lb - lg) // 2
            if not i:
                break
            lg += i

    return lb
