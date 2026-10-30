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
class Queue:
    def __init__(self):
        self._start = None
        self._end = None

    def is_empty(self):
        if self._start == None:
            return True
        else:
            return False

    def push(self, value):
        newObj = No(value)
        if self.is_empty():
            self._start = newObj
            self._end = newObj
        else:
            self._end.next = newObj
            self._end = newObj

    def poping(self):
        if self._start.next == None:
            self._start = None
            self._end = None
        else:
            self._start = self._start.next

    