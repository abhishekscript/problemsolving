

class HashMap:
    def __init__(self, size) -> None:
        self.size = size
        self.hash_table = [
            [None] * self.size # Key
            [None] * self.size # Value
        ]
    
    def add(self, key, value):
        index = hash(value) % self.size
        self.hash_table[0][index] = key
        self.hash_table[1][index] = value

    def get(self, key, value):
        index = hash(value) % self.size
        return self.hash_table[1][index]


class LRUCache:
    def __init__(self, size: int =5) -> None:
        self.hash_map = HashMap(size)
        self.stack = []

    def push(self, key, value):
        self.hash_map.add(key, value)
        self.stack.append(value)
    
    def get(self, key):
        return self.hash_map[key]

from collections import OrderedDict
