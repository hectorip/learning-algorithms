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
    for c in s:
        closer = pairs.get(c, None)
        if closer:
            try:
                removed = stack.pop()
                if removed != closer:
                    return False
            except Exception:
                # This fails when stack is empty, meaning we have a closing char without an opener char
                return False
        else:
            stack.append(c)

    if len(stack) > 0:
        return False

    return True
