class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)

        for i, (k, v) in enumerate(self.bucket[h]):
            if k == key:
                self.bucket[h][i] = (key, value)
                return

        self.bucket[h].append((key, value))

    def get(self, key: int) -> int:
        h = self._hash(key)

        for k, v in self.bucket[h]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)

        for i, (k, v) in enumerate(self.bucket[h]):
            if k == key:
                self.bucket[h].pop(i)
                return