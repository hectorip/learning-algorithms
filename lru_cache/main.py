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
            self.tail = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def move_front(self, node):
        # Si el noddo ya está al frente, no hacemos nada
        if self.head is node:
            return

        node.prev.next = node.next
        if node.next:  # Si no es el último
            node.next.prev = node.prev
        else:
            # Si el nodo es el último, también tenemos que actuliazar la cola
            self.tail = node.prev

        node.prev = None
        self.push_front(node)

    def pop_back(self):
        """Quita el último nodo de la lista (la cola) y devuelve su valor"""
        if not self.tail:
            return None
        tail = self.tail
        # Si solo tenemos un nodo, tenemos que actualizar la cabeza y la cola
        if tail is self.head:
            self.head = None
            self.tail = None
            return tail

        self.tail = tail.prev
        self.tail.next = None
        return tail


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.queue = Deque()
        self.len = 0

    def put(self, key, value):
        node = self.cache.get(key)
        # Si ya existe la llave, actualizamod el valor y lo movemos al frente
        if node is not None:
            node.value = value
            self.queue.move_front(node)
            return 
        # Si ya está lleno el caché tenemos que borrar el último nodo
        if self.len >= self.capacity:
            node_to_drop = self.queue.pop_back()
            if not node_to_drop:
                return
            del(self.cache[node_to_drop.key])
            self.len -= 1

        self.len += 1
        node = Node(key, value)
        self.cache[key] = node
        self.queue.push_front(node)

    def get(self, key):
        node = self.cache.get(key)
        if node:
            self.queue.move_front(node)
            return node.value
        else:
            return -1

