def hashMAtricula(matricula, size):
    m = str(matricula)
    u = m[-1]
    d = m[-2]
    key = int(d+u)
    return key % size
def lookForColisions1(keys, size):
    table = [None] * size
    for i in keys:
        position = i % size #hash
        if table[position] is not None:
            print(f"Colided keys: {i} and {table[position]}")
        table[position] = i
        # We pad the hole table, while we look for equal hashes
def lookForColisions(keys,size):
    table = [None] * size
    for i in keys:
        position = i % size
        if table[position] is not None:
            return f"Colided keys: {i} and {table[position]}"
        else:
            table[position] = i

class hashTable:
    def __init__(self, size):
        self._table = [None] * size
        self._size = size
    @property
    def table(self):
        return self._table
    @property
    def size(self):
        return self._size
    @table.setter
    def table(self, newTable):
        self._table = newTable
    @size.setter
    def size(self, newSize):
        self._size = newSize
    def insertKey(self, key):
        position = key % self.size
        if self.table[position] is not None:
            return f"Colided keys: {self.table[position]} and {key}"
        self.table[position] = key
class HashTable2:
    def __init__(self, size):
        self._size = size
        self._table = [[] for i in range(size)]

    @property
    def size(self):
        return self._size
    @property
    def table(self):
        return self._table
    def insertKey(self, key):
        position = key % self.size
        self._table[position].append(key)
        
    def __str__(self):
        return self._table
table = HashTable2(10)
print(table)
table.insertKey(10)
table.insertKey(100)
table.insertKey(90)
print(table)