def maxDepth(s):
    """Get the max depth of valid parentesis string taking into account nested parenthesis"""
    top = 0
    current = 0
    for c in s:
        if c == "(":
            current += 1
            if current > top:
                top = current
        elif c == ")":
            current -= 1
    return top