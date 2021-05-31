# Remove all the nodes that have val value


def remove_by_val(head, val):
    """Idea remove all the leading nodes having the val to get the head right,
    then remmove the inner nodes
    """
    while head and head.val == val:
        head = head.next

    cursor = head
    while cursor and cursor.next:
        # Hold current node to remove next if it has the value
        if cursor.next.val == val:
            cursor.next = cursor.next.next
        else:
            cursor = cursor.next

    return head
