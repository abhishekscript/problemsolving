class Node:
    def __init__(self, key, value, prev=None, next=None) -> None:
        self.key = key
        self.vale = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity) -> None:
        self.capactiy = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capactiy:
            oldest_node = self.head.next
            self._remove(oldest_node)
            del self.cache[oldest_node.key]

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail



