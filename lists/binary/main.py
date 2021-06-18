
def list_to_binary(l):
    """Idea: Get element by element multiplying previous sum by 2 each time"""
    total = 0
    while l:
        total *= 2
        total += l.val
        l = l.next

    return total
