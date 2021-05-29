def hasCycle(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next
        if fast == slow:
            return True

        fast = fast.next
    return False