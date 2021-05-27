# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def create(cls, array):
        l = cls(array[0])
        cl = l
        for e in array[1:]:
            nn = ListNode(e)
            cl.next = nn
            cl = nn
        return l

    def print(self):
        print(self.val)
        if self.next:
            print("->")
            self.next.print()


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
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        rl = l1

        al = l2
    else:
        rl = l2
        al = l1

    mp = rl
    ap = al
    while mp.next:
        while ap and (ap.val <= mp.next.val):
            temp = mp.next
            mp.next = ap
            mp = mp.next

            ap = ap.next
            mp.next = temp

        mp = mp.next
    mp.next = ap
    return rl


if __name__ == "__main__":
    l1 = ListNode.create([1, 3, 5])
    # ll.print()
    l2 = ListNode.create([2, 4, 6])
    merge_list(l1, l2).print()
