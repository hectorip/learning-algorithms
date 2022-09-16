#


def addTwoNumbers(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    carry = 0
    result = ListNode()
    current_node = result
    while l1 or l2 or carry:

        a = l1 and l1.val or 0
        b = l2 and l2.val or 0
        c = carry

        s = a + b + c
        carry = s // 10
        digit_to_store = s % 10
        current_node.next = ListNode(digit_to_store)
        current_node = current_node.next
        l1 = l1 and l1.next
        l2 = l2 and l2.next

    return result.next