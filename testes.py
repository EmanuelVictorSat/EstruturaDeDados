class No:
    def __init__(self, value = None):
        self._value = value
        self._next = None
    @property
    def value(self):
        return self._value
    @value.setter(self, newValue):
        self._value = newValue
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, newNext):
        self._next = newNext
class ListaEncadeada:
    def __init__(self):
        self._first = None
    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, newFirst):
        self._first = newFirst
    
