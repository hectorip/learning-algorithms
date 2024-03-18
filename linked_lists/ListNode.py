class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, array):
        if not array:
            return None

        return cls(val=array[0], next=cls.build(array[1:]))

    def print(self):
        values = [str(self.val)]
        next_ = self.next

        while next_:
            values.append(str(next_.val))
            next_ = next_.next

        print("->".join(values))




head.nxt = ListNode("at")
item.nxt = ListNode("at")

            item | head
slot 1 -> ["ab" | "Abelardo"] -> ["at" | "Atriedes"]
slot 2 - ["b" | "Bird"] -> 
    slot 3 
