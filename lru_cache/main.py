class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, node):
        
        if not self.head:
            self.head = node
            self.head = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def move_front(self, node):
        if self.head is node:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        self.push_front(node)

    def pop_back(self):
        if not self.tail:
            return None
        tail = self.tail
        self.tail = tail.prev
        return tail

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = Dict()
        self.queue = Deque()

    def put(self, key, value):
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self.cache[key] = node
            self.queue.move_front(node)
            return 

        if len(self.cache) >= self.capacity:
            # Drop
            node_to_drop = self.queue.pop_back()
            del(self.cache[node_to_drop.key])
            self.capacity -= 1

        node = Node(key, value)
        self.cache[key] = node
        self.capacity += 1
        self.queue.push_front(node)

    def get(self, key):
        node = self.cache.get(key)
        if node:
            self.move_front(node)
            return node.value
        else:
            return -1

