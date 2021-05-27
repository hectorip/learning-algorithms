# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(l1, l2):
    """Merge two ordered lists into one ordered list.

    Idea: traverse l1 adding corresponding element from l2, while poping the first element
    """
    result = []
    for i, e in enumerate(l1):
        while l2 and (l2[0] <= e):
            result.append(l2.pop(0))
        result.append(e)

    return result + l2


def merge_list(l1, l2):
    while l1:
        while l2 and (l2.val <= l1.val):
            l2.next = l1
            l1 = l2
            l2 = l2.next.next

        l1 = l1.next
    return l1
