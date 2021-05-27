# from .. import ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, array):
        if not array:
            return None

        return cls(array[0], cls.build(array[1:]))

    def print(self):
        values = [str(self.val)]
        next_ = self.next

        while next_:
            values.append(str(next_.val))
            next_ = next_.next

        print("->".join(values))

    def middle(self):
        """
        Apuntador que avanza a doble de velocidad
        """
        p1 = self  # will be at the middle when the
        p2 = self.next

        while p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                break
            p2 = p2.next
        return p1


l = [1, 2, 3, 4, 5]
ll = ListNode.build(l)
ll.middle().print()