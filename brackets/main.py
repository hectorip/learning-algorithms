"""
Leetcode brackets
"""


def check(s):
    """
    Idea: place in a [stack](https://computersciencewiki.org/index.php/Stack) if the stack is not empty at the end of the string, it is invalid.
    If any character is placed incorrectly ("]" without "[", for example) the process ends immediately
    """

    stack = []
    pairs = {
        "]": "[",
        "}": "{",
        ")": "(",
    }
    closers = pairs.keys()
    for c in s:
        if c in closers:
            opener = pairs[c]
            try:
                removed = stack.pop()
                if removed != opener:
                    return False
            except:
                return False
        else:
            stack.append(c)

    if len(stack) > 0:
        return False

    return True
