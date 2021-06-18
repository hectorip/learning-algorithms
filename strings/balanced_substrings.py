"""
Leetcode: https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


def balancedStringSplit(s: str) -> int:
    rs = 0
    ls = 0
    count = 0
    for c in s:
        if c == "R":
            rs += 1
        else:
            ls += 1
        if rs == ls:
            count += 1
            rs = 0
            ls = 0
    return count
