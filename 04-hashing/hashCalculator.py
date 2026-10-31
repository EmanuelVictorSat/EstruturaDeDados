# Chat exercises
def hash_code(key, listSize):
    hash = key % listSize
    return hash
def registrationHashCalculator(registration, size):
    n = str(registration)
    d = int(n[-2])
    u = int(n[-1])
    
    key = d + u
    return key % size

def identifyColisions(keys, size):
    table = [None] * size
    for i in keys:
        position = i % size
        if table[position] is not None:
            print(f"Colided keys: {i} and {table[position]}")
        table[position] = i

class Table:
    def __init__(self, size):
        self._table = [None] * size
        self._size = size
    @property
    def table(self):
        return self._table
    def insertValue(self, key):
        position = key % self._size
        if self._table[position] is None:
            self._table[position] = key 
        else:
            return f"Colided keys: {self._table[position]} and {key}"
        return self._table