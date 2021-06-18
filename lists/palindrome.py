def isPalindrome(head):
    """
    Idea: compare the the first half with the second half but reversed
    """
    fast = head.next
    slow = head
    half = [slow.val]
    # Push half of the elements into a list using the slow-fast pointers technique
    while fast:
        fast = fast.next
        slow = slow.next
        if fast:
            half.append(slow.val)
            fast = fast.next
    # Pop each element of the first half if it matches with the second half, reversed
    while slow:
        val = half.pop()
        if val != slow.val:
            return False
        slow = slow.next

    return True
