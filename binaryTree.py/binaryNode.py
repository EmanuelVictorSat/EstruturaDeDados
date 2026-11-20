class Bnode:
    def __init__(self, value,):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    @value.setter
    def value(self, newValue):
        if newValue != None:
            self._value = newValue
            return f"New value: {self._value}"
    @left.setter
    def left(self, newLeft):
        self._left = newLeft
        return self._left
    @right.setter
    def right(self, newRight):
        self._right = newRight
        return self.right
    #Methods
    def haveLeft(self):
        if self._left == None:
            return False
        return True
    def haveRight(self):
        if self._right == None:
            return False
        return True
    def isLeaf(self):
        if self.haveRight() or self.haveLeft():
            return False
        else:
            return True

    def haveChildreen(self):
        return not self.isLeaf