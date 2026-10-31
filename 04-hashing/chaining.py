class Table:
    def __init__(self, size):
        self._size = size
        self._table = [[] for i in range(size)]
    @property
    def size(self):
        return self._size
    @property
    def table(self):
        return self._table
    def insertChaining(self, key):
        position = key % self.size
        # Empty space
        self.table[position].append(key)