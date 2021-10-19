# https://leetcode.com/problems/search-insert-position/


def searchInsert(self, nums: List[int], target: int) -> int:
    top = len(nums) - 1
    bottom = 0
    while top > bottom:
        i = (top + bottom) // 2
        if nums[i] == target:
            return i
        elif nums[i] > target:
            top = i - 1
        else:
            bottom = i + 1

    if nums[bottom] >= target:
        return bottom
    else:
        return bottom + 1
