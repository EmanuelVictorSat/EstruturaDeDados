class No:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data
    @property
    def next(self):
        return self._next
    @data.setter #Method setter for the data property
    def data(self, newData):
        self._data = newData
    @next.setter
    def next(self, newObj):
        self._next = newObj

    #Conta
    #Olha se está vazio 
    #Coloca e remove
    #Consulta

    def count(self):
        p = self
        count = 1
        while p._next is not None:
            count += 1
            p = p._next
        return count
#--------------------------------> Stack <------------------------------#
class Stack:
    def __init__(self):
        self._top = None

    @property
    def top(self):
        return self._top
    @top.setter
    def top(self, new):
        self._top = new

    def is_empty(self): #Return true if the stack is empty!
        return self._top == None
    def push(self, data):
        newObj = No(data)
        newObj.next = self._top
        self._top = newObj

    def poping(self):
        removed = self._top
        self._top = self._top.next
        return f"Object removed: {removed}"

    def peek(self):
        return self._top.data

    def sizeOf(self):
        p = self._top
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count

    def countains(self, value):
        p = self._top
        while p is not None:
            if p.data == value:
                return True
            else:
                p = p.next
        return False

    def display(self):
        p = self._top
        while p is not None:
            print(p.data)
            p = p.next  

    def invert(self):
        myTop = self._top
        newStack = Stack() #Creates another instance of the Stack class
        while myTop is not None:
            newStack.push(myTop.data)
            myTop = myTop.next
        self._top = newStack.top
        return newStack.display()
    
    #É apenas a sua mente evitando o esforço, fica calmo, são pensamentos catastróficos, apenas! kkk
    def remove(self, target):
        # One only element on the list
        # I need to make the w pointer go right to his target (OK)
        aletrnative_pointer = self._top
        w = self._top

        if self._top == None:
            return None

        if self._top.data == target:
            removed = self._top
            self._top = self._top.next
            return f"Element removed: {removed.data}"

        while w is not None:
            if w.next is None:
                return f"Target: {target} not found!"
            elif w.next.data == target:
                aletrnative_pointer = w.next.next
                w.next = aletrnative_pointer #it points to the next element on the list, not to my target anymore
                return "Target removed"
            else:
                w = w.next
                