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
        return f"Key inserted in position: {position}"
    def searchFor(self, key):
        position = key % self._size
        for i in self._table[position]:
            if i == key:
                return True
        return False
    def removeKey(self, key):
        position = key % self._size
        if self.searchFor(key):
            self._table[position].remove(key)
            return "Removed"
        return f"Key not found"
    def eightExercise(self): #A lot of information
        elements = 0
        notFreeBuckets = 0
        freeBuckets = 0
        greatterBucket = 0
        #Elements
        for i in self._table:
            if i is not None:
                for j in i:
                    elements += 1
        #Not free buckets
        for i in self._table:
            if i != None:
                notFreeBuckets += 1
        #Free bucket
        for i in self._table:
            if i == None:
                freeBuckets += 1
        #Greatter Bucket
        buckets = []
        for i in self._table:
            elements2 = 0
            for j in i:
                elements2 += 1
            buckets.append(elements2)
        for i in range (len(buckets)):
            if buckets[i] >= greatterBucket:
                greatterBucket = i
        #Each result
        return f"Elements: {elements}\nNot free buckets: {notFreeBuckets}\nFree buckets: {freeBuckets}\nGreatter bucket: Bucket number: {greatterBucket}"
