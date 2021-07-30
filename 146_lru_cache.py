from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value != -1:
            self.cache.move_to_end(key, last=True)

        return value

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.cache.move_to_end(key, last=True)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
