

class ListNode():
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	@classmethod
	def build(cls, array):
		if not array:
			return None

		return cls(array[0], cls.build(array[1:]))

	def print(self):
		values = [self.val]
		next_ = self.next

		while next_:
			values.append(next_.value)
			next_ = next_.next

		print("->".join(values))


