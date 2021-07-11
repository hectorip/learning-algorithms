"""
LeetCode: https://leetcode.com/problems/maximum-binary-tree
"""


def constructMaximumBinaryTree(nums: List[int]):
    if not nums:
        return None
    m = max(nums)
    mi = nums.index(m)
    left = nums[:mi]
    right = nums[(mi + 1) :]
    return TreeNode(
        val=m,
        left=constructMaximumBinaryTree(left),
        right=constructMaximumBinaryTree(right),
    )
