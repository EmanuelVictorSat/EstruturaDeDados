class Node:
    def __init__(self, value: int):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value
    @property
    def next(self):
        return self._next

    @value.setter
    def value(self, newValue):
        self._value = newValue
    @next.setter
    def next(self, newObj):
        self._next = newObj

    #Methods

    def count(self):
        y = self
        counter = 1
        while y._next != None:
                counter += 1
                y = y._next
        return counter

    def contains(self, lookingFor):
        y = self
        while y is not None: #If r is not none, we still have objects to checkout
            if y._value == lookingFor:
                return True
            else:
                y = y.next
            return False

    def __str__(self):
        return str(self._value)