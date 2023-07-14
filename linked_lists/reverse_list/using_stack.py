# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        if not stack:
            return None
        new_head = stack.pop()
        current_node = new_head
        while stack:
            current_node.next = stack.pop()
            current_node = current_node.next
        current_node.next = None
        return new_head
