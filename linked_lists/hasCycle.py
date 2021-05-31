def hasCycle(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next
        if fast == slow:
            return True
        slow = slow.next

        fast = fast.next
