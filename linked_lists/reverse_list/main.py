# Given the head of a singly linked list, reverse the list, and return the reversed list.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        n = head and head.next
        if prev:
            prev.next = None
        while n:
            head = n
            n = n.next
            head.next = prev
            prev = head

        return head
